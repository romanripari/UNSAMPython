# %% El archivo informe_final.py del Ejercicio 10.2.
import informe_final
informe_final.informe_camion('../Data/camion.csv', '../Data/precios.csv')

# %%

import costo_camion
costo_camion.costo_camion('../Data/camion.csv')
# %%
import informe_final
camion = informe_final.leer_camion('../Data/camion.csv')
#%%
camion
#%%
print(camion)
#%%
for c in camion:
    print(c)
#%%
print(camion.contar_cajones())
# %%
from vigilante import vigilar

for line in vigilar('../Data/mercadolog.csv'):
    print(line)
        
# %%
import informe_final
from vigilante import vigilar
from ticker import  parsear_datos
from ticker import  filtrar_datos

camion = informe_final.leer_camion('../Data/camion.csv')
rows = parsear_datos(vigilar('../Data/mercadolog.csv'))
rows = filtrar_datos(rows, camion)
for row in rows:
    print(row)

# %%
from ticker import ticker
ticker('../Data/camion.csv', '../Data/mercadolog.csv', 'csv')
# %%
import listar_imgs
listado = listar_imgs.archivos_png('../Data/ordenar')
for l in listado:
    print(l)

# %%
from animal import Leon, Antilope
L = Leon()

A1 = Antilope()
A2 = Antilope()
A1.energia
A1.edad
A1.es_antilope()
# %%
L.pasar_un_ciclo()
# %%
print(L.energia)
vecinos = [(1,A1),(2,A2)]
pos = L.alimentarse(vecinos)
if pos:
    print(f'El león se come al antílope A{pos}')
else:
    print(f'El león no come')
print(L.energia)

# %%
from animal import Leon, Antilope

M = Leon()
L = Leon()
print(M.puede_reproducir())
M.pasar_un_ciclo()
print(M.puede_reproducir())
vecinos = [L]
lugares_libres = [4,5,6,7,8]
print(L.puede_reproducir())
L.pasar_un_ciclo()
print(L.puede_reproducir())
# %%
pos = M.reproducirse(vecinos, lugares_libres)
print(f'nace un nuevo leoncito en la posición {pos}')
print(M.puede_reproducir())
M.pasar_un_ciclo()
print(M.puede_reproducir())

# %%
from mundo import Mundo
m = Mundo(12, 6, 5, 15, debug=False)
import time
for i in range(20):
    m.pasar_un_ciclo()
#    time.sleep(1)
    print(i +1)
    print(m.listaanimales())
#    print(m)

# %%
from ticker import ticker
ticker('../Data/camion.csv', '../Data/mercadolog.csv', 'txt')
# %%
