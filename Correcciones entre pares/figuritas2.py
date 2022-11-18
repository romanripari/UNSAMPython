'''
Ejercicio 5.10: Crear
Implementá la función crear_album(figus_total) que devuelve un álbum (vector) vacío con figus_total espacios para pegar 
figuritas.
'''

import numpy as np

def crear_album(figus_total):
    album = np.zeros(shape = figus_total)
    return album

#%%
'''
Ejercicio 5.11: Incompleto
Implementá la función album_incompleto(A) que recibe un vector y devuelve True si el álbum A no está completo y False 
si está completo.
'''

import numpy as np
def album_incompleto(A): # si en A usamos 0 para indicar que aún no la conseguimos y 1 para indicar que sí
    return A.min() == 0 # nos devuelve True si el valor minimo es 0

print(album_incompleto(np.array([0, 2, 3, 4])))

#%%
'''
Ejercicio 5.12: Comprar
Implementá una función comprar_figu(figus_total) que reciba el número total de figuritas que tiene el álbum (dado por el 
parámetro figus_total) y devuelva un número entero aleatorio que representa la figurita que nos tocó.
'''

import random

def comprar_figu(figus_total):    
    figurita = random.randint(1, figus_total) # genera un entero aleatorio
    return figurita

print(comprar_figu(10))

#%%
'''
Ejercicio 5.13: Cantidad de compras
Implementá la función cuantas_figus(figus_total) que, dado el tamaño del álbum (figus_total), genere un álbum nuevo, 
simule su llenado y devuelva la cantidad de figuritas que se debieron comprar para completarlo.
'''
import numpy as np

def crear_album(figus_total):
    album = np.zeros(shape = figus_total)
    return album

import random

def cuantas_figus(figus_total):    
    album = crear_album(figus_total)
    compradas = 0
    while album_incompleto(album):
        compradas +=1
        album[comprar_figu(figus_total) -1] = 1
    return compradas
    '''
    ***** Comento el código anterior, arriba dejé el mío ↑ ***** 

    album = crear_album(figus_total)
    for i in range(figus_total):
        album[i] = 1 # simula el llenado del album
        # Quiero incluir el caso de que hayan figuritas repetidas en forma aleatoria
        j = random.randint(1, figus_total - 1)
        if i == j:
            album[i] += 1  
    total = sum(album) 
#    print(album)     
    return total
    '''

print(cuantas_figus(6))

#%%
'''
Ejercicio 5.14:
Ejecutá n_repeticiones = 1000 veces la función anterior utilizando figus_total = 6 y guardá en una lista los resultados 
obtenidos en cada repetición. Con los resultados obtenidos estimá cuántas figuritas hay que comprar, en promedio, para 
completar el álbum de seis figuritas.
Ayuda: El comando np.mean(l) devuelve el promedio de la lista l.
¿Podés crear esta lista usando una comprensión de listas?
'''

import numpy as np

def repeticiones(n):
    lista = [cuantas_figus(6) for i in range(n)] #guardo en una lista los resultados usando comprension de listas
    promedio = np.mean(lista)
    print(f'Para completar el álbum de 6 figuritas hay que comprar un promedio de {promedio} figuritas')    
    return lista

#saqué un print
repeticiones(1000)

#%%
'''
Ejercicio 5.15:
Escribí una función llamada experimento_figus(n_repeticiones, figus_total) que simule el llenado de n_repeticiones álbums 
de figus_total figuritas y devuelva el número estimado de figuritas que hay que comprar, en promedio, para completar el 
álbum.
Para esto, una posibilidad es que la función experimento_figus() llame a la función cuantas_figus() tantas veces como lo 
indica el parámetro n_repeticiones y guarde los resultados parciales en una lista, a partir de la cual luego realice el 
promedio.
¿Cuánto te da para 100 repeticiones en un álbum de 670 figuritas?
'''

import numpy as np


def experimento_figus(n, figus_total):
    lista = [cuantas_figus(figus_total) for i in range(n)] #guardo en una lista los resultados usando comprension de listas
    promedio = np.mean(lista)
    print(f'Para completar el álbum de {figus_total} figuritas hay que comprar un promedio de {promedio} figuritas')    
    return lista
#saqué un print
experimento_figus(100, 670)
