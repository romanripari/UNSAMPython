# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 21:53:48 2021

@author: Román
"""
#Defino el máximo de filas y columnas
tabla = 10

#Cadena vacía, para el primer espacio del encabezado
cadena = " "*4
valor = 0

#Recorro las C (columnas) para imprimir los encabezados
for c in range(tabla+1):
    cadena += f'{valor:>4d}'
    valor += 1
print(cadena)    

#Imprimo el separador
print("-" * (tabla +2) * 4 + "-")

#   Recorro las F (Filas), en cada una voy armando un string que contiene
#   primero la fila en sí con un ":" y luego de manera espaciadas, columna
#   a columna, cada valor sumándole el valor de la fila.
#   Por ejemplo: la fila del 3 empieza en cero, y se le va sumando 3: 0, 3, 6, 9, etc.
for f in range(tabla +1):
    sfila =f'{f}:'
    cadena = f'{sfila:^4}'
    valor = 0
    for c in range(tabla +1):
        cadena += f'{valor:>4d}'
        valor += f
    print(cadena)    
    
