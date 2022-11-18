valor = 10
s = []
n = 0
d = {}


a = valor         # Asignación a una variable
s.append(valor)   # Agregar a una lista
s[n] = valor      # Asignación a una lista
d['key'] = valor  # Agregar a una diccionario

a = [2,2,[100,101],4]
b = a 
a[2].append(102)
print(b[1] is a[1])
print(b[2] is a[2])

# shallow copy (copia pero comparte elementos internos):
a = [2,2,[100,101],4]
b = list(a)
a[2].append(102)
print(b[1] is a[1])
print(b[2] is a[2])

import copy
# deep copy (lo copia, pero no lo comparte):
a = [2,3,[100,101],4]
b = copy.deepcopy(a)
a[2].append(102)
print(b[1] is a[1])
print(b[2] is a[2])
print(b[2])


import math
items = [abs, math, ValueError ]
print(items)