"""Genera los archivos de datos de R y Python desde sistema-final.json.
Fuente unica de verdad -> paridad garantizada entre ambos paquetes.
"""
import json, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data = json.load(open(os.path.join(BASE, 'shared', 'sistema-final.json'), encoding='utf-8'))['aves']

# Orden: aves primero, manchego (paisaje) al final
orden = ['avutarda','flamenco','focha','abejaruco','rabilargo','cernicalo',
         'jilguero','martin','herrerillo','avefria','camachuelo','manchego']
qual = {k: data[k]['cualitativa'] for k in orden}
seq  = {k: data[k]['secuencial'] for k in orden if data[k].get('secuencial')}
div  = {k: data[k]['divergente'] for k in orden if data[k].get('divergente')}

# ---------------- Python ----------------
def py_dict(d):
    lines = []
    for k, v in d.items():
        cols = ', '.join(f'"{c}"' for c in v)
        lines.append(f'    "{k}": [{cols}],')
    return '\n'.join(lines)

py = f'''"""Datos de las paletas manchabirds (generado desde sistema-final.json).

NO editar a mano: se regenera con shared/generate_packages.py.
Paridad exacta con el paquete de R.
"""

# Paletas CUALITATIVAS (categorias): lista de hex.
CUALITATIVA = {{
{py_dict(qual)}
}}

# Paletas SECUENCIALES (magnitud creciente): puntos de un degradado claro->oscuro.
SECUENCIAL = {{
{py_dict(seq)}
}}

# Paletas DIVERGENTES (dato con centro): polo - neutro - polo.
DIVERGENTE = {{
{py_dict(div)}
}}
'''
open(os.path.join(BASE, 'py-package', 'src', 'manchabirds', '_data.py'), 'w', encoding='utf-8').write(py)

# ---------------- R ----------------
def r_list(d):
    lines = []
    for k, v in d.items():
        cols = ', '.join(f'"{c}"' for c in v)
        lines.append(f'  {k} = c({cols}),')
    s = '\n'.join(lines)
    return s[:-1] if s.endswith(',') else s   # quita ultima coma

r = f'''# Datos de las paletas manchabirds (generado desde sistema-final.json).
# NO editar a mano: se regenera con shared/generate_packages.py.
# Paridad exacta con el paquete de Python.

.mb_cualitativa <- list(
{r_list(qual)}
)

.mb_secuencial <- list(
{r_list(seq)}
)

.mb_divergente <- list(
{r_list(div)}
)
'''
# R usa UTF-8 sin BOM
with open(os.path.join(BASE, 'R-package', 'R', 'paletas-datos.R'), 'w', encoding='utf-8', newline='\n') as f:
    f.write(r)

print('Generado:')
print(' - py-package/src/manchabirds/_data.py')
print(' - R-package/R/paletas-datos.R')
print(f'Paletas: {len(qual)} cualitativas, {len(seq)} secuenciales, {len(div)} divergentes')
