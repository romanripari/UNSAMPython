def potencia(base, exp):
    'Calcula la potencia exp del número base, con exp entero mayor que 0.'
    resultado = 1
    for i in range(exp):
        resultado *= base
    return resultado

def maximo(lista):
    'Devuelve el elemento máximo de la lista o None si está vacía.'
    if not lista:
        return None
    max_elem = lista[0]
    for elemento in lista:
        if elemento > max_elem:
            max_elem = elemento
    return max_elem
    
def sumar_enteros(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    suma = 0
    for i in range(desde, hasta+1):
        suma += i
    
    return suma

def sumar_enteros2(desde, hasta):
    suma2 = hasta * (hasta + 1) / 2 - (desde - 1) * desde / 2
    return suma2

print(sumar_enteros(31,25))
print(sumar_enteros2(31,25))

