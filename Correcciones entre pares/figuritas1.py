# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 20:01:35 2021

@author: Kadyr Valdes
"""

import random
import numpy as np


def crear_album(figus_total):
    return np.zeros(figus_total)


def album_incompleto(album):
    return 0 in album


def comprar_figu(figus_total):
    figurita = random.randint(1, figus_total)
    return figurita

# EJERCICIO 5.13


def cuantas_figs(figus_total):
    cantidad_figuritas = 0
    album = crear_album(figus_total)
    while album_incompleto(album):
        cantidad_figuritas += 1
        album[comprar_figu(figus_total)-1] += 1
    return cantidad_figuritas

# EJERCICIO 5.14


def cant_promedio_de_figuras(figus_total, n_repeticiones):
    return np.mean([cuantas_figs(figus_total) for n in range(n_repeticiones)])

# EJERCICIO 5.15


def experimento_figus(n_repeticiones, figus_total):
    return np.mean([cuantas_figs(figus_total) for n in range(n_repeticiones)])


if __name__ == '__main__':
    #album = crear_album(10)
    # print(album_incompleto(album))
    # print(comprar_figu(10))
    # print(cuantas_figs(100))

    n_repeticiones = 100
    figus_total = 670

    print(cant_promedio_de_figuras(figus_total, n_repeticiones))
    print(experimento_figus(n_repeticiones, figus_total))
    #lista = [cuantas_figs(figus_total) for n in range(n_repeticiones)]
    # print(lista)
    # print(np.mean(lista))