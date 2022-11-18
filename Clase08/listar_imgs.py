import os
import sys

def archivos_png(directorio):
    '''
    Función que recibe un directorio en string y devuelve una lista con
    todos los archivos .png contenidos en él y sus subcarpetas
    '''
    archivos_png = []
    for _, _, files in os.walk(directorio):
        for name in files:
            if name.lower()[-4:] == ".png":
                archivos_png.append(name)
    return archivos_png

def f_principal():
    '''
    Para probar el script se puede ejecutar desde la consola:
    py listar_imgs.py ../Data/ordenar
    '''
    if len(sys.argv) != 2:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} directorio')
    print(archivos_png(sys.argv[1]))

if __name__ == '__main__':
    f_principal()
