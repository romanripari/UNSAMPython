# %% El archivo larenga.py del Ejercicio 11.9.
from larenga import pascal
print("\n".join(["{:^40}".format("  ".join([f'{pascal(n,k)}' for k in range(n+1)])) for n in range(10)]))

# %% El archivo bbin_rec.py del Ejercicio 11.11.
from bbin_rec import bbinaria_rec
lista = [-1,2,3,4.5,4.55,6,7,8]
e = 4.55
print(bbinaria_rec(lista, e))

# %% El archivo hojas_ISO.py del Ejercicio 11.13.
from hojas_ISO import medidas_hoja_A
print( "\n".join([f'A{N}. {medidas_hoja_A(N)[0]} x {medidas_hoja_A(N)[1]}' for N in range(11)]))

# %% El archivo alquiler.py del Ejercicio 11.14.
from alquiler import alquiler
alquiler()