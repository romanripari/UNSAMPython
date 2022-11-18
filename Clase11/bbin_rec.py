def bbinaria_rec(lista, e):
    '''La función devuelve True o False indicando si {e} está o no en la {lista}'''
    if len(lista) == 0:
        res = False
    elif len(lista) == 1:
        res = lista[0] == e
    else:
        medio = len(lista)//2                       # Determino la nueva mitad
        if e >= lista[medio]:                       # Si el número es mayor o igual que el valor del medio,
            res = bbinaria_rec(lista[medio:],e)     # entonces vuelvo a buscar en la lista DESDE la mitad.
        else:                                       # Si el número menor que el valor del medio,
            res = bbinaria_rec(lista[:medio],e)     # entonces vuelvo a buscar en la lista HASTA la mitad.
    return res

def run():
    lista = [-1,2,3,4,5,6,7,8]
    e = -1
    print(bbinaria_rec(lista, e))

if __name__ == "__main__":
    run()

