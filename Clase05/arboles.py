# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 21:17:31 2021
@author: Román
"""
import os
import matplotlib.pyplot as plt
import csv
from pprint import pprint
import numpy as np

# Funciones de clase 04
# Ejercicio 4.15: Lectura de todos los árboles
def leer_arboles(nombre_archivo):
    resultado = []
    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        rows = csv.reader(f)
        encabezados = next(rows)
        for row in rows:
            record = {}
            record = dict(zip(encabezados, row))
            for encabezado in encabezados:                
                record[encabezado] = record[encabezado]
            resultado.append(record)
    return resultado

def medidas_de_especies(especies, arboleda):
    diccionario = { e: [(float(arbol['altura_tot']), float(arbol['diametro']))  for arbol in arboleda if arbol["nombre_com"] == e] for e in especies}
    return diccionario

def histograma_alturas():
    nombre_archivo = os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
    arboleda = leer_arboles(nombre_archivo)
    altos = [float(arbol['altura_tot']) for arbol in arboleda if arbol["nombre_com"] == "Jacarandá"]
    plt.hist(altos,bins=50)
    plt.show()

def scatter_hd(lista_de_pares):
    d = [d[1] for d in lista_de_pares]
    h = [d[0] for d in lista_de_pares]
    area = (15 * np.random.rand(len(lista_de_pares)))**2  # 0 to 15 point radii
    plt.scatter(d,h, s=area, alpha=0.3)
    plt.xlabel("diametro (cm)")
    plt.ylabel("alto (m)")
    plt.title("Relación diámetro-alto para Jacarandás")
    plt.show()


def run():
#    histograma_alturas()
    nombre_archivo = os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
    arboleda = leer_arboles(nombre_archivo)
    jacaranda_H =[(float(arbol['altura_tot']), float(arbol['diametro']))  for arbol in arboleda if arbol["nombre_com"] == "Jacarandá"]
#    scatter_hd(jacaranda_H)

    especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
    medidas = medidas_de_especies(especies, arboleda)
    scatter_hd(medidas["Eucalipto"])
    scatter_hd(medidas["Palo borracho rosado"])
    scatter_hd(medidas["Jacarandá"])

#     arboleda  = leer_arboles("../Data/arbolado-en-espacios-verdes.csv")
#     print(f'Cnatidad de ítems en lista de todos los árboles: {len(arboleda)}')

# #   Ejercicio 4.16: Lista de altos de Jacarandá
#     H=[float(arbol['altura_tot']) for arbol in arboleda]
#     print(f'Cnatidad de ítems en lista de todas las alturas: {len(H)}')
#     jacaranda_H =[float(arbol['altura_tot'])  for arbol in arboleda if arbol["nombre_com"] == "Jacarandá"]
#     print(f'Cnatidad de ítems en lista de todas las alturas del Jacarandá: {len(jacaranda_H)}')
    
#     # Ejercicio 4.17: Lista de altos y diámetros de Jacarandá
#     jacaranda_H =[(float(arbol['altura_tot']), float(arbol['diametro']))  for arbol in arboleda if arbol["nombre_com"] == "Jacarandá"]
#     print(f'Cnatidad de ítems en lista de todas las alturas y diámetros del Jacarandá: {len(jacaranda_H)}')

#     # Ejercicio 4.18: Diccionario con medidas
#     especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
#     resultado = medidas_de_especies(especies, arboleda)
#     print(f'Ítems para Eucalipto: {len(resultado["Eucalipto"])}')
#     print(f'Ítems para Palo borracho rosado: {len(resultado["Palo borracho rosado"])}')
#     print(f'Ítems para Jacarandá: {len(resultado["Jacarandá"])}')

# Punto de entrada
if __name__ == "__main__":
    run()
