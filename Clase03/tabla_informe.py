import csv

#Arma los precios como datos dentro de un diccionario:
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

#Arma los lotes como diccionarios dentro de una lista:
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

# Conformo las ventas del camión como lista
camion = leer_camion("../Data/camion.csv")
# Armo un diccionario con la lista de precios
precios = leer_precios("../Data/precios.csv")
# Creo el informe
informe = hacer_informe(camion, precios)
headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
separador = "-" * 10
print(f'{separador:>10s} {separador:>10s} {separador:>10s} {separador:>10s}')
for nombre, cajones, precio, cambio in informe:
    precio = "${:,.2f}".format(precio)
    print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')