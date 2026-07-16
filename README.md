# iberianbirds 🐦

Sistema de **11 paletas de colores** inspiradas en **aves ibéricas** y en el
**paisaje manchego**, con **paquetes gemelos en R y Python** (paridad exacta).
Cada paleta tiene hasta **3 variantes**: cualitativa, secuencial y divergente.
Colores extraídos y afinados a partir de fotografías reales, pensados para
figuras cohesivas y elegantes en artículos científicos.

![Sistema completo](shared/iberianbirds-sistema-completo.png)

## Las 11 paletas

**Aves:** avutarda · flamenco · focha · abejaruco · rabilargo · cernícalo ·
jilguero · martín (pescador) · herrerillo · avefría · camachuelo
**Paisaje:** manchego (los 4 colores de bandera + el paisaje)

## Nomenclatura

| Variante | Nombre | Para qué |
|---|---|---|
| Cualitativa | `abejaruco` | categorías (datos sin orden) |
| Secuencial | `abejaruco_seq` | magnitud creciente (mapas de calor) |
| Divergente | `abejaruco_div` | dato con centro (anomalías, correlaciones) |

*(El `cernícalo` solo tiene cualitativa y secuencial.)*

## R

```r
# install.packages("remotes")
remotes::install_local("R-package")

library(ggplot2); library(iberianbirds)
ggplot(mtcars, aes(wt, mpg, color = factor(cyl))) +
  geom_point() + scale_color_iberianbirds("manchego")

# continua (secuencial o divergente)
ggplot(faithful, aes(waiting, eruptions, color = eruptions)) +
  geom_point() + scale_color_iberianbirds_c("abejaruco_seq")
```

## Python

```bash
pip install ./py-package
```
```python
import iberianbirds as ib
ib.usar_paleta("avefria")              # ciclo de color por defecto
ib.registrar_cmaps()                   # colormaps "iberianbirds_*"
plt.imshow(z, cmap="iberianbirds_martin_div")
```

## Estructura

```
Paletas/
├── shared/
│   ├── sistema-final.json              ← fuente única de verdad
│   ├── generate_packages.py            ← genera los datos de R y Python
│   ├── iberianbirds-sistema-completo.png
│   ├── boletin-calidad.png             ← auditoría (ΔE, daltonismo, rango)
│   └── aves/                           ← estudio de cada paleta
├── R-package/                          ← paquete R
└── py-package/                         ← paquete Python
```

Para regenerar los datos tras editar `sistema-final.json`:
`python shared/generate_packages.py`

## Paridad R ↔ Python

Los colores nativos (cualitativas y puntos de los degradados) son
**bit-idénticos**. Las rampas interpoladas coinciden dentro de ±1/255.
