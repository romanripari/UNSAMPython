import random
from collections import Counter

def tirar(d: int) -> list:
    '''
    Función que recibe una cantidad de dados solicitados (d: int)
    y devuelve una tirada random de len() = d, con los 
    números del 1 al 6
    '''
    return random.choices([1,2,3,4,5,6], k =d)

def es_generala(tirada:list) -> bool:
    '''
    Función que recibe una tirada de dados (tirada: list) y analiza si es generala,
    devolviendo True si lo es o False si no lo es (-> bool)
    '''
    if len(set(tirada)) == 1:
        generala = True
    else:
        generala = False
    return generala

def es_generala_tres_tiros(tirada: list) -> bool:
    '''
    Función que recibe una tirada de dados (tirada: list) y analiza si es generala,
    devolviendo True si lo es o False si no lo es (-> bool). 
    Realiza hasta tres tiros
    '''
    #Empieza el resultado en False
    generala = False
    #Determino los tiros extra después del original
    tiros = 2
    #Primera comprobación: si es generala servida
    if len(set(tirada)) == 1:
        generala = True
    else:
        #Si no es generala, obtenemos el número más repetido (o uno de ellos) y la cantidad de veces que aparece
        nro_elegido, cantidad = Counter(tirada).most_common()[0]
        #Determinamos la cantidad de dados que NO son el nro que más aparece
        dados_necesarios = 5 - cantidad
        #Recorremos tantas veces como tiros extra:
        for t in range(tiros):
            #Generamos una nueva tirada
            tirada = tirar(dados_necesarios)
            # Si son todos los números iguales entre sí, e iguales a nro, es porque hay generala
            if (len(set(tirada)) == 1 and tirada[0] == nro_elegido):
                generala = True
                break
            else:
                #Si no, recorremos los elemenos de la nueva tirada
                for d in tirada:
                    #Si el elemento es igual al número que más aparecía, quitamos UN dado necesario para la próxima vuelta
                    if d == nro_elegido:
                        dados_necesarios -=1
                #Si no hay más dados necesarios, es porque hay generala            
                if dados_necesarios == 0:
                    generala = True
                    break

    return generala

def es_generala_levanto_todos_distintos(tirada: list, tiros) -> bool:
    '''
    Adaptación de la función es_generala, en la cual se implementa
    la opción de levantar todo en caso de que sean todos los números
    diferentes al tirar 5 dados
    '''

    generala = False
    tiros -=1
    if len(set(tirada)) == 1:
        generala = True
    else:
        if len(set(tirada)) == 5:
            tirada = tirar(5)
            dados_necesarios = 5
            es_generala_levanto_todos_distintos(tirada,tiros)
        else:
            nro, cantidad = Counter(tirada).most_common()[0]
            dados_necesarios = 5 - cantidad

            for t in range(tiros):
                tirada = tirar(dados_necesarios)
                if (len(set(tirada)) == 1 and tirada[0] == nro):
                    generala = True
                    break
                else:
                    for d in tirada:
                        if d == nro:
                            dados_necesarios -=1
                    if dados_necesarios == 0:
                        generala = True
                        break
    return generala

def prob_generala(N):
    G = sum([es_generala_tres_tiros(tirar(5)) for i in range(N)])
    prob = G/N
    return prob
    

def run():

    N = 100000
    prob = prob_generala(N)
    print(f'Podemos estimar la probabilidad de sacar generala en tres tiros en {prob:.6f}.')

    # # Descomentar para testear levantar todo vs dejar uno al azar si son los 5 dados diferentes:
    
    # G = sum([es_generala(tirar(5)) for i in range(N)])
    # prob = G/N

    # G = sum([es_generala_levanto_todos_distintos(tirar(5), 3) for i in range(N)])
    # prob2 = G/N
    # print(f'dejando uno: {prob}, levantando todo: {prob2}' )


if __name__ == "__main__":
    run()