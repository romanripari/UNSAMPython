#%%
import seaborn as sns
import pandas as pd
import os

directorio = '../Data'
archivo = 'arbolado-en-espacios-verdes.csv'
fname = os.path.join(directorio,archivo)
df = pd.read_csv(fname)
# # # Con df.head() podés ver las primeras líneas de datos
# # print(df.head(2))
# # # Análogamente con df.tail(n) verás las últimas n líneas de datos.
# # print(df.tail(2) )
# # print(df.columns )
# # print(df.index)
# # print(df[['altura_tot', 'diametro', 'inclinacio']].describe())
# # print(len(df['nombre_com'].unique()))
# # print((df['nombre_com'] == 'Ombú').sum())
# # cant_ejemplares = df['nombre_com'].value_counts()

# # print(cant_ejemplares.head(10))

df_jacarandas = df[df['nombre_com'] == 'Jacarandá']
# # print(df_jacarandas)

cols = ['altura_tot', 'diametro', 'inclinacio']
df_jacarandas = df_jacarandas[cols]
# # print(df_jacarandas.tail())
# # print(df_jacarandas.describe())

# Para copiar la info y no solo usarla como vista:
df_jacarandas = df[df['nombre_com'] == 'Jacarandá'][cols].copy()
# print(df_jacarandas)
df_jacarandas.plot.scatter(x = 'diametro', y = 'altura_tot')
sns.scatterplot(data = df_jacarandas, x = 'diametro', y = 'altura_tot')

#%%

cant_ejemplares = df['nombre_com'].value_counts() 
print(cant_ejemplares.index)

print(df.loc[165])
print("*****************************")
print(df_jacarandas.iloc[0])
print("*****************************")

print(cant_ejemplares.loc['Eucalipto'])

print(cant_ejemplares.iloc[0:3])

'''
filas y columnas
'''
print(df_jacarandas.iloc[-5:,2])
# Selección de una columna
df_jacarandas_diam = df_jacarandas['diametro']
print(type(df_jacarandas))
print(type(df_jacarandas_diam))

# %%
import pandas as pd
pd.date_range('20200923', periods = 7)
pd.date_range('20200923 14:00', periods = 7)
pd.date_range('20200923 14:00', periods = 6, freq = 'H')


# %%

pd.Series([1, 2, 3, 4, 5, 6], index = pd.date_range('20200923 14:00', periods = 6, freq = 'H'))


# %%
import numpy as np
idx = pd.date_range('20200923 14:00', periods = 120, freq = 'min')
s1 = pd.Series(np.random.randint(-1,2,120), index = idx)
s2 = s1.cumsum()
#s2.plot()
w = 5 
s3 = s2.rolling(w).mean()
#s3.plot()
df_series_23 = pd.DataFrame([s2, s3]).T  # armo un dataframe con ambas series
df_series_23.plot()


# %%
horas = 8
idx = pd.date_range('20200923 14:00', periods = horas*60, freq = 'min')
nombres = ['Pedro', 'Santiago', 'Juan', 'Andrés','Bartolomé','Tiago','Isca','Tadeo','Mateo','Felipe','Simón','Tomás']
df_walks = pd.DataFrame(np.random.randint(-1,2,[horas*60,12]).cumsum(axis=0), index = idx, columns = nombres)
#df_walks.plot()
w = 45
df_walk_suav = df_walks.rolling(w, min_periods = 1).mean() # datos suavizados
nsuav = ['S_' + n for n in nombres]
df_walk_suav.columns = nsuav # cambio el nombre de las columnas
                             # para los datos suavizados
df_walk_suav.plot()
df_walk_suav.to_csv('caminata_apostolica.csv')
