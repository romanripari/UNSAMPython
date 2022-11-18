def ord_burbujeo(lista):
    '''Recibe una lista y la devuelve ordenada'''
    # Comienza el contador en cero
    comparaciones = 0
    for i, _ in enumerate(lista):
        # Recorro desde el principio de la lista hasta el elemento i-1
        for j in range(0,i):
            # Cada vez que realiza comparaciones entre dos elementos de la lista,
            # aumenta en uno la cantidad de comparaciones
            comparaciones += 1
            # Si el elemento en i es menor que el elemento en j, lo intercambio
            if lista[i] < lista[j]:
                lista[j], lista[i] = lista[i], lista[j]
            
    return lista

'''
La función ord_burbujeo realiza N^2 comparaciones.

En el peor de los casos, cada elemento se compara con todos sus anteriores:
T(N) = (1 * 0 + 2 * 1 + 3 * 2 ... N * N-1)

Por lo tanto, se puede resumir en 
N*N = N^2
'''
def run():
    pass
    # Pruebas:
    lista = [5, 4, 3, 2, 1]
    print(lista)
    ord_burbujeo(lista)
    print(lista)

    lista = [1, 2, -3, 8, 1, 5]
    print(lista)
    ord_burbujeo(lista)
    print(lista)

    lista = [1, 2, 3, 4, 5]
    print(lista)
    ord_burbujeo(lista)
    print(lista)

    lista = [0, 9, 3, 8, 5, 3, 2, 4]
    print(lista)
    ord_burbujeo(lista)
    print(lista)

    lista = [10, 8, 6, 2, -2, -5]
    print(lista)
    ord_burbujeo(lista)
    print(lista)

    lista = [2, 5, 1, 0]
    print(lista)
    ord_burbujeo(lista)
    print(lista)

    lista = [10,9,8,7,6,5,4,3,2,1]
    print(lista)
    ord_burbujeo(lista)
    print(lista)
    
if __name__ == "__main__":
    run()