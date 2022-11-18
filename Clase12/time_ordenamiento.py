# %%
import numpy as np
import pandas as pd
import timeit as tt
import random
from matplotlib import pyplot as plt

# ord merge_sort
def merge_sort(lista):
    if len(lista) < 2:
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        izq = merge_sort(lista[:medio])
        der = merge_sort(lista[medio:])
        lista_nueva = merge(izq, der)
    return lista_nueva
def merge(lista1, lista2):
    i, j = 0, 0
    resultado = []
    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1
    resultado += lista1[i:]
    resultado += lista2[j:]
    return resultado

# ord_insercion
def ord_insercion(lista):
    for i in range(len(lista) - 1):
        if lista[i + 1] < lista[i]:
            comp = reubicar(lista, i + 1)
    return 

def reubicar(lista, p):
    v = lista[p]
    j = p
    while j > 0 and v < lista[j - 1]:
        lista[j] = lista[j - 1]
        j -= 1
    lista[j] = v
    return 

# ord_seleccion
def ord_seleccion(lista):
    n = len(lista) - 1
    while n > 0:
        p = buscar_max(lista, 0, n)
        lista[p], lista[n] = lista[n], lista[p]
        n = n - 1
    return 

def buscar_max(lista, a, b):
    pos_max = a
    for i in range(a + 1, b + 1):
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max

# ord_burbujeo
def ord_burbujeo(lista):
    for i, _ in enumerate(lista):
        for j in range(0,i):
            if lista[i] < lista[j]:
                lista[j], lista[i] = lista[i], lista[j] 
    return 

def experimento_timeit_seleccion(listas, num):
    '''Realiza UN experimento con la lista, evalúa y retorna el tiempo
    que tardó el método Selección'''
    tiempos_seleccion = []
    global lista
    for lista in listas:
        tiempo_seleccion = tt.timeit('ord_seleccion(lista.copy())', number = num, globals = globals())
        tiempos_seleccion.append(tiempo_seleccion)
    tiempos_seleccion = np.array(tiempos_seleccion)
    return tiempos_seleccion

def experimento_timeit_burbujas(listas, num):
    '''Realiza UN experimento con la lista, evalúa y retorna el tiempo
    que tardó el método Burbujeo'''
    tiempos_burbujas = []
    global lista
    for lista in listas:
        tiempo_burbujas = tt.timeit('ord_burbujeo(lista.copy())', number = num, globals = globals())
        tiempos_burbujas.append(tiempo_burbujas)
    tiempos_burbujas = np.array(tiempos_burbujas)
    return tiempos_burbujas

def experimento_timeit_inserciones(listas, num):
    '''Realiza UN experimento con la lista, evalúa y retorna el tiempo
    que tardó el método Inserción'''
    tiempos_inserciones = []
    global lista
    for lista in listas:
        tiempo_inserciones = tt.timeit('ord_insercion(lista.copy())', number = num, globals = globals())
        tiempos_inserciones.append(tiempo_inserciones)
    tiempos_inserciones = np.array(tiempos_inserciones)
    return tiempos_inserciones

def experimento_timeit_merge_sort(listas, num):
    '''Realiza UN experimento con la lista, evalúa y retorna el tiempo
    que tardó el método Merge_Sort'''
    tiempos_merge_sort = []
    global lista
    for lista in listas: 
        tiempo_merge_sort = tt.timeit('merge_sort(lista.copy())', number = num, globals = globals())
        tiempos_merge_sort.append(tiempo_merge_sort)
    tiempos_merge_sort = np.array(tiempos_merge_sort)
    return tiempos_merge_sort


def grafica(listas, titulos):
    '''Recibe 4 series y las grafica, dándoles cierta suavización w=5'''
    w = 5
    for i in range(len(listas)):
        l = pd.Series(listas[i]).rolling(w).mean()
        plt.plot(l, label=titulos[i])
    plt.legend()
    plt.show()

def generar_lista(N):
    '''Genera una lista de N largo, con elementos random de 1 a 1000'''
    return [random.randint(1, 1000) for _ in range(N)]

def experimento_timeit(Nmax):   
    '''Genera un experimento por cada N, con listas desde 1 hasta Nmax y
    evaluándolas con la función experimento_timeit_[metodo].
    Envía los resultados de tiempos a la función grafica()'''
    selecciones = []
    inserciones  = []
    burbujeos = []
    sort_merges = []
    for N in range(Nmax):
        listas = [generar_lista(N) for _ in range(1)]
        selecciones.append(experimento_timeit_seleccion(listas.copy(), 1))
        inserciones.append(experimento_timeit_inserciones(listas.copy(), 1))
        burbujeos.append(experimento_timeit_burbujas(listas.copy(), 1))
        sort_merges.append(experimento_timeit_merge_sort(listas.copy(), 1))
    grafica([selecciones, inserciones, burbujeos, sort_merges], ["Selección", "Inserción", "Burbujeo", "Merge_Sort"]) 

def run():
    experimento_timeit(20)

    # Pruebas realizadas sobre las funciones:

    # print(merge_sort([4,5,3,54,54,76,7,21,1,35,1345,5662,0,-10]*2))
    # unalista = [1, 4, 3, 1, 7, 5]
    # otralista = [7, 6, 5, 4, 3, 2, 1, 0]
    # print(merge_sort(otralista))
    # otralista = [7, 6, 5, 4, 3, 2, 1, 0]
    # print(merge3sort(otralista))

if __name__ == "__main__":
    run()