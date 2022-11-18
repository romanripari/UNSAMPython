camion = [
    ('Pera', 100, 490.1),
    ('Naranja', 50, 91.3),
    ('Limon', 150, 83.44)
]


registros = []  # Empezamos con una lista vacía
registros.append(('Pera', 100, 490.10))
registros.append(('Naranja', 50, 91.3))

registros = []  # Empezamos con una lista vacía

with open('../Data/camion.csv', 'rt') as f:
    next(f) # Saltear el encabezado
    for line in f:
        row = line.split(',')
        registros.append((row[0], int(row[1]), float(row[2])))

print(registros)

precios = {
   'Pera': 513.25,
   'Limon': 87.22,
   'Naranja': 93.37,
   'Mandarina': 44.12
}

print(precios['Naranja'])

precios = {} # Empezamos con un diccionario vacío

# Agregamos elementos
precios['Pera'] = 513.25
precios['Limon'] = 87.22
precios['Naranja'] = 93.37

precios = {}  # Empezamos con un diccionario vacío

with open('../Data/precios.csv', 'rt') as f:
    for line in f:
        row = line.split(",")
        try:
            precios[row[0]] = float(row[1])
        except:
            pass

print(precios)

feriados = {
  (1, 1) : 'Año nuevo',
  (1, 5) : 'Día del trabajador',
  (13, 9) : "Día del programador",
}

print(feriados[(1, 5)])


citricos = { 'Naranja','Limon','Mandarina' }
# Alternativamente podemos escribirlo así:
citricos = set(['Naranja', 'Limon', 'Mandarina'])

print(citricos)
print('Naranja' in citricos)
print('Manzana' in citricos)

precios = {}
precios['Naranja'] = 92.45
precios['Mandarina'] = 45.12
print(precios)