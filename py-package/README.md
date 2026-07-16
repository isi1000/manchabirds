# iberianbirds (Python)

Paletas inspiradas en aves ibéricas y La Mancha para **matplotlib** y
**seaborn**. Paquete gemelo del de R, con paridad exacta de colores.

## Instalación

```bash
pip install ./py-package
```

## API

| Función | Qué hace |
|---|---|
| `ib.paletas()` | Nombres de todas las paletas por tipo |
| `ib.paleta("manchego", n=None, reverse=False)` | Lista de hex de una paleta |
| `ib.cmap("abejaruco_seq")` | `LinearSegmentedColormap` continuo |
| `ib.listed_cmap("manchego")` | `ListedColormap` discreto |
| `ib.registrar_cmaps()` | Registra `iberianbirds_*` en matplotlib |
| `ib.usar_paleta("avefria")` | Fija el ciclo de color por defecto |
| `ib.mostrar_paleta("flamenco_div")` | Dibuja la paleta |

## Nomenclatura

- Cualitativa: `"abejaruco"`
- Secuencial: `"abejaruco_seq"`
- Divergente: `"abejaruco_div"`

## Ejemplo

```python
import matplotlib.pyplot as plt
import iberianbirds as ib

ib.usar_paleta("manchego")
plt.bar(list("ABCD"), [4, 7, 3, 8])
plt.show()
```

Más ejemplos en [`examples/demo.py`](examples/demo.py) (cualitativa, secuencial
y divergente).

> Los datos viven en `src/iberianbirds/_data.py` (generado desde
> `../shared/sistema-final.json`). Regenera con
> `python ../shared/generate_packages.py`.
