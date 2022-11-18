import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos=np.random.randint(-1,2,largo)    
    return pasos.cumsum()

def run():
    N = 100000
    plt.subplot(2, 1, 1)

    maxima = []
    minima = []
    # Iniciamos el alejamiento mayor como el mínimi alejamiento posible: 0
    alejamiento_mayor = -1
    # Iniciamos el alejamiento menor como el máximo alejamiento posible: N
    alejamiento_menor = N+1

    #Recorro las listas de caminatas
    for i in range(12):
        caminata = randomwalk(N)
        plt.plot(caminata, linewidth=1)
        alejamiento_actual = max(abs(caminata))
        # Si el máximo absoluto en esa lista es mayor al alejamiento mayor, 
        # identifico esa lista como más alejada
        if alejamiento_actual > alejamiento_mayor:
            alejamiento_mayor = alejamiento_actual
            maxima = caminata
        # Si el máximo absoluto en esa lista es menor al alejamiento menor,
        # identifico esa lista como menos alejada
        if alejamiento_actual < alejamiento_menor:
            alejamiento_menor = alejamiento_actual
            minima = caminata

    plt.title("12 Caminatas al azar")
    plt.ylim(-1000, 1000)
    plt.yticks([-500, 0, 500])
    plt.xticks([])

    plt.subplot(2, 2, 3)
    plt.title("La caminata que más se aleja")
    plt.ylim(-1000, 1000)
    plt.yticks([-500, 0, 500])
    plt.plot(maxima, linewidth=1)

    plt.subplot(2, 2, 4) 
    plt.title("La caminata que menos se aleja")
    plt.ylim(-1000, 1000)
    plt.yticks([-500, 0, 500])
    plt.xticks([])
    plt.plot(minima, linewidth=1)

    plt.show()

if __name__ == '__main__':
    run()