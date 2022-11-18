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
    '''
    Lee un archivo de lotes en un camión 
    y lo devuelve como lista de diccionarios con claves
    nombre, cajones, precio.

    '''
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

def hacer_informe(camion, precios):
    informe = []
    mi_tupla = ()
    for s in camion:
        nombre = s["nombre"]
        cajones = int(s['cajones'])
        precio = float(s['precio'])
        cambio = float((float(precios[s["nombre"]])) - precio)
        mi_tupla = (nombre, cajones, precio, cambio)
        informe.append(mi_tupla)
    return informe

def imprimir_informe(informe):
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    separador = "-" * 10
    print(f'{separador:>10s} {separador:>10s} {separador:>10s} {separador:>10s}')
    for nombre, cajones, precio, cambio in informe:
        precio = "${:,.2f}".format(precio)
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')

def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    camion = leer_camion(nombre_archivo_camion)
    precios = leer_precios(nombre_archivo_precios)
    informe = hacer_informe(camion, precios)
    imprimir_informe(informe)       

informe_camion('../Data/camion.csv', '../Data/precios.csv')

def run():
    informe_camion('../Data/camion.csv', '../Data/precios.csv')
    # nombre_archivo_camion = "../Data/camion.csv"
    # nombre_archivo_precios = "../Data/precios.csv"
    # informe_camion(nombre_archivo_camion, nombre_archivo_precios)

    files = ['../Data/camion.csv', '../Data/camion2.csv']
    for name in files:
        print(f'{name:-^43s}')
        informe_camion(name, '../Data/precios.csv')
        print()

if __name__ == "__main__":
    run()