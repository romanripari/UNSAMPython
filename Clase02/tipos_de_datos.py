import csv


f = open('./Data/camion.csv')
filas = csv.reader(f)
next(filas)

# Tuplas

fila = next(filas)
print(fila)
t = (fila[0], int(fila[1]), float(fila[2]))
cost = t[1] * t[2]
print(cost)
print(f'{cost:0.2f}')
t = (t[0], 75, t[2])
print(t)
nombre, cajones, precio = t
print(nombre)
print(cajones)
print(precio)

t = (nombre, 2*cajones, precio)
print(t)

# Diccionarios:

d = {
        'nombre' : fila[0],
        'cajones' : int(fila[1]),
        'precio'  : float(fila[2])
    }

print (d)
cost = d['cajones'] * d['precio']
print(cost)

d['cajones'] = 75
d['fecha'] = (14, 8, 2020)
d['cuenta'] = 12345

for k in d:
    print('k =', k)

for k in d:
    print(k, '=', d[k])

items = d.items()
print(items)
for k, v in d.items():
        print(k, '=', v)

print(list(d))
claves = d.keys()

nuevos_items = [('nombre', 'Manzanas'), ('cajones', 100), ('precio', 490.1), ('fecha', (13, 8, 2020))]
print(nuevos_items)
d = dict(nuevos_items)
print(d)