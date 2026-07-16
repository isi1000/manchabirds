"""iberianbirds: paletas de colores inspiradas en aves ibericas y La Mancha.

Sistema de 11 paletas (10 aves + el paisaje manchego), cada una con hasta
3 variantes:
  - cualitativa  -> "abejaruco"        (categorias)
  - secuencial   -> "abejaruco_seq"    (magnitud creciente)
  - divergente   -> "abejaruco_div"    (dato con centro)

Paridad exacta con el paquete de R del mismo nombre.

Uso rapido
----------
>>> import iberianbirds as ib
>>> ib.paleta("manchego")             # lista de hex (cualitativa)
>>> ib.paleta("abejaruco_seq", n=9)   # degradado interpolado a 9
>>> cm = ib.cmap("martin_div")        # colormap divergente de matplotlib
>>> ib.usar_paleta("avefria")         # fija el ciclo de color por defecto
>>> ib.registrar_cmaps()              # registra "iberianbirds_*" en matplotlib
"""
from __future__ import annotations
from typing import List, Optional, Tuple, Dict

from . import _data
from ._data import CUALITATIVA, SECUENCIAL, DIVERGENTE

__version__ = "0.1.0"
__all__ = [
    "CUALITATIVA", "SECUENCIAL", "DIVERGENTE",
    "paleta", "paletas", "hex", "cmap", "listed_cmap",
    "registrar_cmaps", "usar_paleta", "mostrar_paleta", "__version__",
]


# ---------------------------------------------------------------- interno
def _resolver(nombre: str) -> Tuple[str, Dict[str, list], str]:
    if nombre.endswith("_seq"):
        return "seq", SECUENCIAL, nombre[:-4]
    if nombre.endswith("_div"):
        return "div", DIVERGENTE, nombre[:-4]
    return "qual", CUALITATIVA, nombre


def _stops(nombre: str) -> Tuple[str, List[str]]:
    tipo, tabla, base = _resolver(nombre)
    if base not in tabla:
        raise KeyError(
            f"Paleta desconocida: {nombre!r}. Ver iberianbirds.paletas()."
        )
    return tipo, list(tabla[base])


def _hex2rgb(h: str) -> tuple:
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) / 255.0 for i in (0, 2, 4))


def _interp(hexes: List[str], n: int) -> List[str]:
    """Interpola una lista de hex a n colores (lineal en RGB)."""
    if n <= 0:
        return []
    stops = [_hex2rgb(h) for h in hexes]
    if len(stops) == 1:
        stops = stops * 2
    if n == 1:
        stops = [stops[0]]
        return ["#%02X%02X%02X" % tuple(round(v * 255) for v in stops[0])]
    seg = len(stops) - 1
    out = []
    for i in range(n):
        t = i / (n - 1) * seg
        lo = min(int(t), seg - 1)
        f = t - lo
        rgb = tuple(stops[lo][k] + (stops[lo + 1][k] - stops[lo][k]) * f for k in range(3))
        out.append("#%02X%02X%02X" % tuple(round(v * 255) for v in rgb))
    return out


# ---------------------------------------------------------------- publico
def paletas() -> dict:
    """Nombres de todas las paletas disponibles, por tipo."""
    return {
        "cualitativas": list(CUALITATIVA),
        "secuenciales": [f"{k}_seq" for k in SECUENCIAL],
        "divergentes": [f"{k}_div" for k in DIVERGENTE],
    }


def paleta(nombre: str = "manchego", n: Optional[int] = None,
           reverse: bool = False) -> List[str]:
    """Devuelve los colores de una paleta como lista de hex.

    - Cualitativas ("manchego"): sus colores nativos; si n supera el tamano,
      interpola.
    - Secuenciales/divergentes ("manchego_seq", "manchego_div"): interpola a
      n colores (por defecto 7).
    """
    tipo, stops = _stops(nombre)
    if tipo == "qual":
        cols = stops
        if n is None:
            n = len(cols)
        cols = cols[:n] if n <= len(cols) else _interp(cols, n)
    else:
        cols = _interp(stops, 7 if n is None else n)
    return list(reversed(cols)) if reverse else cols


def hex(nombre: str, *nombres: str) -> List[str]:
    """Atajo: devuelve los hex nativos de una o varias paletas cualitativas."""
    todas = [nombre, *nombres]
    out: List[str] = []
    for nm in todas:
        out.extend(paleta(nm))
    return out


def cmap(nombre: str = "manchego_seq", n: int = 256, reverse: bool = False):
    """Colormap continuo (``LinearSegmentedColormap``) de matplotlib.

    Valido para cualquier paleta; para cualitativas interpola sus colores.
    """
    from matplotlib.colors import LinearSegmentedColormap
    tipo, stops = _stops(nombre)
    if reverse:
        stops = list(reversed(stops))
    return LinearSegmentedColormap.from_list(f"iberianbirds_{nombre}", stops, N=n)


def listed_cmap(nombre: str = "manchego", reverse: bool = False):
    """``ListedColormap`` discreto de una paleta cualitativa."""
    from matplotlib.colors import ListedColormap
    return ListedColormap(paleta(nombre, reverse=reverse), name=f"iberianbirds_{nombre}")


def registrar_cmaps() -> List[str]:
    """Registra los degradados (secuenciales y divergentes) en matplotlib.

    Quedan accesibles por nombre, p. ej. ``cmap="iberianbirds_martin_div"``.
    Devuelve la lista de nombres registrados.
    """
    import matplotlib
    try:
        registrar = matplotlib.colormaps.register            # mpl >= 3.6
    except AttributeError:                                    # pragma: no cover
        from matplotlib import cm as _cm
        registrar = _cm.register_cmap
    nombres = [f"{k}_seq" for k in SECUENCIAL] + [f"{k}_div" for k in DIVERGENTE]
    hechos = []
    for nm in nombres:
        cm_ = cmap(nm)
        cm_r = cmap(nm, reverse=True); cm_r.name = f"{cm_.name}_r"
        for c in (cm_, cm_r):
            try:
                registrar(cmap=c)
            except (ValueError, TypeError):
                registrar(name=c.name, cmap=c)
            hechos.append(c.name)
    return hechos


def usar_paleta(nombre: str = "manchego", n: Optional[int] = None,
                reverse: bool = False) -> List[str]:
    """Fija una paleta cualitativa como ciclo de color por defecto de matplotlib."""
    import matplotlib as mpl
    from cycler import cycler
    cols = paleta(nombre, n=n, reverse=reverse)
    mpl.rcParams["axes.prop_cycle"] = cycler(color=cols)
    return cols


def mostrar_paleta(nombre: str = "manchego", n: Optional[int] = None, ax=None):
    """Dibuja una tira de color con la paleta indicada."""
    import matplotlib.pyplot as plt
    tipo = _resolver(nombre)[0]
    if n is None and tipo != "qual":
        n = 9                      # los degradados se muestran con 9 pasos
    cols = paleta(nombre, n=n)
    creado = ax is None
    if creado:
        _, ax = plt.subplots(figsize=(max(4, len(cols) * 0.8), 1.3))
    for i, c in enumerate(cols):
        ax.add_patch(plt.Rectangle((i, 0), 1, 1, color=c))
    ax.set_xlim(0, len(cols)); ax.set_ylim(0, 1)
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_title(f"iberianbirds: {nombre}")
    if creado:
        plt.tight_layout()
    return ax
