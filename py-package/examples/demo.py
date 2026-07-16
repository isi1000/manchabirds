"""Ejemplos de uso de iberianbirds en matplotlib y seaborn."""
import numpy as np
import matplotlib.pyplot as plt
import iberianbirds as ib


def demo_cualitativa():
    """Barras categoricas con la paleta manchega."""
    ib.usar_paleta("manchego")
    cats = list("ABCDEFGH")
    vals = [5, 9, 3, 7, 4, 8, 6, 5]
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.bar(cats, vals, color=ib.paleta("manchego"))
    ax.set_title("iberianbirds — manchego (cualitativa)")
    fig.tight_layout()
    return fig


def demo_secuencial():
    """Mapa de calor con un colormap secuencial."""
    ib.registrar_cmaps()
    z = np.random.default_rng(0).normal(size=(20, 20)).cumsum(0).cumsum(1)
    fig, ax = plt.subplots(figsize=(5, 4))
    im = ax.imshow(z, cmap="iberianbirds_abejaruco_seq")
    fig.colorbar(im, ax=ax)
    ax.set_title("iberianbirds — abejaruco_seq")
    fig.tight_layout()
    return fig


def demo_divergente():
    """Matriz centrada en 0 con un colormap divergente (naranja-azul)."""
    from matplotlib.colors import TwoSlopeNorm
    rng = np.random.default_rng(3)
    z = rng.normal(size=(12, 12))
    z = (z + z.T) / 2
    fig, ax = plt.subplots(figsize=(5, 4))
    im = ax.imshow(z, cmap=ib.cmap("martin_div"), norm=TwoSlopeNorm(0))
    fig.colorbar(im, ax=ax)
    ax.set_title("iberianbirds — martin_div (naranja-azul)")
    fig.tight_layout()
    return fig


if __name__ == "__main__":
    demo_cualitativa()
    demo_secuencial()
    demo_divergente()
    plt.show()
