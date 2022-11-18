# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 18:58:38 2021

@author: amene
"""


def propaga(lista):
    contador = 0
    encendido = False
    pro_lista = []
    for i, e in enumerate(lista):
        # Ya sea si el fosforo esta apagado o encendido añade al contador.
        if e == 0:
            contador += 1
        # Si el fosforo esta encendido activa la variable "encendido"
        elif e == 1:
            contador += 1
            encendido = True
        # Si encuentra un fosforo carbonizado agrega a la nueva lista tantos 
        #fosforos como diga el contador, encendidos o apagados segun diga la 
        #variable booleana. Luego se resetea encendido y el contador sale en 0
        #ademas se agrega el fosforo quemado.
        elif e == -1:
            while contador > 0:
                contador -= 1
                if encendido:
                    pro_lista.append(1)
                else:
                    pro_lista.append(0)
            pro_lista.append(-1)
            encendido = False
    #Una vez que se salio del bucle for, se agrean los fosforos contados que 
    #quedaron.
    while contador > 0:
        contador -= 1
        if encendido:
            pro_lista.append(1)
        else:
            pro_lista.append(0)
    return pro_lista


def main():
    lista = [0, 0, 0, -1, 1, 0, 0, 0, -1, 0, 1, 0, 0]
    print(lista)
    print(propaga(lista))
    lista = [0, 0, 0, 1, 0, 0]
    print(lista)
    print(propaga(lista))