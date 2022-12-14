
from scipy import signal # para procesar señales
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('../Data/OBS_SHN_SF-BA.csv',index_col=['Time'],parse_dates=True)
inicio = '2014-01'
fin = '2014-06'
alturas_sf = df[inicio:fin]['H_SF'].to_numpy()
alturas_ba = df[inicio:fin]['H_BA'].to_numpy()

def calcular_fft(y, freq_sampleo = 24.0):
    '''y debe ser un vector con números reales
    representando datos de una serie temporal.
    freq_sampleo está seteado para considerar 24 datos por unidad.
    Devuelve dos vectores, uno de frecuencias 
    y otro con la transformada propiamente.
    La transformada contiene los valores complejos
    que se corresponden con respectivas frecuencias.'''
    N = len(y)
    freq = np.fft.fftfreq(N, d = 1/freq_sampleo)[:N//2]
    tran = (np.fft.fft(y)/N)[:N//2]
    return freq, tran

freq_sf, fft_sf = calcular_fft(alturas_sf)
plt.plot(freq_sf, np.abs(fft_sf))
plt.xlabel("Frecuencia")
plt.ylabel("Potencia (energía)")
plt.show()
print(freq_sf[0])
print(np.abs(fft_sf[0]))
print(signal.find_peaks(np.abs(fft_sf), prominence = 8))
freq_sf[350]
plt.plot(freq_sf, np.abs(fft_sf))
plt.xlabel("Frecuencia")
plt.ylabel("Potencia (energía)")
plt.xlim(0,4)
plt.ylim(0,20)
# me quedo solo con el último pico
pico_sf = signal.find_peaks(np.abs(fft_sf), prominence = 8)[0][-1]
# es el pico a analizar, el de la onda de mareas
# marco ese pico con un circulito rojo
plt.scatter(freq_sf[pico_sf], np.abs(fft_sf)[pico_sf], facecolor = 'r')
plt.show()
ang_sf = np.angle(fft_sf)[pico_sf]
print(ang_sf)
print(ang_sf * 24 / (2 * np.pi * freq_sf[350]))

# Para Buenos Aires
freq_ba, fft_ba = calcular_fft(alturas_ba)
plt.plot(freq_ba, np.abs(fft_ba))
plt.xlabel("Frecuencia")
plt.ylabel("Potencia (energía)")
plt.xlim(0,4)
plt.ylim(0,20)
# me quedo solo con el último pico
pico_ba = signal.find_peaks(np.abs(fft_ba), prominence = 8)[0][-1]
#se grafican los picos como circulitos rojos
plt.scatter(freq_ba[pico_ba], np.abs(fft_ba)[pico_ba], facecolor='r')
plt.title("Espectro de Potencias Bs.As.")
plt.show()
np.abs(fft_ba[0])
print(signal.find_peaks(np.abs(fft_ba), prominence=8))
ang_ba = np.angle(fft_ba)[pico_ba]
print(ang_ba)
freq = freq_ba[pico_ba]
ang2h = 24 / (2*np.pi*freq)
ang_ba * ang2h
(ang_ba - ang_sf) * ang2h * 60

