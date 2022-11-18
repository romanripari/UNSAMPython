from pprint import pprint


a = 'Hello'               # String o cadena
b = [1, 4, 5]             # Lista
c = ('Pera', 100, 490.1)  # Tupla
# Orden indexado
print(a[0]      )                # 'H'
print(b[-1]    )                 # 5
print(c[1]    )                  # 100

# Longitud de secuencias
print(len(a) )                   # 5
print(len(b))                    # 3
print(len(c))                    # 3

# Rebanadas 

a = [0,1,2,3,4,5,6,7,8]

print(a[2:5])    # [2,3,4]
print(a[-5:])    # [4,5,6,7,8]
print(a[:3])     # [0,1,2]

a = [0,1,2,3,4,5,6,7,8]
a[2:4] = [10,11,12, 25]       # [0,1,10,11,12,4,5,6,7,8]
print(a)
#%%
points = [
  (1, 4),(10, 40),(23, 14),(5, 6),(7, 8)
]
for x, y in points:
    print(x, y)
#%%
columnas = ['nombre', 'cajones', 'precio', "otro"]
valores = ['Pera', 100, 490.1 ]
d = dict(zip(columnas, valores))
print(d)
pares = zip(columnas, valores)
for columna, valor in pares:
    print(columna, valor)
    


precios = {
        'Pera' : 490.1,
        'Lima' : 23.45,
        'Naranja' : 91.1,
        'Mandarina' : 34.23,
        'Pera2' : 490.1,
        'Lima2' : 23.45,
        'Naranja2' : 91.1,
        'Mandarina2' : 34.23,
        'Pera3' : 490.1,
        'Lima3' : 23.45,
        'Naranja3' : 91.1,
        'Mandarina3' : 34.23
    }
print(precios.items())
lista_precios = list(zip(precios.values(),precios.keys()))
print(lista_precios)
print(min(lista_precios))
print(max(lista_precios))
pprint(sorted(lista_precios))
print(sorted(lista_precios))

#%%
a = [1, 2, 3, 4]
b = ['w', 'x', 'y', 'z']
c = [0.2, 0.4, 0.6, 0.8]
print(list(zip(a, b, c)))

# %%
