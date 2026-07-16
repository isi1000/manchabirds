# Ejemplos de uso de manchabirds con ggplot2
library(ggplot2)
library(manchabirds)

# Ver las paletas disponibles
mb_paletas()

# 1. Cualitativa (categorias) con la paleta manchega
df <- data.frame(cat = LETTERS[1:8], val = c(5, 9, 3, 7, 4, 8, 6, 5))
ggplot(df, aes(cat, val, fill = cat)) +
  geom_col() +
  scale_fill_manchabirds("manchego") +
  labs(title = "manchabirds — manchego (cualitativa)") +
  theme_minimal()

# 2. Puntos por grupo con el abejaruco
ggplot(iris, aes(Sepal.Length, Petal.Length, color = Species)) +
  geom_point(size = 3) +
  scale_color_manchabirds("abejaruco") +
  theme_minimal()

# 3. Continua secuencial
ggplot(faithful, aes(waiting, eruptions, color = eruptions)) +
  geom_point(size = 2) +
  scale_color_manchabirds_c("rabilargo_seq") +
  theme_minimal()

# 4. Continua divergente (naranja-azul del martin pescador)
ggplot(mtcars, aes(wt, mpg, color = scale(drat)[, 1])) +
  geom_point(size = 3) +
  scale_color_manchabirds_c("martin_div") +
  labs(color = "drat (z)") +
  theme_minimal()

# 5. Ver una paleta
mb_mostrar("avefria")
mb_mostrar("flamenco_seq")
