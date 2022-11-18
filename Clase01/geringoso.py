def es_vocal(a: str) -> bool:
    vocales = 'aeiouáéíóúàèìòùäëïöü'
    return a.lower() in vocales


cadena = input("Ingrese una palabra o frase: ")
capadepenapa = ''
vocales = 'aeiouáéíóúàèìòùäëïöü'

for c in cadena:
    if c.lower() in vocales:
        capadepenapa += c + "p" + c
    else:
        capadepenapa += c

print(capadepenapa)

capadepenapa = ""
for c in cadena:
    capadepenapa += ((c + "p" ) if c.lower() in vocales else "") + c

print(capadepenapa)