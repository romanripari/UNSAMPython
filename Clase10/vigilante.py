'''
Autor: Román Ripari
'''
import os
import time

def vigilar(filename):
    f = open(filename)
    f.seek(0, os.SEEK_END)   # Mover el índice 0 posiciones desde el EOF
    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.5)     # Esperar un rato y
            continue            # vuelve al comienzo del while
        yield line              # Devuelve la línea leída

def ejercicio_10_6():
    '''Ejercicio 10.6: Uso de un generador para producir datos'''
    for line in vigilar('../Data/mercadolog.csv'):
        fields = line.split(',')
        nombre = fields[0].strip('"')
        precio = float(fields[1])
        volumen = int(fields[2])
        if volumen > 1000:
            print(f'{nombre:>10s} {precio:>10.2f} {volumen:>10d}')

def ejercicio_10_7():
    '''Ejercicio 10.7: Cambios de precio de un camión'''
    import informe_final
    camion = informe_final.leer_camion ('../Data/camion.csv')
    print(camion)
    for line in vigilar('../Data/mercadolog.csv'):  
        fields = line.split(',')
        nombre = fields[0].strip('"')
        precio = float(fields[1])
        volumen = int(fields[2])
        if nombre in camion:    
            print(f'{nombre:>10s} {precio:>10.2f} {volumen:>10d}')

if __name__ == '__main__':
    ejercicio_10_7()