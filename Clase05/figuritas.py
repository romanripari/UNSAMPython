import matplotlib.pyplot as plt
import random
import numpy as np

def crear_album(figus_total):
    return np.zeros(figus_total)

def album_incompleto(A):
    # Al 100% 
    return 0 in A
    # Al 90%
#    return  (sum(A) / len(A)) < 0.9

def comprar_figu(figus_total):
    return random.randint(1,figus_total)

def cuantas_figus(figus_total):
    album = crear_album(figus_total)
    compradas = 0
    while album_incompleto(album):
        compradas +=1
        album[comprar_figu(figus_total) -1] = 1
    return compradas

def comprar_paquete(figus_total, figus_paquete):
    # Con posibles repetidos en el paquete
    # return random.choices(range(figus_total),k=figus_paquete)
    # Para que no haya repetidos en el paquete
    return random.sample(range(figus_total),k=figus_paquete)

def cuantos_paquetes(figus_total, figus_paquete):
    album = crear_album(figus_total)
    comprados = 0
    while album_incompleto(album):
        comprados +=1
        paquete = comprar_paquete(figus_total, figus_paquete)
        for p in paquete:
            album[p - 1] = 1
    return comprados
    
def experimento_paquetes(n_repeticiones, figus_total, figus_paquete):
    L = [cuantos_paquetes(figus_total, figus_paquete) for i in range(n_repeticiones)]
    return np.mean(L)


def experimento_figus(n_repeticiones, figus_total):
    return np.mean([cuantas_figus(figus_total) for i in range(n_repeticiones)])

def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()] = 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)        
    return historia_figus_pegadas


def run():
    # Figus
    # n_repeticiones = 100
    # figus_total = 860
    # print(f'Un álbum de {figus_total} figuritas se llenó en promedio (probado {n_repeticiones} veces) comprando {experimento_figus(n_repeticiones, figus_total)} figuritas')

    # Paquetes
    n_repeticiones = 100
    figus_total = 860
    figus_paquete = 5
    print(f'Un álbum de {figus_total} figuritas se llenó en promedio (probado {n_repeticiones} veces) comprando {experimento_paquetes(n_repeticiones, figus_total, figus_paquete)} paquetes')

    #gráficos:
    # figus_total = 670
    # figus_paquete = 5

    # plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
    # plt.xlabel("Cantidad de paquetes comprados.")
    # plt.ylabel("Cantidad de figuritas pegadas.")
    # plt.title("La curva de llenado se desacelera al final")
    # plt.show()


    # Ejercicio 5.20:

if __name__ == "__main__":
    run()
