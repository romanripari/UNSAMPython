import csv
import informe_final
from vigilante import vigilar
from formato_tabla import crear_formateador

def parsear_datos(lines):
    rows = csv.reader(lines)
    # Filtramos las filas según los índices 0, 1 y 2 y creamos un generador a partir de rows
    rows = ([row[index] for index in [0, 1, 2]] for row in rows )  #  rows = elegir_columnas(rows, [0, 1, 2])
    # Creamos un generador para formatear los datatypes
    rows = ( [func(val) for func, val in zip([str, float, int], row)] for row in rows)    # rows = cambiar_tipo(rows, [str, float, int])
    # Creamos un generador de diccionarios a partir del generador anterior
    headers = ['Nombre', 'Precio', 'Volumen']
    rows = (dict(zip(headers, row)) for row in rows)                # rows = hace_dicts(rows, ['nombre', 'precio', 'volumen'])
    return rows

def ticker(camion_file, log_file, fmt):
    '''
    Función que filtra de un log_file todos los productos que aparezcan
    en camion_file y los muestra con el formato 'fmt'
    '''
    # Creamos el Camion()
    camion = informe_final.leer_camion(camion_file)
    # Comenzamos el iterador en rows
    rows = parsear_datos(vigilar(log_file))
    # Filtramos las filas según el contenido de camión
    rows = (row for row in rows if row['Nombre'] in camion)         # rows = filtrar_datos(rows, camion)
    # Creamos el formateador con el formato elegido
    formateador = crear_formateador(fmt)
    # Variable booleana para imprimir una vez el encabezado
    encabezado = False
    for row in rows:
        print(type(row))
        if not encabezado:
            # Imprime los encabezados con el formateador, si todavía no lo hizo:
            formateador.encabezado([str(_) for _ in row])
            # Imprime cada línea con el formateador:
            formateador.fila([str(r) for r in row.values()])
            encabezado = True
        else:
            # Imprime cada línea con el formateador:
            formateador.fila([str(r) for r in row.values()])

if __name__ == '__main__':
    # HTML:
    # ticker('../Data/camion.csv', '../Data/mercadolog.csv', 'html')
    # CSV:
    # ticker('../Data/camion.csv', '../Data/mercadolog.csv', 'csv')
    # TXT:
    ticker('../Data/camion.csv', '../Data/mercadolog.csv', 'txt')