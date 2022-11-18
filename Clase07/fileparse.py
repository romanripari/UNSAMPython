import csv
from pprint import pprint

def parse_csv(iterable,
                select = None,
                types = None,
                has_headers = True,
                silence_errors = False):
    '''
    Recibe un elemento iterable y devuelve una lista de registros
    select = None -> Recibe como lista las columnas que se seleccionarán
    types = None -> Recibe como lista los tipos de datos para cada columna
    has_headers = True -> Si se indica que tiene encabezado, generará una lista de diccionarios. De lo contrario, una lista de tuplas
    silence_errors = False -> Elegir True para omitir la impresión de errores
    '''
    filas = csv.reader(iterable)
    
    # Lee los encabezados
    if has_headers:
        encabezados = next(filas)

    try:
        if select:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select
        else:
            indices = []
    # Ejercicio 7.1
    # Excepción en caso de que haya elegido campos, pero no tiene encabezado
    except Exception as e:
        raise RuntimeError('Para seleccionar, necesito encabezados.') 

    registros = []
    for i, fila in enumerate(filas):
        try:
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

        # Ejercicio 7.2
        # Excepción en caso de que alguna fila no se pueda procesar por problema de valores
        except ValueError as e:
            # Ejercicio 7.3
            # Bool para que le usuarie decida si ver o no los errores en pantalla
            if not silence_errors:
                print(f'Fila {i+1}: No pude convertir {fila}')
                print(f'Fila {i+1}: Motivo: {e}')
    return registros

def run():
#    parse_csv('../Data/precios.csv', select = ['nombre','precio'], has_headers = False)
    precios = parse_csv('../Data/precios.csv', types=[str,float])
#    camion = parse_csv('../Data/camion.csv', select=["nombre", "cajones"], has_headers=True)
#    camion = parse_csv('../Data/missing.csv', types = [str, int, float], silence_errors=True)    
#    pprint(camion)
#    precios = parse_csv('../Data/precios.csv', select = ['nombre','precio'], has_headers = False)
    pprint(precios)
if __name__ == "__main__":
    run()