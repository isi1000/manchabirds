"""Datos de las paletas iberianbirds (generado desde sistema-final.json).

NO editar a mano: se regenera con shared/generate_packages.py.
Paridad exacta con el paquete de R.
"""

# Paletas CUALITATIVAS (categorias): lista de hex.
CUALITATIVA = {
    "avutarda": ["#B4B8BB", "#F1E7D5", "#C8842A", "#A5522A", "#241206"],
    "flamenco": ["#F3D3D6", "#F14E33", "#D6437B", "#6BAAC9", "#191920"],
    "focha": ["#B81A1A", "#ECE7DC", "#6F7883", "#1A1A1D", "#B9C0C7"],
    "abejaruco": ["#99D3DB", "#F8E463", "#D29B57", "#6C9661", "#3B4049", "#F1E9D4"],
    "rabilargo": ["#2B91AE", "#E1B170", "#AFCDCA", "#3B3C36"],
    "cernicalo": ["#A5A9B2", "#A17971", "#F5D52F", "#E2C2A6", "#443F48"],
    "jilguero": ["#D64135", "#1F1D23", "#FEF355", "#CE9B7B", "#E2D7D5"],
    "martin": ["#FBB058", "#58D2EB", "#198EB6", "#283238", "#DDE8F2"],
    "herrerillo": ["#2C549A", "#DED363", "#4E93CE", "#1E1E3A", "#D2D7D7"],
    "avefria": ["#AE4F94", "#65895D", "#4497A7", "#D39C5B", "#2D3540", "#CFCFD9"],
    "camachuelo": ["#EE5E48", "#7B92A7", "#E0998C", "#15151B", "#D2D2CD"],
    "manchego": ["#3150B5", "#E7E1D6", "#C0362B", "#3C4650", "#8FB8E0", "#E8C24A", "#C96A38", "#7E8E3C"],
}

# Paletas SECUENCIALES (magnitud creciente): puntos de un degradado claro->oscuro.
SECUENCIAL = {
    "avutarda": ["#FBF5EB", "#A5522A", "#5E2E14"],
    "flamenco": ["#FDEFF3", "#E894BA", "#D6437B", "#B83063"],
    "focha": ["#ECE7DC", "#1A1A1D"],
    "abejaruco": ["#F4FBFC", "#99D3DB", "#3F9BB2", "#154E62"],
    "rabilargo": ["#EAF1EF", "#AFCDCA", "#2B91AE", "#1F3D48"],
    "cernicalo": ["#F3E6D6", "#E2C2A6", "#A17971", "#443F48"],
    "jilguero": ["#FCF8F6", "#D64135", "#7C1B15"],
    "martin": ["#EAF3FA", "#58D2EB", "#198EB6", "#283238"],
    "herrerillo": ["#ECEEEF", "#4E93CE", "#2C549A", "#1E1E3A"],
    "avefria": ["#F2E6EE", "#AE4F94", "#3A2038"],
    "camachuelo": ["#F9EEEA", "#E0998C", "#EE5E48", "#AF241A"],
    "manchego": ["#EFEAE0", "#8FB8E0", "#3150B5", "#1B2C6A"],
}

# Paletas DIVERGENTES (dato con centro): polo - neutro - polo.
DIVERGENTE = {
    "avutarda": ["#A5522A", "#F4ECDD", "#5A6064"],
    "flamenco": ["#F14E33", "#F4ECEA", "#9FB4C4"],
    "focha": ["#B81A1A", "#ECE7DC", "#1A1A1D"],
    "abejaruco": ["#EFCB1E", "#F4EFE1", "#4FAEC2"],
    "rabilargo": ["#D19A47", "#EDE7D8", "#1E7E9A"],
    "jilguero": ["#D64135", "#F7EDE0", "#1F1D23"],
    "martin": ["#EE9628", "#ECEDE8", "#12708F"],
    "herrerillo": ["#D2C63E", "#EDEDE6", "#254B8C"],
    "avefria": ["#9E3D82", "#EEEAE2", "#C4882C"],
    "camachuelo": ["#EA5B46", "#EFE9E4", "#6E85A0"],
    "manchego": ["#AE2E22", "#EFE9DC", "#2C4AA8"],
}
