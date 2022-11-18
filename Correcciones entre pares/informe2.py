#Función del ejercicio 2.18

import csv

with open('camion.csv', 'wt') as f:
        f.write('nombre,cajones,precio\n"Lima",100,32.20\n"Naranja",50,91.10\n"Caqui",150,83.44\n"Mandarina",200,51.23\n"Durazno",95,40.37\n')

with open('precios.csv', 'wt') as g:
        g.write('nombre,cajones,precio\n"Lima",100,42.20\n"Naranja",50,94.10\n"Caqui",150,89.44\n"Mandarina",200,71.23\n"Durazno",95,60.37\n')

def costo_camion(nombre_archivo,nombre_archivo2):
  with open(nombre_archivo) as f:
    rows = csv.reader(f)
    headers = next(rows)
    sum1=0
    for line in f:
          sum1+= int(line.split(',')[1])*float(line.split(',')[2].rstrip('\n'))
    print("Costo total de el camion ,usando la funcion del 2.18: $" ,sum1)
  
  with open(nombre_archivo2) as g:
    rows1 = csv.reader(g)
    headers1 = next(rows1)
    sum2=0
    for line in g:
          sum2+= int(line.split(',')[1])*float(line.split(',')[2].rstrip('\n'))
    print("Precio del venta total de el camion ,usando la funcion del 2.18: $" ,sum2)
    
  
  if (sum2-sum1)>0:
      dif="(Hay ganancia +)"
  else:
      dif="(Hay perdida -)"

  print("Diferencia ,usando la funcion del 2.18: $", (sum2-sum1),dif)

costo_camion('camion.csv','precios.csv')