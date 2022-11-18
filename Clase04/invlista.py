
def invertir_lista(lista):
    lista_invertida = []
    for e in lista:
        lista_invertida = [e] + lista_invertida
#        lista_invertida = [ e, *lista_invertida]
#        lista_invertida.insert(0, e)
    return lista_invertida

def run():    

    print(invertir_lista([1, 2, 3, 4, 5]))
    print(invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']))

if __name__ == "__main__":
    run()
