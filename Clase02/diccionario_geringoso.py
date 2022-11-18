def traduce(cadena):
    capadepenapa = ""
    vocales = 'aeiouáéíóúàèìòùäëïöü'
    for c in cadena:
        if c.lower() in vocales:
            capadepenapa += c + "p" + c
        else:
            capadepenapa += c
    return capadepenapa

lista = ['banana', 'manzana', 'mandarina']
lista_dict = {}
for palabra in lista:
    lista_dict[palabra] = traduce(palabra)

print(lista_dict)