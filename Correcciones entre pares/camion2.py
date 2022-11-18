# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 14:38:18 2021

@author: Win8
"""
#%%
# camion.py
# VERSION NO ITERABLE.
# class Camion:

#     def __init__(self, lotes):
#         self.lotes = lotes

#     def precio_total(self):
#         return sum([l.costo() for l in self.lotes])

#     def contar_cajones(self):
#         from collections import Counter
#         cantidad_total = Counter()
#         for l in self.lotes:
#             cantidad_total[l.nombre] += l.cajones
#         return cantidad_total
    
    
#%%

# VERSION ITERABLE.
# Ejercicio 10.2

# class Camion:

#     def __init__(self, lotes):
#         self.lotes = lotes

#     def __iter__(self):
#         return self.lotes.__iter__()

#     def precio_total(self):
#         return sum([l.costo() for l in self.lotes])

#     def contar_cajones(self):
#         from collections import Counter
#         cantidad_total = Counter()
#         for lote in self.lotes:
#             cantidad_total[lote.nombre] += lote.cajones
#         return cantidad_total

#%%

# Metodos Magicos.
# Ejercicio 10.3:
# import informe_final    
class Camion:
  def __init__(self, lotes):
        self.lotes = lotes

  def __iter__(self):
        return self.lotes.__iter__()
  
  def __len__(self):
      return len(self.lotes)

 
  def __getitem__ (self, position): # Un método especial para obtener valores por índice
         return self.lotes[position]
    
  #Esta funcion me da error,
  #TypeError: 'Camion' object is not subscriptable
  
  def __contains__(self, nombre):
        return any([lote.nombre == nombre for lote in self.lotes])

    
  def precio_total(self):
        return sum([l.costo() for l in self.lotes])
    
    # No me toma esta funcion
  def __str__(self):
      return f'({self.lotes})'

    # No me toma esta funcion
  def __repr__(self):
      return f'Date({self.lotes})'
  
  def contar_cajones(self):
        from collections import Counter
        cantidad_total = Counter()
        for l in self.lotes:
            cantidad_total[l.nombre] += l.cajones
        return cantidad_total




#%%

# camion = informe_final.leer_camion('../Data/camion.csv')
   




#%%




#%%