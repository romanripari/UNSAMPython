def pascal(n, k):
    '''Recibe un número de fila {n} y de columna {k},
    retorna el valor según el tríangulo de Pascal'''
    if k > n:                                  # Si la columna es mayor que la fila significa que no hay más para sumar
        return 0
    if k == 0 or n == 0:                        # Si llego a la primera columna o primera fila, sumo 1
        return 1 
    return pascal(n-1,k) + pascal(n-1,k-1)      # Sumo la (fila anterior, misma columna) + (fila anterior, columna anterior)

def imprime():
    print("\n".join(["{:^40}".format("  ".join([f'{pascal(n,k)}' for k in range(n+1)])) for n in range(10)]))

def run():
    imprime()
    # print(pascal(8, 8))     # 10
    # print(pascal(10, 5))    # 252
    # print(pascal(5, 3))     # 10
    # print(pascal(7, 0))     # 1
    # print(pascal(9, 8))     # 9

if __name__ == '__main__':
    run()