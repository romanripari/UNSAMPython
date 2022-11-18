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

def run():
    lista = [3, 1, 0, 4, 2]
    lista = [6, 0, 3, 2, 5, 7, 4, 1]
    print(merge_sort(lista)[1])
    lista = [6, 0, 3, 2, 5, 7, 4, 1]*2
    print(merge_sort(lista)[1])
    lista = [6, 0, 3, 2, 5, 7, 4, 1]*3
    print(merge_sort(lista)[1])
    lista = [5,4,3,2,1]
    print(merge_sort(lista)[1])

if __name__ == '__main__':
    run()