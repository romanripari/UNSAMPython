def medidas_hoja_A(N):
    '''Devuelve el ancho y largo de la hoja A(N) para todo N entero positivo o cero'''
    ancho = 841
    largo = 1189
    if N == 0: #caso base para el tamaño de hoja A0
        return (ancho, largo)
    else:
        (ancho, largo) = medidas_hoja_A(N-1)
        if largo > ancho:
            largo =largo//2#doblo a la mitad la hoja lo que invierte el ancho y el largo
        return (largo,ancho)#invierto el largo por el ancho y el ancho por el largo

def run():
    # One-Liner para ver en pantalla las medidas de las hojas de A10 a A0
    print( "\n".join([f'A{N}. {medidas_hoja_A(N)[0]} x {medidas_hoja_A(N)[1]}' for N in range(11)]))
if __name__ == '__main__':
    run()