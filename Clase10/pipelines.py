# %%
from vigilante import vigilar
import csv
def filematch(lines, substr):
    for line in lines:
        if substr in line:
            yield line
lines = vigilar('../Data/mercadolog.csv')
#%%
# Ejercicio 10.8: Configuremos un pipeline simple

naranjas = filematch(lines, 'Naranja')
for line in naranjas:
    print(line) 
#%%
# Ejercicio 10.9: Un pipeline más en serio

rows = csv.reader(lines)
for row in rows:
    print(row)

