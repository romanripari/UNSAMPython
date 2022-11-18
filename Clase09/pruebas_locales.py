# # %%
# from Clase09.informe_final import leer_camion
# import lote
# a = lote.Lote('Pera', 100, 490.10)
# print(a.nombre)

# # %%
# b = lote.Lote('Manzana', 50, 122.34)
# c = lote.Lote('Naranja', 75, 91.75)
# b.cajones * b.precio
# # %%
# c.cajones * c.precio

# # %%
# lotes = [a, b, c]
# lotes
# # %%

# for c in lotes:
#     print(f'{c.nombre:>10s} {c.cajones:>10d} {c.precio:>10.2f}')
# # %%
# for c in lotes:
#     print(c.cajones)
# for c in lotes:
#     c.vender(13)
# for c in lotes:
#     print(c.cajones)

# # %%

# import fileparse
# with open('../Data/camion.csv') as lineas:
#     camion_dicts = fileparse.parse_csv(lineas, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
# camion = [lote.Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dicts]
# sum([c.costo() for c in camion])
# # %%
# import informe_final
# informe_final.leer_camion('../Data/camion.csv')
# # %%
# import costo_camion
# costo_camion.costo_camion('../Data/camion.csv')
# # %%
# import informe_final
# informe_final.informe_camion('../Data/camion.csv', '../Data/precios.csv')

# %%
import informe_final
informe_final.informe_camion('../Data/camion.csv', '../Data/precios.csv', fmt='csv')
# %%
from datetime import date
d = date(2020, 12, 21)
print(d)
d

# %%

class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    # Used with `repr()`
    def __repr__(self):
        return f'Punto({self.x}, {self.y})'
    
    def __add__(self, b):
      return Punto(self.x + b.x, self.y + b.y)

# %%
p = Punto(2,2)
print(p)
p
# %%
a = Punto(1,2)  
b = Punto(3,4)  
a + b
# %%
import lote

peras = lote.Lote('Pera', 100, 490.1)
peras
# %%
import informe_final
camion = informe_final.leer_camion('../Data/camion.csv')
camion
# %%

import lote
c = lote.Lote('Peras', 100, 490.1)
columnas = ['nombre', 'cajones']
for colname in columnas:
        print(colname, '=', getattr(c, colname))

# nombre = Peras
# cajones = 100
# %%
import informe_final
camion = informe_final.leer_camion('../Data/camion.csv')
from formato_tabla import crear_formateador, imprimir_tabla
formateador = crear_formateador('html')

imprimir_tabla(camion, ['nombre','cajones'], formateador)

# %%
imprimir_tabla(camion, ['nombre','cajones','precio'], formateador)
# %%
import torre_control
torre = torre_control.TorreDeControl()
torre.nuevo_arribo('AR156')
torre.nueva_partida('KLM1267')
torre.nuevo_arribo('AR32')
torre.ver_estado()
torre.asignar_pista()
torre.asignar_pista()
torre.asignar_pista()
torre.ver_estado()
torre.asignar_pista()
torre.asignar_pista()
# %%
import informe_final
informe_final.informe_camion('../Data/camion.csv', '../Data/precios.csv', fmt = 'txt')
# %%
from lote import Lote
peras = Lote('Pera', 100, 490.1)
peras
import informe_final
camion = informe_final.leer_camion('../Data/camion.csv')
camion
# %%
import informe_final
camion = informe_final.leer_camion('../Data/camion.csv')
from formato_tabla import crear_formateador, imprimir_tabla
formateador = crear_formateador('txt')
imprimir_tabla(camion, ['nombre','cajones'], formateador)
