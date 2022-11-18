import csv
import informe_final

def costo_camion(nombre_archivo):
    '''
    Obtengo el camión con la función informe_funciones.leer_camion y 
    calculo el costo de acuerdo a los cajones * los costos.
    '''
    camion = informe_final.leer_camion(nombre_archivo)
    costo = 0.0
    for fila in camion:
        try:
            ncajones = int(fila['cajones'])
            precio = float(fila['precio'])
            costo += ncajones * precio
        except ValueError:
            pass
    return costo

def f_principal(parametros):
    if len(parametros) != 2:
        raise SystemExit(f'Uso adecuado: {parametros[0]} ' 'archivo_camion')
    costo = costo_camion(parametros[1])
    print(f'Costo total {costo}')

if __name__ == "__main__":
    import sys
    f_principal(sys.argv)