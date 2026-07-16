"""Lamina maestra del sistema manchabirds: 11 paletas x 3 tipos."""
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.colors import LinearSegmentedColormap
import numpy as np
import manchabirds as ib
from manchabirds import CUALITATIVA, SECUENCIAL, DIVERGENTE

orden = list(CUALITATIVA)
grad = np.linspace(0, 1, 128).reshape(1, -1)

fig, ax = plt.subplots(figsize=(15, 0.92 * len(orden) + 1.2))
# tres columnas: cualitativa (x0..7), secuencial (8..12.5), divergente (13..17.5)
def draw_qual(y, cols):
    w = 7.0 / len(cols)
    for i, c in enumerate(cols):
        ax.add_patch(Rectangle((i * w, y - 0.4), w, 0.8, color=c, ec='white', lw=1.2))
def draw_grad(y, x0, x1, stops):
    cm = LinearSegmentedColormap.from_list('x', stops, 128)
    ax.imshow(grad, aspect='auto', cmap=cm, extent=[x0, x1, y - 0.4, y + 0.4], zorder=2)

y = len(orden)
for name in orden:
    ax.text(-0.35, y, name, ha='right', va='center', fontsize=13, weight='bold')
    draw_qual(y, CUALITATIVA[name])
    if name in SECUENCIAL:
        draw_grad(y, 8.0, 12.3, SECUENCIAL[name])
    if name in DIVERGENTE:
        draw_grad(y, 13.0, 17.3, DIVERGENTE[name])
    else:
        ax.text(15.15, y, 'sin divergente', ha='center', va='center', fontsize=8, color='#999', style='italic')
    y -= 1
# cabeceras
for x, t in [(3.5, 'CUALITATIVA  ·  categorias'),
             (10.15, 'SECUENCIAL  ·  _seq'),
             (15.15, 'DIVERGENTE  ·  _div')]:
    ax.text(x, len(orden) + 0.75, t, ha='center', fontsize=12.5, weight='bold', color='#333')
ax.set_xlim(-2.9, 17.6); ax.set_ylim(0, len(orden) + 1.3); ax.axis('off')
ax.set_title('manchabirds  —  sistema completo de paletas (10 aves + paisaje manchego)',
             fontsize=17, weight='bold', loc='left', y=1.01)
fig.text(0.5, 0.005, 'Colores extraidos y afinados de fotografias reales  ·  paridad R / Python  ·  cernicalo solo cualitativa+secuencial',
         ha='center', fontsize=9, color='#666')
fig.savefig('shared/manchabirds-sistema-completo.png', dpi=150, bbox_inches='tight')
print('ok ->', len(orden), 'paletas')
