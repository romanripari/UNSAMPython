import os
from datetime import datetime
import sys

def procesar_nombre(fname:str):
    '''
    Función que recibe el nombre de un archivo y devuelve
    como tupla la fecha y el nombre corregido
    '''
    fecha = fname[-12:-4]
    #Intento armar la fecha a partir del nombre. Si no se logra, continúa con el siguiente.
    try:
        date_object = datetime(year = int(fecha[:4]), month = int(fecha[4:6]), day = int(fecha[6:]))
        nombre = fname.replace("_" + fecha,"")
        return nombre, date_object
    except ValueError:
        raise ValueError(f"El archivo {fname} debe finalizar con '_yyyymmdd.png' para ser procesado correctamente")
    
def procesar(fname:str):
    '''
    Recibe la ruta de un archivo .png y lo procesa:
        - Obtiene la fecha y el nuevo nombre con procesar_nombre
        - Cambia la fecha de acceso y de modificación del archivo
        - Renombra el archivo y lo mueve a la carpeta '../Data/imgs_procesadas/' (Solo si no existen previamente)
    '''
    # Obtengo nombre limpio y fecha
    nombre, fecha = procesar_nombre(fname)
    # Cambio fechas en las propiedades
    ts  = fecha.timestamp()
    os.utime(fname, (ts, ts))
    # Determino la nueva ubicación 
    nueva_ubicacion = os.path.join(sys.argv[2], os.path.basename(nombre))
    os.rename(fname, nueva_ubicacion)

def borrar_vacios(directorio):
    '''
    Recibe un directorio como str y elimina todas las carpetas que estén vacías
    '''
    for root, dirs, _ in os.walk(directorio, topdown=False):
        for carpeta in dirs:
            if os.listdir(os.path.join(root, carpeta)) == []:
                os.rmdir(os.path.join(root, carpeta))

def buscar_png(directorio:str='../Data/ordenar'):
    '''
    Recibe un directorio en string y lo recorre.
    Si encuentra archivos .png los procesa
    '''
    for root, _, files in os.walk(directorio):
        for archivo in files:
            if archivo.lower()[-4:] == ".png":
                procesar(os.path.join(root, archivo))
    #Borro las carpetas vacías
    borrar_vacios(directorio)

def crea_directorio(directorio:str='../Data/imgs_procesadas/'):
    '''
    Recibe un directorio como str y si la ruta no existe, la crea
    '''
    if not os.path.exists(directorio):
        os.mkdir(directorio)

def descomprime():
    import zipfile
    with zipfile.ZipFile('../Data/ordenar.zip', 'r') as zip_ref:
        zip_ref.extractall('../Data')

def f_principal():
    '''
    Para probar el script se puede ejecutar desde la consola:
    py ordenar_imgs.py ../Data/ordenar ../Data/imgs_procesadas/
    '''

    descomprime()
    if len(sys.argv) != 3:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} directorio_original directorio_odestino')
    #Creo el directorio para pegar las imágenes, si no existe
    crea_directorio(sys.argv[2])
    #Busco para procesar los archivos .png
    buscar_png(sys.argv[1])
    
if __name__ == '__main__':
    f_principal()
