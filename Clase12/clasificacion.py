# %%
from sklearn.datasets import  load_iris
iris_dataset = load_iris()
# %%

print("Claves del diccionario iris_dataset:\n", iris_dataset.keys())
# %%
print("Target names:", iris_dataset['target_names'])

# %%
print("Feature names:\n", iris_dataset['feature_names'])

# %%
print("Type of data:", type(iris_dataset['data']))
# %%

print("Shape of data:", iris_dataset['data'].shape)
# %%
print("First five rows of data:\n", iris_dataset['data'][:5])
# %%
print("Type of target:", type(iris_dataset['target']))
# %%
print("Shape of target:", iris_dataset['target'].shape)


# %%
print("Target:\n", iris_dataset['target'])

# %%
import pandas as pd

# %%
iris_dataframe = pd.DataFrame(iris_dataset['data'], columns = iris_dataset.feature_names)
pd.plotting.scatter_matrix(iris_dataframe, c = iris_dataset['target'], figsize = (15, 15), marker = 'o', hist_kwds = {'bins': 20}, s = 60, alpha = 0.8)

# %% 1) Separar los datos en dos conjuntos: train y test.

from sklearn.datasets import  load_iris
iris_dataset = load_iris()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    iris_dataset['data'], iris_dataset['target'], random_state = 0)
# %%

print("X_train shape:", X_train)
# %% 
print("y_train shape:", y_train)
# %%
print("X_test shape:", X_test.shape)
print("y_test shape:", y_test.shape)
# %% 2) Definir un clasificador knn y entrenarlo con los datos de training.

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 1)
# %%
knn.fit(X_train, y_train)
# %% 3) Evaluar el clasificador con los datos de testing.
import numpy as np
X_new = np.array([[5, 2.9, 1, 0.2]])
print("X_new.shape:", X_new.shape)
# %%
import matplotlib.pyplot as plt
plt.scatter(X_train[:, 1], X_train[:, 3], c = y_train)
plt.scatter(X_new[:, 1], X_new[:, 3], c = 'red')
# %%
prediction = knn.predict(X_new)
print("Predicción:", prediction)
print("Nombre de la Especie Predicha:",
       iris_dataset['target_names'][prediction])
# %%
y_pred = knn.predict(X_test)
print("Predicciones para el conjunto de Test:\n", y_pred)
print("Etiquetas originales de este conjunto:\n", y_test)

# %%
print(y_pred == y_test)
print("Test set score: {:.2f}".format(np.mean(y_pred == y_test)))
print("Test set score: {:.2f}".format(knn.score(X_test, y_test)))
# %%

#%%
from sklearn.datasets import  load_iris
iris_dataset = load_iris()
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

#%%

knn = KNeighborsClassifier(n_neighbors = 1)
clf = DecisionTreeClassifier()
#%%

X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'])
knn.fit(X_train, y_train)
prom_knn = knn.score(X_test, y_test)

print("Test set score: {:.2f}".format(knn.score(X_test, y_test)))

clf.fit(X_train, y_train)
prom_clf = clf.score(X_test, y_test)

print("Test set score: {:.2f}".format(clf.score(X_test, y_test)))


