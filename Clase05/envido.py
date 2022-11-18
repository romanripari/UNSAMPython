
import random
from collections import Counter

def es_envido(tres_cartas, pts):
    envido = False
    palos =[]
    tres_cartas.sort()
    for n in tres_cartas:
        palos.append(n[1])

    if len(set(palos)) < 3:
        palo, cantidad = Counter(palos).most_common()[0]
        ptos_env = 20
        cartas = 0
        for n in tres_cartas:
            if n[1] == palo and  n[0] <= 7 and cartas < 2:
                ptos_env += n[0]
                cartas += 1
        if ptos_env == pts:
            envido = True

    return envido

def quiero_sacar(pts):

    valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
    palos = ['oro', 'copa', 'espada', 'basto']
    naipes = [(valor,palo) for valor in valores for palo in palos]

    N = 10000
    G = sum([es_envido(random.sample(naipes,k=3), pts) for i in range(N)])
    prob = G/N

    print(f'Probabilidad de sacar {pts}: {prob:.6f}.')

def run():
    puntos = [20, 21, 22, 23, 24, 25, 26 ,27 ,28 ,29 ,30, 30, 31 ,32 ,33]
    for p in puntos:
        quiero_sacar(p)

if __name__ == "__main__":
    run()
