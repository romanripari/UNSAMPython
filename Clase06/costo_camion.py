import csv
import informe_funciones

def costo_camion(nombre_archivo):
    '''
    Obtengo el camión con la función informe_funciones.leer_camion y 
    calculo el costo de acuerdo a los cajones * los costos.
    '''
    camion = informe_funciones.leer_camion(nombre_archivo)
    costo = 0.0
    for fila in camion:
        try:
            ncajones = int(fila['cajones'])
            precio = float(fila['precio'])
            costo += ncajones * precio
        except ValueError:
            pass
    return costo

def run():
    costo = costo_camion('../Data/fecha_camion.csv')
    print(f'Costo total {costo}')

if __name__ == "__main__":
    run()