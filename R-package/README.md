# iberianbirds (R)

Paletas inspiradas en aves ibéricas y La Mancha para **ggplot2**. Paquete
gemelo del de Python, con paridad exacta de colores.

## Instalación

```r
# install.packages("remotes")
remotes::install_local("R-package")
```

## API

| Función | Qué hace |
|---|---|
| `ib_paletas()` | Nombres de todas las paletas por tipo |
| `ib_paleta("manchego", n, reverse)` | Vector de hex de una paleta |
| `scale_color_iberianbirds("abejaruco")` | Escala discreta (color) |
| `scale_fill_iberianbirds("abejaruco")` | Escala discreta (relleno) |
| `scale_color_iberianbirds_c("abejaruco_seq")` | Escala continua (color) |
| `scale_fill_iberianbirds_c("martin_div")` | Escala continua (relleno) |
| `ib_mostrar("avefria")` | Dibuja la paleta |

## Nomenclatura

- Cualitativa: `"abejaruco"`
- Secuencial: `"abejaruco_seq"`
- Divergente: `"abejaruco_div"`

## Ejemplo

```r
library(ggplot2); library(iberianbirds)
ggplot(iris, aes(Sepal.Length, Petal.Length, color = Species)) +
  geom_point(size = 3) +
  scale_color_iberianbirds("abejaruco") +
  theme_minimal()
```

Más ejemplos en [`inst/examples/demo.R`](inst/examples/demo.R).

> Los datos viven en `R/paletas-datos.R` (generado desde
> `../shared/sistema-final.json`). Regenera con
> `python ../shared/generate_packages.py`. Los `man/*.Rd` se crean con
> `devtools::document()`.
