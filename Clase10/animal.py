# -*- coding: utf-8 -*-
"""
animal.py
Created on Wed Oct  7 14:00:00 2020
@author: mlopez
"""
import random

class Animal(object):
    creatura = []
    """docstring for Animal"""
    def __init__(self):
        # super(Animal, self).__init__()
        self.reproducciones_pendientes = 4
        self.edad = 0
        self.sexo = None # Posible mejora para que no se puedan reproducir dos del mismo sexo
        self.energia = self.energia_maxima
        self.es_reproductore = False
        self.creatura.append("")
        self.creacion = str(len(self.creatura))

    def pasar_un_ciclo(self):
        self.energia -= 1 # Se puede restar si no llega a comer
        self.edad += 1
        # Agregado: Ejercicio 10.19: Alcanzando la madurez
        if self.reproducciones_pendientes > 0 and self.edad > 1: #
            self.es_reproductore = True

    def en_vida(self):
        return (self.edad <= self.edad_maxima) and self.energia > 0

    def tiene_hambre(self):
        """Acá se puede poner comportamiento para que no tenga hambre todo el tiempo
        debería depender de la diferencia entre su nivel de energía y su energía máxima:"""
        # Agregado: Definí que solo tienen hambre si su energía actual es la mitad de su máxima
        return self.energia <= self.energia_maxima // 2

    def es_leon(self):
        return False

    def es_antilope(self):
        return False

    # Agregado
    def especie(self):
        if self.es_antilope():
            esp = "Antílope"
        elif self.es_leon():
            esp = "León"
        return esp

    def puede_reproducir(self):
        return self.es_reproductore

    def tener_cria(self):
        """Acá se puede poner comportamiento que sucede al tener cria para evitar que tengamás de una cria por ciclo, etc"""
        self.reproducciones_pendientes -= 1
        # Agregado
        self.es_reproductore = False

    def reproducirse(self, vecinos, lugares_libres):
        pos = None
        if vecinos:
            animal = random.choice(vecinos)
            if lugares_libres:
                # Agregado: Ejercicio 10.18: Acotando la reproducción
                if self.puede_reproducir() and animal.puede_reproducir():
                    animal.tener_cria()
                    self.tener_cria()
                    # print(f'{self.__repr__()} tuvo cria con {animal.__repr__()}')
                    pos = random.choice(lugares_libres)
        return pos

    def alimentarse(self, animales_vecinos = None):
        self.energia = self.energia_maxima
        return None

    def moverse(self, lugares_libres):
        pos = None
        if lugares_libres:
            pos = random.choice(lugares_libres)
        return pos

    def fila_str(self):
        return f"{self.edad:>3d}    {self.energia:>3d}/{self.energia_maxima:<3d}       {self.es_reproductore!s:<5}"

    def __format__(self):
        return self.__repr__()

    def __str__(self):
        return self.__repr__()


class Leon(Animal):
    """docstring for Leon"""
    def __init__(self):
        self.energia_maxima = 6
        self.edad_maxima = 10
        super(Leon, self).__init__()

    def es_leon(self):
        return True

    def alimentarse(self, animales_vecinos):
        # Se alimenta si puede e indica la posición del animal que se pudo comer
        pos = None
        if self.tiene_hambre(): # no está lleno
            presas_cercanas = [ (pos,animal) for (pos, animal) in animales_vecinos if animal.es_antilope() ]
            if presas_cercanas: # y hay presas cerca
                super(Leon, self).alimentarse()
                (pos, animal) = random.choice(presas_cercanas)
                # print(f'{self.__repr__()} se comió a {animal.__repr__()}')
        return pos

    # Agregado
    def reproducirse(self, vecinos, lugares_libres):
        pos = None
        # Solo se puede reproducir con alguien de su misma especie
        vecinos = [v for v in vecinos if v.es_leon()]
        pos = super(Leon, self).reproducirse(vecinos, lugares_libres)
        return pos

    def __repr__(self):
        return "L"
        return "L_{}".format(self.creacion)



class Antilope(Animal):
    """docstring for Antilope"""
    def __init__(self):
        self.energia_maxima = 10
        self.edad_maxima = 6
        super(Antilope, self).__init__()
        self.reproducciones_pendientes = 3

    def es_antilope(self):
        return True

    # Agregado
    def reproducirse(self, vecinos, lugares_libres):
        pos = None
        # Solo se puede reproducir con alguien de su misma especie
        vecinos = [v for v in vecinos if v.es_antilope()]
        pos = super(Antilope, self).reproducirse(vecinos, lugares_libres)
        return pos


    def __repr__(self):
        return "A"
        return "A_{}".format(self.creacion)

