import random
import numpy as np

def medir_temp(n):
    return [37.5 + random.normalvariate(0,0.2) for i in range(n)]

def resumen_temp(n = 999):
    lista = medir_temp(n)
    maximo = max(lista)
    minimo = min(lista)
    promedio =  sum(lista) / n
    lista.sort()
    if n%2 ==1:
        indice = int((n-1) /2 +1)
        mediana = lista[indice]
    else:
        indice = int(n/2)
        mediana = ( lista[indice] +  lista[indice +1] ) / 2

    temperaturas = np.array(lista)
    np.save('../Data/temperaturas.npy', temperaturas)

    tupla = (maximo, minimo, promedio, mediana)
    return tupla

def run():
    print(resumen_temp(1000000))

if __name__ == "__main__":
    run()