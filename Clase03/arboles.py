# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 21:17:31 2021
@author: Román
"""
import csv
from collections import Counter

# Ejercicio 3.18: Lectura de los árboles de un parque
# Con el nombre del archivo y un parque, devuelve una lista que contiene diccionarios.
# Estos diccionarios tienen como claves todos los encabezados
def leer_parque(nombre_archivo:str, parque:str)->list:
    resultado = []
    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        rows = csv.reader(f)
        encabezados = next(rows)
        for row in rows:
            record = {}
            record = dict(zip(encabezados, row))
            if record["espacio_ve"] == parque:
                for encabezado in encabezados:                
                    record[encabezado] = record[encabezado]
                resultado.append(record)
    return resultado

# Ejercicio 3.19: Determinar las especies en un parque
# De una lista de árboles (con todos sus detalles) de un parque específico, 
# devuelve un SET de los nombres únicos de árboles
def leer_especies(lista_arboles:list)->set:
    resultado = set([])
    for arboles in lista_arboles:
        resultado.add(arboles["nombre_com"])
    return resultado

# Ejercicio 3.20: Contar ejemplares por especie
# Recibe una lista de árboles (con todos sus detalles) y devuelve un diccionario que contiene 
# como clave el nombre del árbol y como valor, va agregando += 1 cada vez que aparece uno igual
# Al final el diccionario se queda solo con los "top" mejores
def contar_ejemplares(lista_arboles:list, top:int)->dict:
    ejemplares = Counter()
    dict_resultado = {}
    for arboles in lista_arboles:
        arbol = arboles["nombre_com"]
        ejemplares[arbol] += 1
        dict_resultado[arbol] = ejemplares[arbol]
    dict_resultado = ejemplares.most_common(top)
    return dict_resultado

# Ejercicio 3.21: Alturas de una especie en una lista
# Recibe una lista de árboles (con todos sus detalles), la recorre y si el nombre del árbol
# es igual a la especie brindada, agrega su altura a una lista. 
def obtener_alturas(lista_arboles:list, especie:str)-> list:
    alturas = []
    for arboles in lista_arboles:
        if arboles["nombre_com"] == especie:
            alturas.append(float(arboles["altura_tot"]))
    return alturas

# Ejercicio 3.22: Inclinaciones por especie de una lista
# Recibe una lista de árboles (con todos sus detalles), la recorre y si el nombre del árbol
# es igual a la especie brindada, agrega su INCLINACIÓN a una lista. 
def obtener_inclinaciones(lista_arboles:list, especie:str)-> list:
    inclinacion = []
    for arboles in lista_arboles:
        if arboles["nombre_com"] == especie:
            inclinacion.append(float(arboles["inclinacio"]))
    return inclinacion

# Ejercicio 3.23: Especie con el ejemplar más inclinado
# Recibe una lista de árboles (con todos sus detalles), la recorre y si la inclinación
# es mayor a la última inclinación registrada, guarda el nombre del árbol y esa inclinación. 
def especimen_mas_inclinado(lista_arboles:list)->str:
    inclinacion_maxima = 0.0
    nuevamaxima = 0.0
    especies =  leer_especies(lista_arboles)
    for especie in especies:
        inclinacion = obtener_inclinaciones(lista_arboles, especie)
        nuevamaxima = max(inclinacion)
        try:
            if nuevamaxima > inclinacion_maxima:
                arbol = especie
                inclinacion_maxima = nuevamaxima
        except:
            pass
    return f'{arbol}, con una inclinación de: {inclinacion_maxima}'

# Ejercicio 3.24: Especie más inclinada en promedio
# Recibe una lista de árboles (con todos sus detalles), y genera una lista con todos sus nombres de árboles.
# A esa lista la vuelve a recorrer y le obtiene una lista de inclinaciones.
# Con esa lista, saca el promedio de inclinación para la especia, y verifica si es la más alta
# Si es mayor a la última inclinación registrada, guarda el nombre del árbol y esa inclinación promediada. 
def especie_promedio_mas_inclinada(lista_arboles:list)->str:
    inclinacion_maxima = 0.0
    nuevamaxima = 0.0
    especies =  leer_especies(lista_arboles)
    for especie in especies:
        inclinacion = obtener_inclinaciones(lista_arboles, especie)
        nuevamaxima =  sum(inclinacion) /len(inclinacion)
        try:
            if nuevamaxima > inclinacion_maxima:
                arbol = especie
                inclinacion_maxima = nuevamaxima
        except:
            pass
    return f'{arbol}, con una inclinación de: {inclinacion_maxima}'


# Esta función contiene TODOS los ejercicios juntos. 
# Se pueden ir comentando para que el print no sea tan largo
def ejercicios_arboles(strparque, especie):

    print("*" * 10)
    print(strparque)
    print("*" * 10)

    # Ejercicio 3.18: Lectura de los árboles de un parque
    parque = leer_parque("../Data/arbolado-en-espacios-verdes.csv", strparque)
#    print(len(parque))


    # Ejercicio 3.19: Determinar las especies en un parque
#    print(len(leer_especies(parque)))


    # Ejercicio 3.20: Contar ejemplares por especie
#    print(contar_ejemplares(parque, 5))


    # Ejercicio 3.21: Alturas de una especie en una lista
    altura = obtener_alturas(parque, especie)
#    print(altura)
    print(f'Altura máxima del {especie}: {max(altura)}')
    print(f'Altura promedio del {especie}: {float(sum(altura)/len(altura)):0.2f}')


    # Ejercicio 3.22: Inclinaciones por especie de una lista
#    print(obtener_inclinaciones(parque, especie))  


    # Ejercicio 3.23: Especie con el ejemplar más inclinado
    print(f'El árbol más inclinado es {especimen_mas_inclinado(parque)}')


    #Ejercicio 3.24: Especie más inclinada en promedio
    print(f'La especia más inclinada es {especie_promedio_mas_inclinada(parque)}')
    print(" ")


# Función RUN para ejecutar todo con tres parque diferentes

def run():
    especie = "Jacarandá"
    strparque = "GENERAL PAZ"
    ejercicios_arboles(strparque, especie)

    strparque = "ANDES, LOS"
    ejercicios_arboles(strparque, especie)
    
    strparque = "CENTENARIO"
    ejercicios_arboles(strparque, especie)


# Punto de entrada
if __name__ == "__main__":
    run()
