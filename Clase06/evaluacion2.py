import csv
from informe_funciones import leer_camion

def costo_camion(nombre_archivo):
        camion= leer_camion(nombre_archivo)
        print(camion)
        total_pagado=0
        for s in camion:
            total_pagado+= int(s['cajones']) * float(s['precio'])

        return total_pagado
costo = costo_camion('../Data/camion.csv')
print('Costo Total:', costo)