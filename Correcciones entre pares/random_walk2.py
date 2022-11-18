#!/usr/bin/env python3
# randomwalk.py
# -*- coding: utf-8 -*-

#%% Ejercicio 7.12: Caminatas al azar o random walk es una formalización matemática de la trayectoria que resulta de hacer sucesivos pasos aleatorios

import numpy as np
import matplotlib.pyplot as plt
import sys

def randomwalk(largo):
    """
    Genera una caminata al azar de N pasos de largo.
    """
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum()

def caminatas(largo):
    """
    Devuelve en una gráfica la evolución de 12 caminatas al azar.
    """
    for _ in range(12):
        dato = randomwalk(largo)
        plt.plot(dato)
        
#    return(plt.show())

def mas_menos_alejada(largo):
    """
    Devuelve la caminata que más se alejo del origen y la que se mantuvo estable.
    """
    maximo = 0
     
    for i in range(12):
        dato = randomwalk(largo)
        maximo = max(abs(dato))
                
        if i == 0:
            max_caminata = maximo
            mas_alejada = dato
            min_caminata = maximo
            menos_alejada = dato
        elif maximo >= max_caminata:
            max_caminata = maximo
            mas_alejada = dato
        elif maximo <= min_caminata:
            min_caminata = maximo
            menos_alejada = dato         
        else:
            continue
        
    return(mas_alejada, menos_alejada)


def f_principal(N):
    """
    Devuelve en una gráfica única, 12 variaciones de caminata en las cuales
    se detalla que caminata se distanció más del origen y cual se mantuvo estable.
    """
    plt.figure(figsize=(8, 6), dpi=80)
    
    plt.subplot(2, 1, 1) # define la figura de arriba
    caminatas(N)
    plt.title("12 caminatas al azar")
    plt.xlim(0,N)
    plt.xticks([])
    plt.ylim(-1000,1000)
    plt.yticks([-500, 0, 500])
    
    plt.subplot(2, 2, 3) # define la primera de abajo
    plt.plot(mas_menos_alejada(N)[0])
    plt.title("La caminata que más se aleja")
    plt.xlim(0,N)
    plt.xticks([])
    plt.ylim(-1000,1000)
    plt.yticks([-500, 0, 500])
    
    plt.subplot(2, 2, 4) # define la segunda de abajo
    plt.plot(mas_menos_alejada(N)[1])
    plt.title("La caminata que menos se aleja")
    plt.xlim(0,N)
    plt.xticks([])
    plt.ylim(-1000,1000)
    plt.yticks([-500, 0, 500])
    #plt.xlabel("Tiempo")
    #plt.ylabel("Distancia al origen")
    #plt.title("Caminata al azar - Randomwalk")
    #plt.legend()
    
    plt.show()

if __name__ == '__main__':
    if len(sys.argv) != 1:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ')
    N = 100000
    print(f_principal(N))