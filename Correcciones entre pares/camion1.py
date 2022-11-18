# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 21:15:17 2021

@author: natal
"""

'''
Ejercicio 10.2: Iteración sobre objetos
Ejercicio 10.3: Un iterador adecuado
Ejercicio 10.14: Expresiones generadoras como argumentos en funciones.
'''

class Camion:

    def __init__(self, lotes):
        self.lotes = lotes    
    
    
    def __iter__(self):
        '''
        Este método hace iterable la clase Camion
        '''
        return self.lotes.__iter__()
    
    
    def __contains__(self, nombre):
        '''
        Este método permite utilizar el operador in. Dado un nombre como str
        devuelve True si nombre esta dentro del lote, y False en caso contrario.
        '''
        return any((lote.nombre == nombre for lote in self.lotes))
    
    
    def __len__(self):
        '''
        Este método devuelve la cantidad de elementos del lote
        '''
        return self.lotes.__len__()
    
    
    def __getitem__(self, pos):
        '''
        Este método permite obtener un elmento del lote dada la posición
        '''
        return self.lotes.__getitem__(pos)
    
    
    def __repr__(self):
        '''
        Este método genera una representación de los objetos Camion
        '''
        return f'Camion({self.lotes})'
    
    
    def __str__(self):
        '''
        Este método permite realizar una impresion de los objetos Camion
        '''
        mensaje = f'Camion con {len(self)} lotes:'
        
        for lote in self.lotes:
            mensaje += f'\nLote con {lote.cajones} cajones de {lote.nombre}, pagados a ${lote.precio} cada uno.'
        
        return mensaje


    def precio_total(self):
        '''
        Este método calcula la el precio total        
        '''
        return sum((l.costo() for l in self.lotes))


    def contar_cajones(self):
        '''
        Este método calcula la cantidad total de cajones del lote
        '''
        from collections import Counter
        cantidad_total = Counter()
        for l in self.lotes:
            cantidad_total[l.nombre] += l.cajones
        return cantidad_total