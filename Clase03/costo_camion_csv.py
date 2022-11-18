import csv

def costo_camion(nombre_archivo):
    f = open(nombre_archivo)
    rows = csv.reader(f)
    encabezados = next(rows)
    costo = 0.0
    for n_fila, fila in enumerate(rows, start=1):
        record = dict(zip(encabezados, fila))
        try:
            ncajones = int(record['cajones'])
            precio = float(record['precio'])
            costo += ncajones * precio
        # Esto atrapa errores en los int() y float() de arriba.
        except ValueError:
            print(f'Fila {n_fila}: No pude interpretar: {fila}')
    return costo

costo = costo_camion('../Data/fecha_camion.csv')
print(f'Costo total {costo}')

