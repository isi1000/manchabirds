# manchabirds (Python)

Paletas inspiradas en aves ibéricas y La Mancha para **matplotlib** y
**seaborn**. Paquete gemelo del de R, con paridad exacta de colores.

## Instalación

```bash
pip install ./py-package
```

## API

| Función | Qué hace |
|---|---|
| `mb.paletas()` | Nombres de todas las paletas por tipo |
| `mb.paleta("manchego", n=None, reverse=False)` | Lista de hex de una paleta |
| `mb.cmap("abejaruco_seq")` | `LinearSegmentedColormap` continuo |
| `mb.listed_cmap("manchego")` | `ListedColormap` discreto |
| `mb.registrar_cmaps()` | Registra `manchabirds_*` en matplotlib |
| `mb.usar_paleta("avefria")` | Fija el ciclo de color por defecto |
| `mb.mostrar_paleta("flamenco_div")` | Dibuja la paleta |

## Nomenclatura

- Cualitativa: `"abejaruco"`
- Secuencial: `"abejaruco_seq"`
- Divergente: `"abejaruco_div"`

## Ejemplo

```python
import matplotlib.pyplot as plt
import manchabirds as mb

mb.usar_paleta("manchego")
plt.bar(list("ABCD"), [4, 7, 3, 8])
plt.show()
```

Más ejemplos en [`examples/demo.py`](examples/demo.py) (cualitativa, secuencial
y divergente).

> Los datos viven en `src/manchabirds/_data.py` (generado desde
> `../shared/sistema-final.json`). Regenera con
> `python ../shared/generate_packages.py`.
