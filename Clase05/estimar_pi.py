import random

def generar_punto():
    x = random.random()
    y = random.random()
    return x,y

def dentro_de_circulo(xy):
    x = xy[0]
    y = xy[1]
    return (x**2 + y**2) <= 1
    


N = 10000
G = sum([dentro_de_circulo(generar_punto()) for i in range(N)])
prob = G/N *4

print(f'Pi es más o menos: {prob:.6f}.')

