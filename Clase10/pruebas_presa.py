# %%
from collections import Counter
from mundo import Mundo
m = Mundo(6, 6, 5, 20, debug=False)
import time
lista_de_animales = []
ciclos = 20
for i in range(ciclos):
    m.pasar_un_ciclo()
    lista_de_animales.append(m.listaanimales())

for lista in lista_de_animales:
    leones_antilopes = {'Antílope':0, 'León':0}
    for ani in lista:
        leones_antilopes[ani] +=1
    print(leones_antilopes)

# print(lista_de_animales)
# print(len(lista_de_animales))

# %%
from animal import Leon, Antilope
L = Leon()
L.energia
#%%
L.edad
# %%
L.tiene_hambre()

#%%
L.es_leon()
#%%
L.es_antilope()
#%%
L.pasar_un_ciclo()
#%%
L.energia
#%%
L.edad
#%%
L.tiene_hambre()

# %%

A1 = Antilope()
A2 = Antilope()
A1.energia
#%%
A1.edad
#%%
A1.es_antilope()
# %%
A1.tiene_hambre()
# %%
A1.pasar_un_ciclo()
# %%
A1.tiene_hambre()
A1.energia
# %%
vecinos = [(1,A1),(2,A2)]
L.pasar_un_ciclo()
pos = L.alimentarse(vecinos)

print(pos) 
#%%
if pos:
    print(f'El león se come al antílope A{pos}')
else:
    print(f'El león no come')

# %%
from animal import Leon, Antilope
L = Leon()
L.energia
L.edad
L.es_leon()
L.es_antilope()
L.pasar_un_ciclo()
L.energia
L.edad
L.tiene_hambre()

A1 = Antilope()
A2 = Antilope()
A1.energia
A1.edad
A1.es_antilope()

# %%
vecinos = [(1,A1),(2,A2)]
pos = L.alimentarse(vecinos)
if pos:
    print(f'El león se come al antílope A{pos}')
else:
    print(f'El león no come')
# %%

M = Leon()
M.puede_reproducir()
M.pasar_un_ciclo()
M.puede_reproducir()
L = Leon()
L.pasar_un_ciclo()
L.puede_reproducir()
# %%
from animal import Leon, Antilope
M = Leon()
A1 = Antilope()
L = Leon()
# %%
print("M reproducir:", M.puede_reproducir())
print("L reproducir:", L.puede_reproducir())
print("A1 reproducir:", A1.puede_reproducir())
M.pasar_un_ciclo()
A1.pasar_un_ciclo()
L.pasar_un_ciclo()
# %%
vecinos = [A1]
lugares_libres = [4,5,6,7,8]
pos = M.reproducirse(vecinos, lugares_libres)
print(f'nace un nuevo leoncito en la posición {pos}')
# %%
M.puede_reproducir()
