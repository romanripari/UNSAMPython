# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 13:41:39 2021

@author: Manjuanel
"""

#Ejercicio 11.13: Hojas ISO y recursión
funcion = 0
def medidas_hoja_A(N):
    global funcion
    funcion +=1
    if N == 0:
        return (841, 1189)
    ancho = medidas_hoja_A(N-1)[1]//2 #Dobla al medio la hoja
    largo = medidas_hoja_A(N-1)[0]  #Cuando doblas el ANCHO pasa a ser el LARGO
    return (ancho,largo)

# print("A0", medidas_hoja_A(0))
# print("A1", medidas_hoja_A(1))
# print("A2", medidas_hoja_A(2))
# print("A3", medidas_hoja_A(3))
# print("A4", medidas_hoja_A(4))
# print("A5", medidas_hoja_A(5))
# print("A6", medidas_hoja_A(6))
# print("A7", medidas_hoja_A(7))

def run():
    # One-Liner para ver en pantalla las medidas de las hojas de A10 a A0
    print("A7", medidas_hoja_A(7))
    # print( "\n".join([f'A{N}. {medidas_hoja_A(N)[0]} x {medidas_hoja_A(N)[1]}' for N in range(11)]))
    print(funcion)
if __name__ == '__main__':
    run()
