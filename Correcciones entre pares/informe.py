# -*- coding: utf-8 -*-
# informe.py
"""
Created on Mon Aug 16 18:30:26 2021

@author: Fabiana


Ejercicio 2.18: Balances

Supongamos que los precios en camion.csv son los precios pagados al productor de frutas 
mientras que los precios en precios.csv son los precios de venta en el lugar de descarga del camión.

Ahora vamos calcular el balance del negocio:  programa informe.py 
(usando las funciones leer_camion() y leer_precios()) y completá el programa para que con los precios del camión
(Ejercicio 2.16) y los de venta en el negocio (Ejercicio 2.17) calcule lo que costó el camión, lo que se recaudó con la venta, 
y la diferencia. ¿Hubo ganancia o pérdida? El programa debe imprimir por pantalla un balance con estos datos.

Requiere:    archivo camion.dat   y   archivo precios.csv 

"""



import csv

# función de lectura de datos del camión, devuelve una lista de tuplas(str(fruta), int(cajones), float(precio)
def leer_camion(nombre_archivo):
  camion = []
  with open(nombre_archivo, 'rt') as f:
      rows = csv.reader(f)
      next(rows) #para evitar los encabezados al calcular e precio del camion
      for i,row in enumerate(rows):
      #se usa el strip para sacar caracteres como \n\t\r etc e igualmente se hace un tratamiento del error por si aparecen líneas vacias, 
      #se usa el enumerate para poder informar qué linea/s no se puede tomar en cuenta          
          row=row[0].strip().split(' ')
          try:
            lote = (row[0], int(row[1]), float(row[2]))
            camion.append(lote)
          except:
            print(i, 'línea no procesable archivo camion' )
            print('línea: ',row)

  return camion

# función de lectura de datos de preciós, devuelve un diccionario con nombre de fruta de keys y precio como value
def leer_precios(nombre_archivo):
  '''Lee el archivo de precios'''
  precios = {}  # Se inicia un diccionario vacío

  with open(nombre_archivo, 'rt') as f:
    #rows = csv.reader(f)
    #se usa el strip para sacar caracteres como \n\t\r etc e igualmente se hace un tratamiento del error por si aparecen líneas vacias, 
    #se usa el enumerate para poder informar qué linea/s no se puede tomar en cuenta
    for i, line in enumerate(f):
        row = line.strip().split(',')
        try:
          precios[row[0]] = float(row[1])
        except:
          print(i, 'línea no procesable archivo precios')
          print('línea: ',row)
  return(precios)

#Se llama a las funciones de lectura de los datos del camión y de precios
camion=(leer_camion('../Data/camion.csv'))
precios=(leer_precios('../Data/precios.csv'))

# Cálculo del costo del camión cantidad de (cajones * precio de costo)
costo_camion=0
linea=0
while linea < len(camion):
  costo_camion += camion[linea][1]*camion[linea][2]
  linea+=1

# cálculo del valor de venta del camión (cantidad de cajones * precio de venta)
valor_venta=0
linea=0
while linea < len(camion):
  valor_venta += precios[camion[linea][0]]*camion[linea][1]
  linea+=1

balance= valor_venta - costo_camion

print('\n'f'Costo:    ${costo_camion:10.2f}')
print(f'Ingreso:  ${valor_venta:10.2f}')
print(f'Saldo:    ${balance:10.2f}')


"""Test
30 línea no procesable archivo precios
línea:  ['']

Costo:    $  47671.15
Ingreso:  $  62986.10
Saldo:    $  15314.95
"""