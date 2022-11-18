# *********************************************
'''
Clase Experimentos.

Utilizando una instancia de Experimentos creé dos funciones:

1) multiples_simulaciones():
    Realiza un Experimento y arroja conclusiones luego de realizar múltiples simulaciones

2) imprimir_tableros():
    Realiza un Experimento con una simulación, e imprime en consola una vez por segundo el status de tablero.

Ambas funciones se ejecutan desde if __name__ == '__main__'
'''
# *********************************************
import time
import os
from mundo import Mundo

# *********************************************

class Experimentos:
    def __init__(self,columnas = 12,filas = 6,n_leones = 4,n_antilopes = 25,
                ciclos = 20, simulaciones = 1000, imprime_tableros = False):
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
        return f'{self.extinguidos()} de {self.simulaciones} simulaciones terminaron con una especie extinta\n{"*"*15}'\
            f'\nEn {self.antilopes_extinguidos()} se extinguieron los antílopes y en {self.leones_extinguidos()} se extinguieron los leones'\
            f'\nEn {self.todos_extintos()} se extinguieron ambas especies\n{"*"*15}'

    def __str__(self):
        return f'Columnas: {self.columnas}, Filas: {self.filas}, n_leones: {self.n_leones}, n_antilopes: {self.n_antilopes}, ciclos: {self.ciclos}, simulaciones: {self.simulaciones}'

    def __repr__(self):
        return f'Experimentos({self.__str__()})'

def multiples_simulaciones():
    '''Crea un experimento e imprime las conclusiones'''
    columnas = 12
    filas = 6
    n_leones = 5
    n_antilopes = 25
    ciclos = 20
    simulaciones = 50
    ensayos = Experimentos(columnas, filas, n_leones, n_antilopes, ciclos, simulaciones)
    print(ensayos)
    print(ensayos.print_maximos())
    print(ensayos.print_promedios())
    print(ensayos.print_al_menos_uno())
    print(ensayos.print_extinguidos())

def imprimir_tableros():
    '''Crea un experimento con UNA simulación y muestra en pantalla la evolución del tablero'''
    columnas = 12
    filas = 8
    n_leones = 4
    n_antilopes = 15
    ciclos = 20
    simulaciones = 1
    ensayos = Experimentos(columnas, filas, n_leones, n_antilopes, ciclos,simulaciones, True)
    
if __name__ == '__main__':
    # multiples_simulaciones()
    imprimir_tableros()