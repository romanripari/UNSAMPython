#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 19:31:36 2021

@author: juan
"""
# %%
import pandas as pd
import os
import seaborn as sns

directorio = '../Data'

archivo = 'arbolado-en-espacios-verdes.csv'
fname = os.path.join(directorio,archivo)
df_parques = pd.read_csv(fname)
cols = ['altura_tot', 'diametro']
df_tipas_parques = df_parques[df_parques['nombre_cie'] == 'Tipuana Tipu'][cols].copy()

archivo2 = 'arbolado-publico-lineal-2017-2018.csv'
fname2 = os.path.join(directorio,archivo2)
df_veredas = pd.read_csv(fname2)
cols2 = ['altura_arbol', 'diametro_altura_pecho']
df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico'] == 'Tipuana tipu'][cols2].copy()
df_tipas_veredas = df_tipas_veredas.rename(columns={"altura_arbol": "altura_tot", "diametro_altura_pecho": "diametro"})

df_tipas_parques['ambiente'] = ['parque']*len(df_tipas_parques)
df_tipas_veredas['ambiente'] = ['vereda']*len(df_tipas_veredas)
df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])
df_tipas.boxplot('diametro',by = 'ambiente')
df_tipas.boxplot('altura_tot',by = 'ambiente')
# %%
