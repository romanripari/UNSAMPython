# %%
import numpy as np
import pandas as pd
import timeit as tt
import random
from matplotlib import pyplot as plt


# ord merge_sort
def merge_sort(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    if len(lista) < 2:
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        izq = merge_sort(lista[:medio])
        der = merge_sort(lista[medio:])
        lista_nueva = merge(izq, der)
    return lista_nueva

def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []
    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1
    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]
    return resultado

# ord_insercion
def ord_insercion(lista):
    for i in range(len(lista) - 1):
        if lista[i + 1] < lista[i]:
            reubicar(lista, i + 1)
            
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

def generar_lista(N):
    return [random.randint(1, 1000) for _ in range(N)]

def experimento_timeit_seleccion(listas, num):
    tiempos_seleccion = []
    global lista
    for lista in listas:
        tiempo_seleccion = tt.timeit('ord_seleccion(lista.copy())', number = num, globals = globals())
        tiempos_seleccion.append(tiempo_seleccion)
    tiempos_seleccion = np.array(tiempos_seleccion)
    return tiempos_seleccion

def experimento_timeit_burbujas(listas, num):
    tiempos_burbujas = []
    global lista
    for lista in listas:
        tiempo_burbujas = tt.timeit('ord_burbujeo(lista.copy())', number = num, globals = globals())
        tiempos_burbujas.append(tiempo_burbujas)
    tiempos_burbujas = np.array(tiempos_burbujas)
    return tiempos_burbujas

def experimento_timeit_inserciones(listas, num):
    tiempos_inserciones = []
    global lista
    for lista in listas:
        tiempo_inserciones = tt.timeit('ord_insercion(lista.copy())', number = num, globals = globals())
        tiempos_inserciones.append(tiempo_inserciones)
    tiempos_inserciones = np.array(tiempos_inserciones)
    return tiempos_inserciones

def experimento_timeit_merge_sort(listas, num):
    tiempos_merge_sort = []
    global lista
    for lista in listas: 
        tiempo_merge_sort = tt.timeit('merge_sort(lista.copy())', number = num, globals = globals())
        tiempos_merge_sort.append(tiempo_merge_sort)
    tiempos_merge_sort = np.array(tiempos_merge_sort)
    return tiempos_merge_sort

def grafica(sel, inc, bur, mer):
    w = 5
    sel = pd.Series(sel).rolling(w).mean()
    inc = pd.Series(inc).rolling(w).mean()
    bur = pd.Series(bur).rolling(w).mean()
    mer = pd.Series(mer).rolling(w).mean()
    plt.plot(sel, label="Seleccion")
    plt.plot(inc, label="Inserción")
    plt.plot(mer, label="Merge_Sort")
    plt.plot(bur, "r--", label="Burbujeo")
    plt.legend()
    plt.show()

def experimento(N, k):
    
    listas = [generar_lista(N) for _ in range(k)]
    seleccion = [experimento_timeit_seleccion(lista.copy(),1) for lista in listas]
    insercion = [experimento_timeit_inserciones(lista.copy(),1) for lista in listas]
    burbuja = [experimento_timeit_burbujas(lista.copy(),1) for lista in listas]
    merge_sorts = [experimento_timeit_merge_sort(lista.copy()) for lista in listas]
    return (sum(seleccion)/k, sum(insercion)/k , sum(burbuja)/k, sum(merge_sorts)/k) 

def experimento_timeit(Nmax):   
    selecciones = []
    inserciones  = []
    burbujeos = []
    sort_merges = []
    for N in range(Nmax):
        s, i, b, m = experimento(N, 1)
        selecciones.append(s)
        inserciones.append(i)
        burbujeos.append(b)
        sort_merges.append(m)
    grafica(selecciones, inserciones, burbujeos, sort_merges)

def run():
    # listas = []
    # for N in range(1, 256):
    #     listas.append(generar_lista(N))
    # tiempos_seleccion = experimento_timeit_seleccion(listas, 100)
    # w = 30
    # tiempos_seleccion = pd.Series(tiempos_seleccion).rolling(w).mean()
    # plt.plot(tiempos_seleccion)
    # plt.show()
    experimento_timeit(10)

if __name__ == "__main__":
    run()
