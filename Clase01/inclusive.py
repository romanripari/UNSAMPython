frase = 'Los hermanos sean unidos'
palabras = frase.split()
frase_t = ""
for palabra in palabras:
    palabra_nueva = ""
    if palabra[-1].lower() == "o": 
        for letra in palabra[0:-1]:
            palabra_nueva = palabra_nueva + letra
        palabra_nueva = palabra_nueva  + "e" 
    elif  (palabra[-1].lower() == "s" and palabra[-2].lower() == "o"): 
        for letra in palabra[0:-2]:
            palabra_nueva = palabra_nueva + letra
        palabra_nueva = palabra_nueva  + "es" 
    else:
        palabra_nueva = palabra
    frase_t = frase_t   + " " + palabra_nueva

print(frase_t)
