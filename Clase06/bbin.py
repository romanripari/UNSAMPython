


def donde_insertar(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    Si no está en la lista, devuelve la posición en que podría insertarse
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

    # Agregado para devolver el index de dónde 
    # debería insertarse un valor si no está en la lista
    if pos < 0:
        pos +=1
        while pos < len(lista) and lista[pos] < x:
            pos += 1
    return pos

def insertar(lista, x):
    pos = donde_insertar(lista,x)
    if x not in lista:
        lista.insert(pos, x)
    return pos

def run():
    print(insertar([0,1,3,5,6,8], 9))
if __name__ == "__main__":
    run()