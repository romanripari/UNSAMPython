
import matplotlib.pyplot as plt
import numpy as np

def plotear_temperaturas():
    temperaturas = np.load('../Data/temperaturas.npy')
    plt.hist(temperaturas,bins=115)
    plt.show() #el show no hace falta en algunos entornos. A veces lo omitiremos.

def run():
    plotear_temperaturas()

if __name__ == "__main__":
    run()
