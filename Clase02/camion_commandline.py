import sys
import csv

def costo_camion(nombre_archivo):
    f = open(nombre_archivo)
    rows = csv.reader(f)
    headers = next(f)
    headers
    costo = 0.0
    for row in rows:
        try:
            costo += (float(row[2].replace('\n', '')) * float(row[1].replace('\n', '')) )
        except ValueError:
            pass
    return costo
    
if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'

costo = costo_camion(nombre_archivo)

print(f'Costo total {costo}')