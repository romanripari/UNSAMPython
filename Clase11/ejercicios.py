# %%
# Ejercicio 11.2: Números triangulares
def triangular(n):
    if n == 1:
        return 1
    return n + triangular(n-1)

triangular(50)
# %%
# Ejercicio 11.3: Dígitos
def cant_digitos(n):
    # decena = n/10
    if n/10 < 1:
        return 1
    return 1 + cant_digitos(n/10)

cant_digitos(273245.123)
# %%
# Ejercicio 11.4: Potencias 
# def es_potencia(n, b):
    
#     def es_potencia_aux(n, b, pot):
#         if b ** pot == n:
#             return True
#         if b ** pot > n:
#             return False
#         return es_potencia_aux(n, b, pot+1)

#     return es_potencia_aux(n,b,0)

def es_potencia(n, b):
    if n == 1:
        return True
    if b == 1:
        return False
    if n % b == 0:
        return es_potencia(n//b,b)
    else:
        return False


print(es_potencia(8, 2))
print(es_potencia(8, 1))
# print(es_potencia(64, 4))
# print(es_potencia(70, 10))
# print(es_potencia(1, 2))
# print(es_potencia(1, 2))
# print(es_potencia(1024, 2))

# %%
# Ejercicio 11.5: Subcadenas 
def posiciones(a, b):
    lista = []
    
    def posiciones_aux(a,b,i): 
        if len(a) == 0:
            return None
        if a[:len(b)] == b:
            lista.append(i)
        return posiciones_aux(a[len(b)-1:],b,i+1)

    posiciones_aux(a,b,0)
    return lista

# def posiciones(a,b):
#     if len(b) > len(a):
#         return []
#     return posiciones(a[:-1], b)   + (a[ -len(b):] == b) * [len(a) - len(b)] 

print(posiciones('Un tete a tete con Tete', 'te'))
# %%
# Ejercicio 11.6: Paridad
# Palabras:
def par(n):
    if n == 0:
        return "Par"
    if n == 1:
        return "Impar"
    return impar(n-2)
def impar(n):
    if n == 0:
        return "Par"
    if n == 1:
        return "Impar"
    return par(n-2)

# True / False:
def par(n):
    if n == 1:
        return False
    return impar(n-1)
def impar(n):
    if n == 1:
        return True
    return par(n-1)

print(par(1))   # False
print(par(3))   # False
print(impar(3)) # True
print(par(4))   # True
print(impar(4)) # False
print(par(100)) # True


# %%
# Ejercicio 11.7: Máximo
def maximo(lista):
    if not lista:
        return 

    lista_aux = lista.copy()
    def maximo_aux(lista_aux, valor):
        if not lista_aux:
            return valor
        primero = lista_aux.pop(0)
        if valor < primero:
            valor = primero
        return maximo_aux(lista_aux, valor)

    valor = lista_aux[0]
    return maximo_aux(lista_aux,valor)

print(maximo([7,40]))
# maximo([0,1,-7,3,-4,1,-12,3])
# %% 
# Ejercicio 11.8: Replicar 
def replicar(lista, n):

    def replicar_aux(n, lista, replicada=[]):
        # Si la longitud de la lista es 0, devuelve la lista replicada como está
        if len(lista) == 0:
            return replicada
        for _ in range(n):
            replicada.append(lista[0])
        # replicada.append([lista[0] for _ in range(n)])
        return replicar_aux(n, lista[1:], replicada)

    return replicar_aux(n, lista)

print(replicar([3,2], 4))
print(replicar([1,3,2], 2))
print(replicar([1], 3))
print(replicar([1,2], 5))
print(replicar([1,2], 1))

# %%
# Ejercicio 11.10: Combinatorios  MAL!
def combinaciones(lista, k):
    if k ==1:
        return lista
    else:
        lista_f = []
        lista_act = combinaciones(lista,k-1)
        for i in range(0, len(lista)):
            for x in range(0, len(lista_act)):
                lista_f.append(lista[i] + lista_act[x])
    return lista_f

print(combinaciones(['a', 'b', 'c'],2)) # -> aa ab ac ba bb bc ca cb cc
# %%
def combinaciones(lista, k):

    if k == 1:
        comb = lista
    else:
        comb_rec = combinaciones(lista, k-1)
        comb = [e + c for e in lista for c in comb_rec ]
    return comb

def combinaciones(lista, k):
    if k == 1: return lista
    return [e + c for e in lista for c in combinaciones(lista, k-1) ]

print(combinaciones('abc',2)) # -> aa ab ac ba bb bc ca cb cc
# %%
# True / False:
def par(n):
    return impar(n-1)
def impar(n):
    if n == 0:
        return False
    return par(n-1)

print(impar(4))   # False
