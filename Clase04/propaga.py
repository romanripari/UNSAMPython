# Defino la función
def propagar(fosforos):
    #Recorro la lista con enumerate para usar el índice
    for i, f in enumerate(fosforos):
        # Primera condición: si el fósforo es 1
        if fosforos[i] == 1:
            
            # Si NO es la posición 1 y el anterior es 0, entonces prende el anterior
            if i > 0 and fosforos[i-1] == 0:
                fosforos[i-1] = 1
                #Como prendimos un nuevo fósforo, volvemos a evaluar todo
                propagar(fosforos)

            # Si NO es la última posición y el siguiente es 0, entonces prende el siguiente
            if i != len(fosforos) -1 and fosforos[i + 1] == 0:
                fosforos[i + 1] = 1
                #Como prendimos un nuevo fósforo, volvemos a evaluar todo
                propagar(fosforos)

        # Cuando ya recorrió todos los fósforos, devuelve la lista fósforos.
        # Mientras tanto, en cada vuelta de recursividad, va devolviendo
        # el nuevo "estado" de los fósforos, siempre con uno
        # más prendido fuego
    return fosforos

def run():
    print(propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]))
    print(propagar([ 0, 0, -1, 1, 0, 0]))

if __name__ == "__main__":
    run()

