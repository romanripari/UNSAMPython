# %%
import pandas as pd
import os
import seaborn as sns


def run():
    directorio = '../Data'
    archivo = 'arbolado-publico-lineal-2017-2018.csv'
    fname = os.path.join(directorio,archivo)
    df = pd.read_csv(fname)
    cols_sel = ['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']
    df_lineal  = df[cols_sel]
# Imprimí las diez especies más frecuentes con sus respectivas cantidades.
    df_mas_frecuentes = df_lineal['nombre_cientifico'].value_counts()
    diez_mas_frecuentes = df_mas_frecuentes[0:10]
    print(diez_mas_frecuentes)
    especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']
    df_lineal_seleccion = df_lineal[df_lineal['nombre_cientifico'].isin(especies_seleccionadas)]
    print(df_lineal_seleccion)

# Ejercicio 8.8: Boxplots
    df_lineal_seleccion.boxplot('diametro_altura_pecho', by = 'nombre_cientifico')

    sns.pairplot(data = df_lineal_seleccion[cols_sel], hue = 'nombre_cientifico')

# Pregunta: ¿Por qué el ancho_acera no tiene lugar en el gráfico?
# RTA: porque no es numérico

if __name__ == '__main__':
    run()