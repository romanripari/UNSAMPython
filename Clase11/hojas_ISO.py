contador = 0
def medidas_hoja_A(N):
    global contador
    contador +=1
    '''Recibe un {N} mayor a cero y devuelve las medidas (ancho, largo) de la hoja DIN A{N}'''
    if N == 0:                          # Caso base, si es A0
        return (841, 1189)
    ancho, largo = medidas_hoja_A(N-1)  # Si no es caso base, busca ancho y largo del N anterior
    return (largo // 2, ancho)          # retorna tupla (ancho = largo_ant // 2, largo = ancho_ant)

def run():
    # One-Liner para ver en pantalla las medidas de las hojas de A10 a A0
    # print("A7", medidas_hoja_A(7))
    print( "\n".join([f'A{N}. {medidas_hoja_A(N)[0]} x {medidas_hoja_A(N)[1]}' for N in range(11)]))
    print(contador)
if __name__ == '__main__':
    run()
