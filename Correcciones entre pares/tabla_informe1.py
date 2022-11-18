import csv
def leer_camion(camion):
    camion_lista= []
    with open (camion,'rt') as file:
        filas = csv.reader(file)
        encabezado_camion=next(file).split(',')
        for fila in filas:
            try:
                diccionario_camion={}
                diccionario_camion[encabezado_camion[0]]=fila[0]
                diccionario_camion[encabezado_camion[1]]=fila[1]
                diccionario_camion[encabezado_camion[2]]=fila[2]
                camion_lista.append(diccionario_camion)
            except:
                print("No se pudo leer la fila:", fila)
        return camion_lista

def leer_precios(precios):
    lista_precios=[]
    with open (precios,'rt', encoding="UTF-8") as file2:
        filas1=csv.reader(file2)
        for fila1 in filas1:
            try:
                diccionario_precios={}
                diccionario_precios[fila1[0]]=fila1[1]
                lista_precios.append(diccionario_precios)
            except :
                print("No se pudo leer la fila:", fila1)
        return lista_precios

def hacer_informe(a,b):
    dato_tabla=[]
    cont = 0
    headers = ('Nombre','cajones','precio','cambio')
    separador=()
    for i in a:
        valores=list(i.values())
        fruta_camion=valores[0]
        cajones_camion=int(valores[1])
        precios_camion=float(valores[2])
        for k in b:
            fruta=list(k.keys())
            frutax=fruta[0]
            precio_fruta=list(k.values())
            precio_frutax=float(precio_fruta[cont])
            if fruta_camion == frutax:
                l=frutax
                l1=cajones_camion
                l2=precios_camion
                l3=precio_frutax-precios_camion
                lista_tabla=[l,l1,l2,l3]
                dato_tabla.append(lista_tabla)
                break
    titulo1=print("{:>15} {:>15} {:>15} {:>15}".format('Nombre','cajones','precio','cambio'))
    titulo2=print("{:>15} {:>15} {:>15} {:>15}".format('----------','----------','----------','----------'))
    for nombre,cajones ,precio,cambio in dato_tabla:
        titulo3=print (f'{nombre:>15s} {cajones:>15} {precio:>15.2f} {cambio:>15.2f}')
    return titulo1,titulo2,titulo3

a=leer_camion('../Data/camion.csv')
b=leer_precios('../Data/precios.csv')
c=hacer_informe(a,b)