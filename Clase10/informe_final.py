#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (Me basé en parte en el código ofrecido en la clase 09, aunque el mío funcionaba bien)
'''
informe_final.py
'''

import fileparse
import lote
import formato_tabla
from camion import Camion

def leer_camion(filename):
    '''
    Lee un archivo con el contenido de un camión
    y lo devuelve como un objeto Camion.
    '''
    with open(filename) as file:
        camiondicts = fileparse.parse_csv(file,
                                        select = ['nombre', 'cajones', 'precio'],
                                        types = [str, int, float])

    camion = [lote.Lote(d['nombre'], d['cajones'], d['precio']) for d in camiondicts]
    return Camion(camion)

def leer_precios(nombre_archivo):
    with open(nombre_archivo) as f:
        precios = fileparse.parse_csv(f, types = [str, float], has_headers = False)
    return precios

def hacer_informe(camion, precios):
    lista = []
    for lote in camion:
        cambio = precios[lote.nombre] - lote.precio
        t = (lote.nombre, lote.cajones, lote.precio, cambio)
        lista.append(t)
    return lista

def imprimir_informe(informe, formateador):
    formateador.encabezado(['Nombre', 'Cantidad', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in informe:
        rowdata = [nombre, str(cajones), f'${precio:0.2f}', f'{cambio:0.2f}']
        formateador.fila(rowdata)

def informe_camion(nombre_archivo_camion, nombre_archivo_precios, fmt = 'txt'):
    camion = leer_camion(nombre_archivo_camion)
    lista_precios = leer_precios(nombre_archivo_precios)
    precios = dict(lista_precios)
    informe = hacer_informe(camion, precios)

    formateador = formato_tabla.crear_formateador(fmt)        
    imprimir_informe(informe, formateador)

def run(argumentos):
    if len(argumentos) != 3 and len(argumentos) != 4:
        raise SystemExit(f'Uso adecuado: {argumentos[0]} ' 'archivo_camion archivo_precios formato_opcional')
    if len(argumentos) == 3:
        informe_camion(argumentos[1], argumentos[2])
    elif len(argumentos) == 4:
        informe_camion(argumentos[1], argumentos[2], argumentos[3])

if __name__ == '__main__':
    import sys
    run(sys.argv)
    






