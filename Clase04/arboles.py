# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 21:17:31 2021
@author: Román
"""
import csv
from pprint import pprint

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
    # List comprehension múltiple. Es un diccionario, pero el valor es otro List comprehension:
    '''
     diccionario = { clave: valor for clave in claves }
        * clave * ----> e
        * valor * ----> [(valor1, valor2) for diccionario in lista if condicion]
                       valor1      ----> float(arbol['altura_tot'])
                       valor2      ----> float(arbol['diametro'])
                       diccionario ----> arbol
                       lista       ----> arboleda
                       condicion   ----> arbol["nombre_com"] == e
        * valor *                  ----> [(float(arbol['altura_tot']), float(arbol['diametro']))  for arbol in arboleda if arbol["nombre_com"] == e]
        * clave in claves          ----> "for e in especies"
    '''
    diccionario = { e: [(float(arbol['altura_tot']), float(arbol['diametro']))  for arbol in arboleda if arbol["nombre_com"] == e] for e in especies}
    return diccionario

def run():
   
    arboleda  = leer_arboles("../Data/arbolado-en-espacios-verdes.csv")
    print(f'Cnatidad de ítems en lista de todos los árboles: {len(arboleda)}')

#   Ejercicio 4.16: Lista de altos de Jacarandá
    H=[float(arbol['altura_tot']) for arbol in arboleda]
    print(f'Cnatidad de ítems en lista de todas las alturas: {len(H)}')
    jacaranda_H =[float(arbol['altura_tot'])  for arbol in arboleda if arbol["nombre_com"] == "Jacarandá"]
    print(f'Cnatidad de ítems en lista de todas las alturas del Jacarandá: {len(jacaranda_H)}')
    
    # Ejercicio 4.17: Lista de altos y diámetros de Jacarandá
    jacaranda_H =[(float(arbol['altura_tot']), float(arbol['diametro']))  for arbol in arboleda if arbol["nombre_com"] == "Jacarandá"]
    print(f'Cnatidad de ítems en lista de todas las alturas y diámetros del Jacarandá: {len(jacaranda_H)}')

    # Ejercicio 4.18: Diccionario con medidas
    especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
    resultado = medidas_de_especies(especies, arboleda)
    print(f'Ítems para Eucalipto: {len(resultado["Eucalipto"])}')
    print(f'Ítems para Palo borracho rosado: {len(resultado["Palo borracho rosado"])}')
    print(f'Ítems para Jacarandá: {len(resultado["Jacarandá"])}')

# Punto de entrada
if __name__ == "__main__":
    run()
