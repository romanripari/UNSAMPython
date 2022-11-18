def valor_absoluto(n):
    '''
    Reciba un número real y devuelve su valor absoluto

    Pre: n es un número real
    Pos: Devuelve un número real, el valor absoluto de n
    '''
    if n >= 0:
        return n
    else:
        return -n
def suma_pares(l):
    '''
    Reciba una lista y devuelve la suma de todos los
    números pares que contiene
    
    Pre: l es una lista 
    Pos: Se devuelve la sumatoria de todos los números 
        pares contenidos en 'l'. Si no hay ninguno, devuelve 0
    '''
    res = 0
    for e in l:
        if e % 2 ==0:
            res += e
        # else:
        #     res += 0
    # Invariante: res
    return res

def veces(a, b):
    '''
    Recibe dos números enteros y devuelve la multiplicación
    entre el primero y el segundo

    Pre: 'a' es un número real y 'b' es un número entero positivo
    Pos: Devuelve un número real, la multiplicación de 'a' * 'b'
    '''
    res = 0
    nb = b
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1
    # Invariante: res
    return res

def collatz(n):
    '''
    Devuelve la cantidad de ciclos necesarios para alcanzar
    el número 1 según la conjetura de Collatz, comenzando en un número real 'n'
    
    Pre: 'n' es un número entero positivo
    Pos: Devuelve la cantidad de ciclos necesarios para llegar a 1
    '''
    res = 1
    # Continuará el ciclo mientras que no sea 1 
    while n!=1:
        # Si el número es par, se divide por dos. Caso contrario, se multiplca por 3 y se le suma 1.
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1
    # Invariante: res
    return res

# print(veces(13.4,3.1))
# print(help(valor_absoluto))
# print(help(suma_pares))
# print(help(veces))
# print(help(collatz))

# import this
