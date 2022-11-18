import sys
from datetime import datetime, timedelta

# Ejercicio 8.1: Segundos vividos
def vida_en_segundos(fecha_nac:str) -> float:
    '''
    Función que recibe como parámetro una fecha con el formato:
        dd/mm/yyyy
    Devuelve la cantidad de segundos transcurridos entre la fecha
    recibida a las 00:00 hs y el instante actual.
    '''
    # Si no es el formato pedido, devuelve un error indicando cuál debe ser el correcto
    try:
        fnac_date = datetime.strptime(fecha_nac, '%d/%m/%Y')
    except ValueError:
        raise ValueError("El formato debe ser 'dd/mm/yyyy'")
    # Armamos un timedelta en la variable vida, contamos los días vividos y los segundos transcurridos el día de hoy
    vida = datetime.now() - fnac_date
    dias = vida.days
    seg_hoy = vida.seconds
    # Multiplicamos los días y sumamos los segundos de hoy para obtener los segundos totales
    seg_totales = float(dias * 24 * 60 * 60 + seg_hoy)
    return seg_totales

# Ejercicio 8.2: Cuánto falta
def falta_primavera():
    '''
    Función que busca la primaver más próxima y retorna un texto
    indicando cuántos días faltan para que llegue ese día
    '''
    # Se busca el año actual y la primavera de este año
    año_actual = datetime.now().year
    primavera = datetime(year = año_actual, month = 9, day = 21)
    # Si la primavera de este año ya pasó, se determina como la del siguiente año
    if primavera < datetime.now():
        primavera = datetime(year = año_actual+1, month = 9, day = 21)
    # Se resta a primavera, el día actual, generando un int
    dias_faltan = int((primavera - datetime.now()).days)
    return f'Faltan {dias_faltan} días para la primavera'

# Ejercicio 8.3: Fecha de reincorporación
def reincorporacion():
    empieza = datetime(year = 2020, month = 9, day = 26)
    licencia = timedelta(days=200)
    nueva_fecha = empieza + licencia
    # Agregué esto por si cae fin de semana. En ese caso, sigue aumentando un día
    # extra hasta que la nueva_fecha sea lunes (mientras que el weekday sea 5 o 6)
    while nueva_fecha.weekday() > 4:
        nueva_fecha += timedelta(days=1)
    return nueva_fecha    

# Ejercicio 8.4: Días hábiles
def dias_habiles(inicio, fin, feriados):
    fechas_feriados = []
    for f in feriados:
        fechas_feriados.append(datetime.strptime(f, '%d/%m/%Y'))
    try:
        finicio = datetime.strptime(inicio, '%d/%m/%Y')
        ffin = datetime.strptime(fin, '%d/%m/%Y')
    except ValueError:
        raise ValueError("El formato debe ser 'dd/mm/yyyy'")
    dias_habiles = 0
    while ffin >= finicio:
        if finicio.weekday() < 5 and finicio not in fechas_feriados:
            dias_habiles +=1
        finicio += timedelta(days=1)
    return dias_habiles

def run():
    '''
    Para probar el script se puede ejecutar desde la consola:
    py vida.py fecha_nac
    '''
    if len(sys.argv) != 2:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} fecha_nac')
    # print("**** 8.1 ****") 
    fecha = sys.argv[1]
    print(f'Tiempo transcurrido: {vida_en_segundos(fecha)} segundos')
    # print("**** 8.2 ****") 
    # print(falta_primavera())
    # print("**** 8.3 ****") 
    # print(reincorporacion())
    # print("**** 8.4 ****") 
    # feriados = ['12/10/2020', '23/11/2020', '7/12/2020', '8/12/2020', '25/12/2020']
    # print(dias_habiles('20/9/2020', '31/12/2020', feriados))

if __name__ == "__main__":
    run()