import csv
import fileparse

def leer_precios(nombre_archivo):
    with open(nombre_archivo) as f:
        precios = fileparse.parse_csv(f, types=[str,float], has_headers=False)
    precios = dict(precios)
    return precios

def leer_camion(nombre_archivo):
    with open(nombre_archivo) as f:
        camion = fileparse.parse_csv(f)
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


def f_principal(parametros):
    if len(parametros) != 3:
        raise SystemExit(f'Uso adecuado: {parametros[0]} ' 'archivo_camion archivo_precios')
    camion = parametros[1]
    precios = parametros[2]
    informe_camion(camion, precios)
    print()
    # files = ['../Data/camion.csv', '../Data/camion2.csv']
    # for name in files:
    #     print(f'{name:-^43s}')
    #     informe_camion(name, '../Data/precios.csv')
    #     print()

if __name__ == "__main__":
    import sys
    f_principal(sys.argv)