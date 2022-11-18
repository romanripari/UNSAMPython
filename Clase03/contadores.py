from pprint import pprint
import csv
from collections import Counter

def leer_camion(nombre_archivo):
    camion = []
    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = dict(zip(headers, row))
            record['precio'] = float(record['precio'])
            record['cajones'] = int(record['cajones'])
 # Clase 02:
            # lote = {"nombre": row[0],
            #         "cajones": int(row[1]),
            #         "precio": float(row[2])}
            camion.append(record)
    return camion

camion = leer_camion("../Data/camion.csv")
#print(camion)
tenencias = Counter()
for s in camion:
    tenencias[s['nombre']] += s['cajones']

print(tenencias)
#print(tenencias['Naranja'])
#print(tenencias['Mandarina'])

camion2 = leer_camion('../Data/camion2.csv')
tenencias2 = Counter()

for s in camion2:
    tenencias2[s['nombre']] += s['cajones']

print(tenencias2)

combinada = tenencias + tenencias2

print(combinada)