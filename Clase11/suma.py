#%% 
mi_lista = [1,2,3,4,5]
def sumar(lista):
    if len(lista) == 0:
        return 0
    suma = lista[0] 
    return suma + sumar(lista[1:])

sumar(mi_lista)
# %%
def sumar(lista):
   """Devuelve la suma de los elementos en la lista."""
   res = 0
   if len(lista) != 0:
       res = lista[0] + sumar(lista[1:])
   return res
sumar(mi_lista)

# %%
def sumar(lista, suma = 0):
    """Devuelve la suma de los elementos en la lista."""
    res = suma
    if len(lista) != 0:
        res = sumar(lista[1:], lista[0] + suma)
    return res
sumar(mi_lista)
# %%

def sumar(lista):
    """Devuelve la suma de los elementos en la lista."""
    suma = 0
    while lista:
        lista, suma = lista[1:], lista[0] + suma
    return suma
sumar(mi_lista)

# %%
