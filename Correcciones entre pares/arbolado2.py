# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 20:09:21 2021

@author: Javier
"""

# %% Ejercicio 8.9

import pandas as pd
from pprint import pprint
#  Abre los datasets a los que llamaremos df_parques y df_veredas.
df_parques = pd.read_csv('../Data/arbolado-en-espacios-verdes.csv')
df_veredas = pd.read_csv('../Data/arbolado-publico-lineal-2017-2018.csv')
# definimos las columnas a cambiar para la concatenación
cols_p = ['altura_tot', 'diametro'] # columnas de parques
cols_v = ['altura_arbol', 'diametro_altura_pecho'] # columnas de veredas
# copiamos de los df originales con las columnas seleccionadas
df_tipas_parques = df_parques[df_parques['nombre_cie'] =='Tipuana Tipu'][cols_p].copy()
df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico'] =='Tipuana tipu'][cols_v].copy()
# renombramos las columnas de veredas con los nombres de las columnas seleccionadas de parque
df_tipas_veredas = df_tipas_veredas.rename(columns={'altura_arbol':'altura_tot','diametro_altura_pecho':'diametro'})
# Agrega a cada dataframe (df_tipas_parques y df_tipas_veredas) una columna llamada 'ambiente'
df_tipas_veredas.insert(2,'ambiente','vereda')
df_tipas_parques.insert(2,"ambiente",'parque')
pprint(df_tipas_parques)
# concatena ambos datasets 
df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])
# Creá un boxplot para los diámetros de la tipas distinguiendo los ambientes
df_tipas.boxplot('diametro',by = 'ambiente',figsize=(8,5))
# Creá un boxplot para las alturas de la tipas distinguiendo los ambientes
df_tipas.boxplot('altura_tot',by = 'ambiente',figsize=(8,5))
# %%
