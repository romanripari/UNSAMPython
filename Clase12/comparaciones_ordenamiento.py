# %%
import random
from matplotlib import pyplot as plt
from numpy import log, log2
import pandas as pd

# ord merge_sort
def merge_sort(lista, comparaciones = 0):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    comparaciones +=1
    if len(lista) < 2:
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        izq, comparaciones = merge_sort(lista[:medio], comparaciones)
        der, comparaciones = merge_sort(lista[medio:], comparaciones)
        lista_nueva, comparaciones = merge(izq, der, comparaciones)

    return lista_nueva, comparaciones

def merge(lista1, lista2, comparaciones):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []

    while(i < len(lista1) and j < len(lista2)):
        comparaciones += 1
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1
    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado, comparaciones

# ord_insercion
def ord_insercion(lista):
    comparaciones = 0
    for i in range(len(lista) - 1):
        comparaciones += 1
        if lista[i + 1] < lista[i]:
            comp = reubicar(lista, i + 1)
            comparaciones += comp

    return comparaciones

def reubicar(lista, p):
    comp = 0
    v = lista[p]
    j = p
    while j > 0 and v < lista[j - 1]:
        comp += 1
        lista[j] = lista[j - 1]
        j -= 1
    lista[j] = v

    return comp

# ord_seleccion
def ord_seleccion(lista):
    comparaciones = 0
    n = len(lista) - 1
    while n > 0:
        comparaciones += n
        p = buscar_max(lista, 0, n)
        lista[p], lista[n] = lista[n], lista[p]
        n = n - 1

    return comparaciones

def buscar_max(lista, a, b):
    pos_max = a
    for i in range(a + 1, b + 1):
        if lista[i] > lista[pos_max]:
            pos_max = i

    return pos_max


# ord_burbujeo
def ord_burbujeo(lista):
    comparaciones = 0
    for i, _ in enumerate(lista):
        for j in range(0,i):
            comparaciones += 1
            if lista[i] < lista[j]:
                lista[j], lista[i] = lista[i], lista[j] 

    return comparaciones

print(ord_seleccion([3,0,1,2]))


def generar_lista(N):
    '''Genera una lista de N largo, con elementos random de 1 a 1000'''
    return [random.randint(1, 1000) for _ in range(N)]

def experimento(N, k):
    ''' Genera un conjunto k de listas de tamaño N y evalúa las comparaciones 
    realizadas por cada método de ordenamiento.
    Devuelve el promedio de comparaciones realizadas'''
    listas = [generar_lista(N) for _ in range(k)]
    seleccion = [ord_seleccion(lista.copy()) for lista in listas]
    insercion = [ord_insercion(lista.copy()) for lista in listas]
    burbuja = [ord_burbujeo(lista.copy()) for lista in listas]
    merge_sorts = [merge_sort(lista.copy())[1] for lista in listas]

    return (sum(seleccion)/k, sum(insercion)/k , sum(burbuja)/k, sum(merge_sorts)/k) 

def grafica(listas, titulos):
    '''Recibe 4 series y las grafica, dándoles cierta suavización w=5'''
    w = 5
    for i in range(len(listas)):
        l = pd.Series(listas[i]).rolling(w).mean()
        plt.plot(l, label=titulos[i])
    plt.legend()
    plt.show()

def experimento_vectores(Nmax):   
    '''Genera un experimento por cada N, con listas desde 1 hasta Nmax y
    evaluándolas con la función experimento.
    Envía los resultados de comparaciones a la función grafica()'''
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
    grafica([selecciones, inserciones, burbujeos, sort_merges], ["Selección", "Inserción", "Burbujeo", "Merge_Sort"]) 

def run():
    # experimento_vectores(30)
    
    # Pruebas realizadas sobre las funciones:

    print(ord_insercion([5,5,5,5,5]))
    # lista =  [3,2,-1,5,0,2]
    # print(ord_insercion(lista))
    # lista =  [3,2,-1,5,0,2]
    # print(ord_seleccion(lista))
    # lista =  [5,4,3,2,1]
    # print(ord_burbujeo(lista))
    # print(experimento(10, 2))
    # print(experimento(5, 1000))
    # lista =  [random.randint(1, 1000) for _ in range(1000000)]
    # lista =  [3,2,-1,5,0,2]
    # print(ord_burbujeo(lista))
    # print(lista)
    # lista =  [3,2,-1,5,0,2]
    # print(lista)
    # print(experimento(10,2))

if __name__ == "__main__":
    run()