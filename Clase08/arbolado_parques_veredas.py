#%%
import pandas as pd
import os
import seaborn as sns

def funcion(especie_parque, especie_vereda):
    directorio = '../Data'
    archivo_parques = 'arbolado-en-espacios-verdes.csv'
    fname_parques = os.path.join(directorio,archivo_parques)
    df_p = pd.read_csv(fname_parques)
    cols = ['altura_tot', 'diametro', 'nombre_cie']
    df_parques = df_p[cols].copy()
    especies_seleccionadas = [especie_parque]
    df_tipas_parques = df_parques[df_parques['nombre_cie'].isin(especies_seleccionadas)]
    df_tipas_parques= df_tipas_parques.rename(columns={'altura_tot': 'altura','nombre_cie':'nombre'})
    df_tipas_parques = df_tipas_parques.assign(ambiente='parque')


    archivo_veredas = 'arbolado-publico-lineal-2017-2018.csv'
    fname_veredas = os.path.join(directorio,archivo_veredas)
    df_v = pd.read_csv(fname_veredas)
    cols = ['altura_arbol', 'diametro_altura_pecho', 'nombre_cientifico']
    df_veredas = df_v[cols].copy()
    especies_seleccionadas = [especie_vereda]
    df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico'].isin(especies_seleccionadas)]
    df_tipas_veredas = df_tipas_veredas.rename(columns={'altura_arbol': 'altura','diametro_altura_pecho': 'diametro', 'nombre_cientifico':'nombre'})
    df_tipas_veredas = df_tipas_veredas.assign(ambiente='vereda')
    df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])

    return df_tipas

def run():
    df_tipas = funcion('Tipuana Tipu','Tipuana tipu')    
#    df_tipas = funcion('Jacarandá mimosifolia','Jacaranda mimosifolia')    
    df_tipas.boxplot('diametro', by = 'ambiente')
    df_tipas.boxplot('altura', by = 'ambiente', )

if __name__ == '__main__':
    run()