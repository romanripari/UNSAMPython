# %%
# *********************************************
'''
El archivo contiene las 3 clases: Animal, Tablero, Mundo.
Tablero quedó idéntica a la que dieron en la clase, pero Animal y Mundo tiene varios cambios.
Cuando edité algo en estas clases, le puse "Agregado"

Además, al final hay una clase que se llama Experimentos.

Utilizando una instancia de Experimentos creé dos funciones:

1) multiples_simulaciones():
    Realiza un Experimento y arroja conclusiones luego de realizar múltiples simulaciones
    Imprime un gráfico suavizado con las especies sobrevivintes

2) imprimir_tableros():
    Realiza un Experimento con una simulación, e imprime en consola una vez por segundo el status de tablero.

Ambas funciones se ejecutan desde if __name__ == '__main__'
'''
# *********************************************
import time
import os
import random
from random import choice
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter

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

# *********************************************

class Tablero(object):
    """docstring for Tablero"""
    # constructor
    def __init__(self, filas, columnas):
        super(Tablero, self).__init__()
        self.filas = filas
        self.columnas = columnas
        self.posiciones = {}
        self.n_posiciones_libres = self.filas * self.columnas

    # modificadores
    def ubicar(self,  pos, elem):
        if not self.ocupada(pos):
            self.n_posiciones_libres -= 1
        self.posiciones[pos] = elem
        return pos in self.posiciones

    def retirar(self, pos):
        self.n_posiciones_libres += 1
        return self.posiciones.pop(pos)

    def mover(self, p_origen, p_destino):
        self.ubicar(p_destino, self.retirar(p_origen))

    # getters
    def posicion(self, pos):
        return self.posiciones[pos]

    def ocupada(self,  pos):
        return pos in self.posiciones

    def libre(self,  pos):
        return pos not in self.posiciones

    def elementos(self):
        return list(self.posiciones.values())

    def n_filas(self):
        return self.filas

    def n_columnas(self):
        return self.columnas

    # modificadores complejos
    def ubicar_en_posicion_vacia(self, elem):
        if not self.hay_posiciones_libres():
            raise RuntimeError("Estás intentado agregar algo al tablero y está lleno")
        pos = choice(self.posiciones_libres())
        self.ubicar(pos, elem)


    # consultas
    def hay_posiciones_libres(self):
        return self.n_posiciones_libres > 0
        # return len(self.posiciones) <  self.filas * self.columnas

    def posiciones_ocupadas(self):
        res = []
        for f in range(self.filas):
            for c in range(self.columnas):
                if self.ocupada((f,c)):
                    res.append((f,c))
        return res

    def posiciones_libres(self):
        res = []
        for f in range(self.filas):
            for c in range(self.columnas):
                if self.libre((f,c)):
                    res.append((f,c))
        return res


    def posiciones_vecinas_libre(self, pos):
        res = self.posiciones_vecinas(pos)
        res = [ p for p in res if self.libre(p)]
        return res

    def posiciones_vecinas_con_ocupantes(self, pos):
        res = self.posiciones_vecinas(pos)
        res = [ (p, self.posicion(p)) for p in res if self.ocupada(p)]
        return res

    # auxiliar
    def posiciones_vecinas(self, pos):
        desp=[(-1, -1), (-1, 0), (-1, 1),(0, 1), (1, 1), (1, 0),(1, -1), (0, -1)]
        for i in range(len(desp)):
            f = (desp[i][0] + pos[0])
            c = (desp[i][1] + pos[1])
            desp[i] = (f, c)
        desp = [ (f,c) for f,c in desp if (0<=f and f<self.filas) and (0<=c and c<self.columnas) ]
        return desp

    # impresion
    def __repr__(self):
        res = ""
        for f in range(self.filas-1,-1,-1):
            for c in range(self.columnas):
                res += f"{(str(self.posiciones[(f,c)]) if (f,c) in self.posiciones else '-'):^3}"
            res += "\n"
        return res

# *********************************************

def print_debug(msg, print_flag=False):
    if print_flag:
        print(msg)

class Mundo(object):
    """docstring for Mundo"""

    def __init__(self, columnas, filas, n_leones, n_antilopes, debug=False):
        super(Mundo, self).__init__()

        self.debug = debug

        self.ciclo = 0
        self.tablero = Tablero(filas, columnas)
        self.llenar_mundo(n_leones, n_antilopes)

    def llenar_mundo(self, n_leones, n_antilopes):
        for _ in range(n_leones):
            if self.tablero.hay_posiciones_libres():
                print_debug("ubicando un leon", self.debug)
                self.tablero.ubicar_en_posicion_vacia(Leon())
        for _ in range(n_antilopes):
            if self.tablero.hay_posiciones_libres():
                print_debug("ubicando un Antilope", self.debug)
                self.tablero.ubicar_en_posicion_vacia(Antilope())

    def cant_leones(self):
        return sum([1 for x in self.tablero.elementos() if x.es_leon()])

    def cant_antilopes(self):
        return sum([1 for x in self.tablero.elementos() if x.es_antilope()])

    def etapa_movimiento(self):
        print_debug(f"Iniciando Movimiento en ciclo {self.ciclo}", self.debug)
        for p in self.tablero.posiciones_ocupadas():
            animal = self.tablero.posicion(p)

            posiciones_libres = self.tablero.posiciones_vecinas_libre(p)
            nueva_posicion = animal.moverse(posiciones_libres)
            if nueva_posicion:
                self.tablero.mover(p, nueva_posicion)

    def etapa_alimentacion(self):
        print_debug(f"Iniciando Alimentación en ciclo {self.ciclo}", self.debug)
        for p in self.tablero.posiciones_ocupadas():
            animal = self.tablero.posicion(p)
            animales_cercanos = self.tablero.posiciones_vecinas_con_ocupantes(p)
            desplazo = animal.alimentarse(animales_cercanos)
            if desplazo:
                # Agregado. Si el que comió fue León, quitamos al animal en desplazo
                # Alguien más deberá ocuparse de retirarlo del mundo
                if animal.es_leon():
                    self.tablero.retirar(desplazo)
                self.tablero.ubicar(desplazo, self.tablero.retirar(p))

    # Agregado. Ejercicio 10.17: Etapa de reproducción
    def etapa_reproduccion(self):
        print_debug(f"Iniciando Reproducción en ciclo {self.ciclo}", self.debug)
        for p in self.tablero.posiciones_ocupadas():
            animal = self.tablero.posicion(p)
            animales_cercanos = self.tablero.posiciones_vecinas_con_ocupantes(p)
            vecinos = [ v for _,v in animales_cercanos]
            lugares_libres = self.tablero.posiciones_libres()
            pos = animal.reproducirse(vecinos, lugares_libres)
            if pos:
                if animal.es_antilope():
                    self.tablero.ubicar_en_posicion_vacia(Antilope())
                elif animal.es_leon():
                    self.tablero.ubicar_en_posicion_vacia(Leon())

    def cerrar_un_ciclo(self):
        print_debug(f"Concluyendo ciclo {self.ciclo}", self.debug)
        for p in self.tablero.posiciones_ocupadas():
            animal = self.tablero.posicion(p)
            animal.pasar_un_ciclo() #envejecer, consumir alimento
            if not animal.en_vida():
                self.tablero.retirar(p)
        self.ciclo += 1

    def pasar_un_ciclo(self):
        self.etapa_movimiento()
        self.etapa_alimentacion()
        self.etapa_reproduccion()
        self.cerrar_un_ciclo()

    def __repr__(self):
        res = str(self.tablero)
        res += f"\nEstamos en la ciclo {self.ciclo}"
        res += f"\nCon {self.cant_leones()} Leones, y {self.cant_antilopes()} Antilopes."
        if False:
            res += '\nEspecie   Posicion   años  energia   puede_reproduc\n'
            for p in self.tablero.posiciones_ocupadas():
                animal = self.tablero.posicion(p)
                res += f'{"Leon    " if animal.es_leon() else "Antilope"} {str(p):^10s} {animal.fila_str()}\n'

        return res

    def __str__(self):
        return self.__repr__()

    def listaanimales(self):
        res = []
        for p in self.tablero.posiciones_ocupadas():
            animal = self.tablero.posicion(p)
            res.append(animal.especie())

        return res

# *********************************************

class Experimentos:
    def __init__(self,columnas = 12,filas = 6,n_leones = 4,n_antilopes = 25,
                ciclos = 20, simulaciones = 100, imprime_tableros = False):
        '''Se crea un experimento con todos los parámetros enviados y se ejecutan las simulaciones'''
        self.columnas = columnas
        self.filas = filas
        self.n_leones = n_leones
        self.n_antilopes = n_antilopes
        self.ciclos = ciclos
        self.simulaciones = simulaciones
        self.imprime_tableros = imprime_tableros
        self.ejecuta_simulaciones()
    
    def crea_mundo(self):
        '''Crea un mundo para cada simulación'''
        self.mundo = Mundo(self.columnas, self.filas, self.n_leones, self.n_antilopes)
    
    def simula_ciclos(self):
        '''Simula los ciclos dentro de una simulación y retorna una tupla
            con los antílopes y leones sobrevivientes al final de los ciclos'''
        self.crea_mundo()
        for i in range(self.ciclos):
            '''Si estamos en la simulación de imprimir tablero, lo hace en la consola'''
            if self.imprime_tableros:
                os.system("cls")
                print("Ciclo:", i+1)
                print(self.mundo.tablero)
                print("*" * 20)
                leones = (len([ elem for elem in self.mundo.tablero.elementos() if elem.es_leon()]))
                antilopes = (len([ elem for elem in self.mundo.tablero.elementos() if elem.es_antilope()]))
                print(f'Leones: {leones}. Antílopes: {antilopes}')
                time.sleep(0.5)
            self.mundo.pasar_un_ciclo()
        lista_de_animales = self.mundo.listaanimales()
        leones_antilopes = {'Antílope':0, 'León':0}
        for ani in lista_de_animales:
            leones_antilopes[ani] +=1
        return tuple(leones_antilopes.values())  # tupla(antilopes sobrevivientes, leones sobrevivientes)  
    
    def ejecuta_simulaciones(self):
        '''Para cada simulación, llama a simula_ciclos y guarda los resultados en tupla en una lista'''
        self.finales = []
        for _ in range(self.simulaciones):
            self.finales.append(self.simula_ciclos())
        return self.finales #lista[tuplas(antilopes sobrevivientes, leones sobrevivientes)]
    
    def obtiene_finales(self):
        '''Retorna la lista de tuplas generadas en ejecuta_simulaciones()'''
        return self.finales
    
    def obtiene_antilopes(self):
        '''Retorna una lista de Antílopes sobrevivientes al final de las simulaciones'''
        antilopes = []
        for f in self.obtiene_finales():
            antilopes.append(f[0])
        return antilopes 
    
    def obtiene_leones(self):
        '''Retorna una lista de Leones sobrevivientes al final de las simulaciones'''
        leones = []
        for f in self.obtiene_finales():
            leones.append(f[1])
        return leones 
    
    def promedio_antilopes(self):
        '''Promedio de Antílopes sobrevivientes en todas las simulaciones'''
        return sum(self.obtiene_antilopes()) / len(self.obtiene_antilopes())
    
    def promedio_leones(self):
        '''Promedio de Leones sobrevivientes en todas las simulaciones'''
        return sum(self.obtiene_leones()) / len(self.obtiene_leones())
    
    def al_menos_un_antilope(self):
        '''Cantidad de simulaciones con al menos un Antílope sobrevivientes'''
        return len([_ for _ in self.obtiene_antilopes() if _ > 0])
    
    def antilopes_extinguidos(self):
        '''Cantidad de simulaciones con Antílopes extinguidos'''
        return len([_ for _ in self.obtiene_antilopes() if _ == 0])
    
    def al_menos_un_leon(self):
        '''Cantidad de simulaciones con al menos un León sobrevivientes'''
        return len([_ for _ in self.obtiene_leones() if _ > 0])
    
    def leones_extinguidos(self):
        '''Cantidad de simulaciones con Leones extinguidos'''
        return len([_ for _ in self.obtiene_leones() if _ == 0])
    
    def extinguidos(self):
        '''Cantidad de simulaciones con Leones O Antílopes extinguidos'''
        return len([(a,l) for a,l in self.obtiene_finales() if a == 0 or l == 0])
    
    def todos_extintos(self):
        '''Cantidad de simulaciones con Leones Y Antílopes extinguidos'''
        return len([(a,l) for a,l in self.obtiene_finales() if a == 0 and l == 0])
    
    def print_titular(self):
        '''Retorna titular'''
        return f'Resultados para {self.simulaciones} simulaciones\n{"*"*15}'
    
    def print_maximos(self):
        '''Retorna máximos sobrevivientes para cada especie'''
        return ''
        return f'Máximo de Antílopes sobrevivientes: {max(self.obtiene_antilopes())}\n'\
        f'Máximo de Leones sobrevivientes: {max(self.obtiene_leones())}\n{"*"*15}'
    
    def print_promedios(self):
        '''Retorna promedio de sobrevivientes para cada especie'''
        return f'Promedio de Antílopes sobrevivientes: {self.promedio_antilopes()}\n'\
        f'Promedio de Leones sobrevivientes: {self.promedio_leones()}\n{"*"*15}'
    
    def print_al_menos_uno(self):
        '''Retorna simulaciones con sobrevivientes para cada especie'''
        return f'Simulaciones con al menos un Antílope sobreviviente: {self.al_menos_un_antilope()}\n'\
        f'Simulaciones con al menos un León sobreviviente: {self.al_menos_un_leon()}\n{"*"*15}'
    
    def print_extinguidos(self):
        '''Retorna simulaciones con las especies extintas para cada especie'''
        return f'{self.extinguidos()} de {self.simulaciones} simulaciones terminaron con una especie extinta'\
            f'\nEn {self.antilopes_extinguidos()} se extinguieron los antílopes y en {self.leones_extinguidos()} se extinguieron los leones'\
            f'\nEn {self.todos_extintos()} se extinguieron ambas especies\n{"*"*15}'

    def __str__(self):
        return f'Columnas: {self.columnas}, Filas: {self.filas}, n_leones: {self.n_leones}, n_antilopes: {self.n_antilopes}, ciclos: {self.ciclos}, simulaciones: {self.simulaciones}'

    def __repr__(self):
        return f'Experimentos({self.__str__()})'

def multiples_simulaciones():
    '''Crea un experimento e imprime las conclusiones'''
    columnas = 12
    filas = 12
    n_leones = 7
    n_antilopes = 50
    ciclos = 20
    simulaciones = 50
    ensayos = Experimentos(columnas, filas, n_leones, n_antilopes, ciclos, simulaciones)

    antilopes = ensayos.obtiene_antilopes()
    leones = ensayos.obtiene_leones()
   
    valores = [antilopes, leones]
    df_walk_suav = pd.DataFrame(valores)
    df_walk_suav = df_walk_suav.rolling(1, min_periods = 1).mean().T
    df_walk_suav = pd.DataFrame(df_walk_suav)
    df_walk_suav.plot()

    print(ensayos)
    print(ensayos.print_maximos())
    print(ensayos.print_promedios())
    print(ensayos.print_al_menos_uno())
    print(ensayos.print_extinguidos())

def imprimir_tableros():
    '''Crea un experimento con UNA simulación y muestra en pantalla la evolución del tablero'''
    columnas = 12
    filas = 12
    n_leones = 7
    n_antilopes = 30
    ciclos = 20
    simulaciones = 1
    ensayos = Experimentos(columnas, filas, n_leones, n_antilopes, ciclos,simulaciones, True)
    
if __name__ == '__main__':
    
    # imprimir_tableros()
    multiples_simulaciones()
# %%
