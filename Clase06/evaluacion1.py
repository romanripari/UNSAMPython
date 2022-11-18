import informe_funciones
def costo_camion(nombre_archivo):
    return informe_funciones.leer_camion(nombre_archivo)

ruta_camion = '../Data/fecha_camion.csv'
print(costo_camion(ruta_camion))