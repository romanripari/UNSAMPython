import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model

def AIC(k, ecm, num_params):
    '''Calcula el AIC de una regresión lineal múltiple de 'num_params' parámetros, ajustada sobre una muestra de 'k' elementos, y que da lugar a un error cuadrático medio 'ecm'.'''
    aic = k * np.log(ecm) + 2 * num_params
    return aic


k = 1
ecm = 201.194
num_params = 2
aic = AIC(k, ecm, num_params)
print('-------------------------')
print(f'Grado del polinomio: {k}')
print(f'Cantidad de parámetros: {num_params}')
print(f'ECM: {ecm}')
print(f'AIC: {aic}')
