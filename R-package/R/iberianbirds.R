#' iberianbirds: paletas inspiradas en aves ibericas y La Mancha
#'
#' Sistema de 11 paletas (10 aves + el paisaje manchego), cada una con hasta
#' 3 variantes: cualitativa ("abejaruco"), secuencial ("abejaruco_seq") y
#' divergente ("abejaruco_div"). Paridad exacta con el paquete de Python.
#'
#' @keywords internal
"_PACKAGE"

# Resuelve un nombre de paleta al tipo, tabla y nombre base.
.ib_resolver <- function(nombre) {
  if (grepl("_seq$", nombre)) return(list("seq", .ib_secuencial, sub("_seq$", "", nombre)))
  if (grepl("_div$", nombre)) return(list("div", .ib_divergente, sub("_div$", "", nombre)))
  list("qual", .ib_cualitativa, nombre)
}

.ib_stops <- function(nombre) {
  r <- .ib_resolver(nombre)
  tipo <- r[[1]]; tabla <- r[[2]]; base <- r[[3]]
  if (is.null(tabla[[base]]))
    stop("Paleta desconocida: '", nombre, "'. Ver ib_paletas().")
  list(tipo = tipo, cols = tabla[[base]])
}

#' Nombres de las paletas disponibles
#'
#' @return Lista con los nombres por tipo (cualitativas, secuenciales, divergentes).
#' @export
ib_paletas <- function() {
  list(
    cualitativas = names(.ib_cualitativa),
    secuenciales = paste0(names(.ib_secuencial), "_seq"),
    divergentes  = paste0(names(.ib_divergente), "_div")
  )
}

#' Obtener los colores de una paleta
#'
#' @param nombre Nombre de la paleta. Cualitativa: "manchego". Secuencial:
#'   "manchego_seq". Divergente: "manchego_div".
#' @param n Numero de colores. Cualitativas: por defecto todos (interpola si
#'   se pide mas). Secuenciales/divergentes: por defecto 7 (interpola).
#' @param reverse Invertir el orden.
#' @return Vector de caracteres con codigos hexadecimales.
#' @examples
#' ib_paleta("manchego")
#' ib_paleta("abejaruco_seq", n = 9)
#' @export
ib_paleta <- function(nombre = "manchego", n = NULL, reverse = FALSE) {
  s <- .ib_stops(nombre); cols <- s$cols
  if (s$tipo == "qual") {
    if (is.null(n)) n <- length(cols)
    cols <- if (n <= length(cols)) cols[seq_len(n)]
            else grDevices::colorRampPalette(cols)(n)
  } else {
    if (is.null(n)) n <- 7
    cols <- grDevices::colorRampPalette(cols)(n)
  }
  if (reverse) cols <- rev(cols)
  cols
}

# Funcion de paleta para ggplot2 (discreta).
.ib_pal_discreta <- function(nombre, reverse = FALSE) {
  function(n) ib_paleta(nombre, n = n, reverse = reverse)
}

#' Escala de color discreta (cualitativa) para ggplot2
#'
#' @param paleta Nombre de una paleta cualitativa (p. ej. "manchego").
#' @param reverse Invertir el orden.
#' @param ... Parametros para `ggplot2::discrete_scale`.
#' @return Objeto de escala de ggplot2.
#' @export
scale_color_iberianbirds <- function(paleta = "manchego", reverse = FALSE, ...) {
  ggplot2::discrete_scale("colour", palette = .ib_pal_discreta(paleta, reverse), ...)
}
#' @rdname scale_color_iberianbirds
#' @export
scale_colour_iberianbirds <- scale_color_iberianbirds

#' Escala de relleno discreta (cualitativa) para ggplot2
#' @inheritParams scale_color_iberianbirds
#' @return Objeto de escala de ggplot2.
#' @export
scale_fill_iberianbirds <- function(paleta = "manchego", reverse = FALSE, ...) {
  ggplot2::discrete_scale("fill", palette = .ib_pal_discreta(paleta, reverse), ...)
}

#' Escala de color continua (secuencial o divergente) para ggplot2
#'
#' @param paleta Nombre de una paleta secuencial o divergente (p. ej.
#'   "abejaruco_seq", "martin_div").
#' @param reverse Invertir el degradado.
#' @param ... Parametros para `ggplot2::scale_color_gradientn`.
#' @return Objeto de escala de ggplot2.
#' @export
scale_color_iberianbirds_c <- function(paleta = "manchego_seq", reverse = FALSE, ...) {
  ggplot2::scale_color_gradientn(colours = ib_paleta(paleta, n = 256, reverse = reverse), ...)
}
#' @rdname scale_color_iberianbirds_c
#' @export
scale_colour_iberianbirds_c <- scale_color_iberianbirds_c

#' Escala de relleno continua (secuencial o divergente) para ggplot2
#' @inheritParams scale_color_iberianbirds_c
#' @return Objeto de escala de ggplot2.
#' @export
scale_fill_iberianbirds_c <- function(paleta = "manchego_seq", reverse = FALSE, ...) {
  ggplot2::scale_fill_gradientn(colours = ib_paleta(paleta, n = 256, reverse = reverse), ...)
}

#' Visualizar una paleta
#'
#' @param nombre Nombre de la paleta.
#' @param n Numero de colores (por defecto: nativo si cualitativa, 9 si degradado).
#' @return Dibuja la paleta (devuelve NULL invisible).
#' @export
ib_mostrar <- function(nombre = "manchego", n = NULL) {
  tipo <- .ib_resolver(nombre)[[1]]
  if (is.null(n) && tipo != "qual") n <- 9
  cols <- ib_paleta(nombre, n = n)
  n <- length(cols)
  graphics::image(seq_len(n), 1, as.matrix(seq_len(n)), col = cols,
                  axes = FALSE, xlab = "", ylab = "",
                  main = paste0("iberianbirds: ", nombre))
  invisible(NULL)
}
