#solucion_de_errores.py
#Ejercicios de errores en el código
#%%
#Ejercicio 3.1. Función tiene_a()
#Comentario: Solo encontraba la A si era minúscula.
#    Además, el while cortaba en la primera letra (por el return)
#    Lo corregí pasando a minúscula la letra y sacando el return False fuera del while
#    A continuación va el código corregido
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i < n:
        if str(expresion[i]).lower() == 'a':
            return True
        i += 1
    return False

print("",
tiene_a('eee'),
tiene_a('UNSAM 2020'),
tiene_a('abracadabra'),
tiene_a('La novela 1984 de George Orwell')
)
#%%
#Ejercicio 3.2. Función tiene_a(), nuevamente
#Comentario: Había 3 errores. La falta de ":", un solo "=" cuando quería comparar y la palabra Falso 
#   Agregué los ":" después de la definición de la función, del while y del if.
#   Además, puse un doble == en lugar de uno solo.
#   Por último, cambié Falso por False

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

print("",
tiene_a('UNSAM 2020'),
tiene_a('La novela 1984 de George Orwell')
)

#%%
#Ejercicio 3.3. Función tiene_uno()
#Comentario: El error era que quiere aplicar funciones de STR a INT. 
#   Para solucionarlo, se convierte en STR la expresión entera con "expresion = str(expresion)"

def tiene_uno(expresion):
    expresion = str(expresion)
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


print("",
tiene_uno('UNSAM 2020'),
tiene_uno('La novela 1984 de George Orwell'),
tiene_uno(1984)
)
#%%
#Ejercicio 3.4. Función suma()
#Comentario: El error era que no tiene Return. 
#   Para solucionarlo, se agregó "Return c"
def suma(a,b):
    c = a + b
    return c

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")

# %%
#Ejercicio 3.4. Función suma()
#Comentario: El error era que el diccionario agregado era siempre el mismo.
#    Esto sucede porque dentro de la lista se agrega EL DICCIONARIO y no los valores 
#    que tenga en ese momento. Entonces, siempre que no se reinicie, 
#    va a estar dentro de la lista el último contenido que se carque a él. 

#    Para solucionarlo, se debe reiniciar el Diccionario cada vez que avance una fila, vaciándolo
#    con registro={} dentro del for

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
#    registro={}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            
            nuevo_registro={}

            nuevo_registro[encabezado[0]] = fila[0]
            nuevo_registro[encabezado[1]] = int(fila[1])
            nuevo_registro[encabezado[2]] = float(fila[2])
            camion.append(nuevo_registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)
