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
            costo = costo
    return costo
    
costo = costo_camion('./Data/camion.csv')
print(f'Costo total {costo}')

