
# import informe_final 
# informe_final.f_principal(['informe_final.py', '../Data/camion.csv', '../Data/precios.csv'])

# import costo_camion
# costo_camion.f_principal(['costo_camion.py', '../Data/camion.csv'])

# import fileparse
# # print(help(fileparse.parse_csv))
# lines = ['nombre,cajones,precio', 'Lima,100,34.23', 'Naranja,50,91.1', 'Mburucuya,75,45.1']
# camion = fileparse.parse_csv(lines, types=[str,int,float])
# print(camion)

# import gzip
# with gzip.open('../Data/camion.csv.gz', 'rt') as file:
#     camion = fileparse.parse_csv(file, types=[str,int,float])
# print(camion)

# camion = fileparse.parse_csv('../Data/camion.csv', types=[str,int,float])
# print(camion)

# import csv
# print(help(csv.reader))
# import fileparse
# print(help(fileparse.parse_csv))

import documentacion as do

print(help(do.valor_absoluto))
print(help(do.suma_pares))
print(help(do.veces))
print(help(do.collatz))

