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

print(busqueda_con_index([1, 4, 54, 3, 0, -1], 1))
print(busqueda_con_index([1, 4, 54, 3, 0, -1], -1))
print(busqueda_con_index([1, 4, 54, 3, 0, -1], 3))
print(busqueda_con_index([1, 4, 54, 3, 0, -1], 44))
print(busqueda_con_index([], 0))

print(busqueda_lineal([1, 4, 54, 3, 0, -1], 44))
print(busqueda_lineal([1, 4, 54, 3, 0, -1], 3))
print(busqueda_lineal([1, 4, 54, 3, 0, -1], 0))
print(busqueda_lineal([], 42))