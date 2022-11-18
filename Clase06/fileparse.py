import csv
from pprint import pprint

def parse_csv(nombre_archivo, select = None, types = None, has_headers = True):
    '''
    Parsea un archivo CSV en una lista de registros
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)
        # Lee los encabezados
        if has_headers:
            encabezados = next(filas)
        if select:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select
        else:
            indices = []
        registros = []

        for fila in filas:
            if not fila:    # Saltear filas vacías
                continue
            # Filtrar la fila si se especificaron columnas
            if indices:
                fila = [fila[index] for index in indices]
            # Si se le indicaron tipos, los agrega a los valores
            if types:
                fila = [func(val) for func, val in zip(types, fila) ]
            #Si tiene encabezados, crea diccionarios. Si no, crea tuplas con todos los campos de la fila
            if has_headers:
                registro = dict(zip(encabezados, fila))
            else:
                registro = tuple(f for f in fila)
            registros.append(registro)
    return registros

def run():
    precios = parse_csv('../Data/precios.csv', types=[str,float], has_headers=False)
    camion = parse_csv('../Data/camion.csv', select=["nombre", "cajones"])
    pprint(precios)
    pprint(camion)
if __name__ == "__main__":
    run()