import numpy as np
import matplotlib.pyplot as plt


def ajuste_lineal_simple(x,y):
    a = sum(((x - x.mean())*(y-y.mean()))) / sum(((x-x.mean())**2))
    b = y.mean() - a*x.mean()
    return a, b

def alquiler():
    superficie = np.array([150.0, 120.0, 170.0, 80.0])
    alquiler = np.array([35.0, 29.6, 37.4, 21.0])
    minx = 0
    maxx = max(superficie)
    a, b = ajuste_lineal_simple(superficie, alquiler)
    grilla_x = np.linspace(start = minx, stop = maxx, num = 1000)
    grilla_y = grilla_x*a + b
    g = plt.scatter(x = superficie, y = alquiler)
    plt.title('precio_alquiler ~ superficie')
    plt.plot(grilla_x, grilla_y, c = 'green')
    plt.xlabel('Superficie en m2')
    plt.ylabel('Alquiler en miles de pesos')
    plt.legend()
    errores = alquiler - (a*superficie + b)
    print(errores)
    print("ECM:", (errores**2).mean())

if __name__ == '__main__':
    alquiler()