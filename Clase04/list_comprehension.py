
# [<expresión> for <variable> in <secuencia> if <condición>]

# resultado = []
# for variable in secuencia:
#     if condición:
#         resultado.append(expresión)

# s = range(10)

# a = [x * x for x in s if x > 0] # Python

# print(a)

# a = {x^2 | x ∈ s, x > 0}        # Matemática

import csv

def leer_precios(nombre_archivo):
    precios = {}
    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                precios[row[0]] = float(row[1])
            except:
                pass    
    return precios

def leer_camion(nombre_archivo):
    camion = []
    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            lote = {"nombre": row[0],
                    "cajones": int(row[1]),
                    "precio": float(row[2])}
            camion.append(lote)
    return camion

camion = leer_camion("../Data/camion.csv")
precios = leer_precios('../Data/precios.csv')

frutas = [s['nombre'] for s in camion]
a = [s for s in camion if s['precio'] > 100 and s['cajones'] > 50]

costo = sum([s['cajones']*s['precio'] for s in camion])
valor = sum([s['cajones'] * precios[s["nombre"]] for s in camion])

print(costo)    
print(valor)

