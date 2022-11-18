import os
import sys

def archivos_png(directorio):
    '''
    Función que recibe un directorio en string y devuelve una lista con
    todos los archivos .png contenidos en él y sus subcarpetas
    '''
    # walker = os.walk(directorio)
    return      ((raiz, archivo_png) 
                for raiz, _, archivos in os.walk(directorio) 
                for archivo_png in archivos
                if ".png" in archivo_png.lower())

def f_principal():
    '''
    Para probar el script se puede ejecutar desde la consola:
    py listar_imgs.py ../Data/ordenar
    '''
    # listado = archivos_png('../Data/ordenar')
    # for l in listado:
    #     print(l)

    if len(sys.argv) != 2:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} directorio')
    for a in archivos_png(sys.argv[1]):
        print(a)

if __name__ == '__main__':
    f_principal()
