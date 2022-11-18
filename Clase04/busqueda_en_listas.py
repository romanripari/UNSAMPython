def buscar_u_elemento(lista, e):
    '''
    En este primer ejercicio tenés que escribir una función buscar_u_elemento()
    que reciba una lista y un elemento y devuelva
    la posición de la última aparición de ese elemento en la lista
    (o -1 si el elemento no pertenece a la lista).
    '''
    pos_max = -1
    for i, l in enumerate(lista):
        if l == e:
            pos_max = i
    return pos_max


def buscar_n_elemento(lista, e):
    '''
    Agregale a tu programa busqueda_en_listas.py una función buscar_n_elemento()
    que reciba una lista y un elemento y devuelva
    la cantidad de veces que aparece el elemento en la lista. 
    '''
    cantidad = 0
    for i, l in enumerate(lista):
        if l == e:
            cantidad += 1
    return cantidad

def minimo(lista):
    m = 0 # Lo inicializo en 0
    # ¿Primero busco el MÁXIMO?
    for e in lista: # Recorro la lista y voy guardando el MAYOR
        if e > m:
            m = e
    for e in lista: # Recorro la lista y voy guardando el MENOR
        if e < m:
            m = e
    return m

def maximo(lista):
    '''Devuelve el máximo de una lista, 
    la lista debe ser no vacía y de números positivos.
    '''
    m = 0 # Lo inicializo en 0
    # ¿Primero busco el MÍNIMO?
    for e in lista: # Recorro la lista y voy guardando el MENOR
        if e < m:
            m = e
    for e in lista: # Recorro la lista y voy guardando el MAYOR
        if e > m:
            m = e
    return m

def run():

    print(buscar_u_elemento([1,2,3,2,3,4],1))   # 0
    print(buscar_u_elemento([1,2,3,2,3,4],2))   # 3
    print(buscar_u_elemento([1,2,3,2,3,4],3))   # 4
    print(buscar_u_elemento([1,2,3,2,3,4],5))   # -1

    print(buscar_n_elemento([1,2,3,2,3,4],1))   # 1
    print(buscar_n_elemento([1,2,3,2,3,4],2))   # 2
    print(buscar_n_elemento([1,2,3,2,3,4],3))   # 2
    print(buscar_n_elemento([1,2,3,2,3,4],5))   # 0

    print(maximo([1,2,7,2,3,4]))                # 7
    print(maximo([1,2,3,4]))                    # 4
    print(maximo([-5,4]))                       # 4
    print(maximo([-5,-4]))                      # -4

    print(minimo([1,2,7,2,3,4]))                # 1
    print(minimo([1,2,3,4]))                    # 1
    print(minimo([-5,4]))                       # -5
    print(minimo([-5,-4]))                      # -5

if __name__ == "__main__":
    run()
