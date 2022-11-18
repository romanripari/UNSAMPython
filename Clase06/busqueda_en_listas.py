#print(  [1, 3, 5, 7].index(5))
def busqueda_con_index(lista, e):
    '''Busca un elemento e en la lista.

    Si e está en lista devuelve el índice,
    de lo contrario devuelve -1.
    '''
    if e in lista:
        pos = lista.index(e)
    else:
        pos = -1
    return pos


def busqueda_lineal(lista, e):
    '''Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    '''
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista): # recorremos la lista
        if z == e:   # si encontramos a e
            pos = i  # guardamos su posición
            break    # y salimos del ciclo
    return pos

def busqueda_lineal_lordenada(lista,e):
#    lista = sorted(lista)
    vueltas= 0 
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista): # recorremos la lista
        vueltas +=1 
        if z == e:   # si encontramos a e
            pos = i  # guardamos su posición
            break    # y salimos del ciclo
        if z > e: 
            break
    return vueltas 

def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos

def run():
    '''
    **Pregunta:** En la línea medio = (izq + der) // 2 efectuamos la división usando el operador // en lugar de /. ¿Qué pasaría su usáramos /?
    
    Nos podría dar un resultado terminado en 0.5 y los índices son solo con números enteros
    '''
    print(busqueda_binaria([2, 3, 5, 7, 11, 13, 15], 7, verbose = True))
    print(busqueda_binaria([1, 3, 5], 1, verbose = True))
    # print(busqueda_lineal([1, 4, 54, 3, 0, -1], 44))
    # print(busqueda_lineal([1, 4, 54, 3, 0, -1], 3))
    # print(busqueda_lineal([1, 4, 54, 3, 0, -1], 0))
    # print(busqueda_lineal([], 42))

    # print(busqueda_lineal_lordenada([1, 4, 54, 3, 0, -1], 44))
    # print(busqueda_lineal_lordenada([1, 4, 54, 3, 0, -1], 3))
    # print(busqueda_lineal_lordenada([1, 4, 54, 3, 0, -1], 0))
    # print(busqueda_lineal_lordenada([], 42))


if __name__ == "__main__":
    run()