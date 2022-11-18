# tabla_informe.py
#%%
# funcion leer_precios
import csv
def leer_precios(nombre_archivo):
    with open(nombre_archivo, 'rt', encoding="UTF-8") as f:
        FILAS = csv.reader(f)
        encabezado = ['nombre', 'precio']
        precios = {}
        for n_fila,fila in enumerate(FILAS):
            record = dict(zip(encabezado,fila)) #esto es importante
            try:
                #print(row)
                precios[record['nombre']] = float(record['precio'])     
                #print(precios)
            except KeyError:
                print('******Faltan datos en la línea', n_fila, 'del archivo*****')
        return precios

#%%
# funcion leer_camion
import csv
def leer_camion(nombre_archivo):
    with open(nombre_archivo, 'rt') as f:
        lote = {}
        camion =[]
        FILAS = csv.reader(f)
        encabezado = next(FILAS)
        for n_fila,fila in enumerate(FILAS):
            try:
                record = dict(zip(encabezado, fila))
                lote = {       
                    'nombre' : record['nombre'],
                    'cajones': int(record['cajones']),
                    'precio': float(record['precio'])
                    } #construimos el dicion. con las claves 'nombre',etc, pueden ser cualquier nombre pero los hacemos coincidir 
                camion.append(lote)
                #print(camion)
            except ValueError:
                print(f'*****Fila {n_fila}: No puede interpretar: {fila}****')
        return camion 

#%%
# funcion hacer_informe
def hacer_informe(camion,precios):
    informe = []
    for ind,prod in enumerate(camion):
        name = camion[ind]['nombre']
        tupa = (
                camion[ind]['nombre'],
                camion[ind]['cajones'],
                camion[ind]['precio'],
                (precios[name] - camion[ind]['precio'])
                )
        informe.append(tupa)
    return informe

#%%
# evaluamos la funcion leer_camion
archivo_camion = '../Data/camion2.csv'
camion = leer_camion(archivo_camion)

#%%
# evaluamos la funcion leer_precios
archivo_precios = '../Data/precios.csv'
precios = leer_precios(archivo_precios)

#%%
# evaluamos la funcion hacer_informe
informe = hacer_informe(camion, precios)

#%%
# generamos la tabla

headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
barrita = ('---------- ---------- ---------- ----------')
print(f'{(headers[0]):>10s} {(headers[1]):>10s} {(headers[2]):>10s} {(headers[3]):>10s}')
print(f'{(barrita):>10s}')
for nombre, cajones, precio, cambio in informe:
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10.2f} {cambio:>10.2f}')


# resultado:
#     Nombre    Cajones     Precio     Cambio
# ---------- ---------- ---------- ----------
#       Lima        100      32.20       8.02
#    Naranja         50      91.10      15.18
#      Caqui        150     103.44       2.02
#  Mandarina        200      51.23      29.66
#    Durazno         95      40.37      33.11
#  Mandarina         50      65.10      15.79
#    Naranja        100      70.44      35.84