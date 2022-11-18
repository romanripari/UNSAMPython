#%%
#****** El archivo generala.py del Ejercicio 5.2.
import generala
N = 100000
prob = generala.prob_generala(N)
print(f'Podemos estimar la probabilidad de sacar generala en tres tiros en {prob:.6f}.')
# %%
#****** El archivo termometro.py del Ejercicio 5.8.
import termometro
tupla_maximos_minimos_etc = termometro.resumen_temp()
print(tupla_maximos_minimos_etc)
# %%
#****** El archivo plotear_temperaturas.py del Ejercicio 5.9.
import plotear_temperaturas
plotear_temperaturas.plotear_temperaturas()
# %%
#****** El archivo figuritas.py abarcando lo hecho con figuritas (al menos) hasta el Ejercicio 5.15.
import figuritas
n_repeticiones = 100
figus_total = 670
figus_paquete = 5

# print(figuritas.experimento_figus(n_repeticiones, figus_total) / figuritas.experimento_paquetes(n_repeticiones, figus_total, figus_paquete) )

#print(f'Un álbum de {figus_total} figuritas se llenó en promedio (probado {n_repeticiones} veces) comprando {figuritas.experimento_paquetes(n_repeticiones, figus_total, figus_paquete)} paquetes')
print(f'Un álbum de {figus_total} figuritas se llenó en promedio (probado {n_repeticiones} veces) comprando {figuritas.experimento_figus(n_repeticiones, figus_total)} figuritas')

# %%
