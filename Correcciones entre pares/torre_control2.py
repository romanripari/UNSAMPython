
# %%!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 04:45:00 2021

@author: anahi
"""


class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola 
        y devuelve su valor. 
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve 
        True si la cola esta vacia, 
        False si no.'''
        return len(self.items) == 0

#cola_aterrizaje = Cola()
#cola_despegue = Cola()

    
class TorreDeControl:
    '''
    Modela una torre de control de un aeropuerto.
    Encola aviones para despegar y aviones para aterrizar.
    Los que aterrizan tienen prioridad para desencolar.
    '''
    def __init__(self):
       '''Crea dos colas vacías, una para despegue y otra para aterrizaje.
       La de aterrizaje tiene prioridad sobre la otra.'''
       self.cola_aterrizaje = Cola()
       self.cola_despegue = Cola()
       
       
    def nuevo_arribo(self, avion):
        '''Encola avion que llega, PRIORITARIO'''
        self.cola_aterrizaje.encolar(avion) 
        
        
    def nueva_partida(self, avion):
        '''Encola avion que sale'''
        self.cola_despegue.encolar(avion)
        
    
    def esta_vacia(self):
        despegue = self.cola_despegue.esta_vacia()
        aterrizaje = self.cola_aterrizaje.esta_vacia()
        
        return (despegue + aterrizaje)
        
    def asignar_pista(self):
        '''Asigna pista al primer avión que aterriza, mientras haya.
        Cuando no hay más para aterrizar, asigna pista a los que despegan.
        Cuando no hay más, da ValueError: 'No hay vuelos en espera'
        '''
              
        if not self.cola_aterrizaje.esta_vacia():
            print(f'El vuelo {self.cola_aterrizaje.items[0]} aterrizó con éxito.')
            self.cola_aterrizaje.desencolar()            
        elif not self.cola_despegue.esta_vacia():
            print(f'El vuelo {self.cola_despegue.items[0]} despegó con éxito.')
            self.cola_despegue.desencolar()
        else:
            print('No hay vuelos en espera.')
             
        return      
        
    def ver_estado(self):
        '''Muestra aviones esperando para aterrizar y para despegar'''
        pantalla = f'Vuelos esperando para aterrizar: '
        pantalla += ', '.join(self.cola_aterrizaje.items)
        pantalla += '\n'
        pantalla += f'Vuelos esperando para despegar: '
        pantalla += ', '.join(self.cola_despegue.items)
        pantalla += '\n'
        print(pantalla)


torre = TorreDeControl()
torre.nuevo_arribo('AR156')
torre.nueva_partida('KLM1267')
torre.nuevo_arribo('AR32')
torre2 = TorreDeControl()
torre2.nueva_partida("partida1")
torre2.nueva_partida("partida2")
torre2.ver_estado()
torre2.asignar_pista()
torre2.nueva_partida("partida4")
torre2.ver_estado()
# %%
