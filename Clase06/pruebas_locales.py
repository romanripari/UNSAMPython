#%%
import fileparse
precios = fileparse.parse_csv('../Data/precios.csv', types=[str,float], has_headers=False)
print(precios)

import informe_funciones
files = ['../Data/camion.csv', '../Data/camion2.csv']
for name in files:
    print(f'{name:-^43s}')
    informe_funciones.informe_camion(name, '../Data/precios.csv')
    print()

import costo_camion
print(costo_camion.costo_camion('../Data/camion.csv'))

import bbin
lista = [0,1,3,5,6,8]
print(bbin.insertar(lista, 4))
print(lista)