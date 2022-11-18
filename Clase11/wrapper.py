# %%
def promediar(lista):
    """Devuelve el promedio de los elementos de una lista de números."""

    def promediar_aux(lista):
        suma = lista[0]
        cantidad = 1    
        if len(lista) > 1:
            suma_resto, cantidad_resto = promediar_aux(lista[1:])
            suma += suma_resto
            cantidad += cantidad_resto
        return suma, cantidad

    suma, cantidad = promediar_aux(lista)
    return suma / cantidad

def inutil(n):
    return inutil(n - 1)

inutil(10)
# %%
