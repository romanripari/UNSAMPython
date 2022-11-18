cadena = "ciudades o barrios"
salida = ""
vocales = "aeiou"
# Corrección:
# for c in cadena.lower():
#         if c in vocales:
#             salida += c + "p" + c 
#         else:
#             salida += c
            
for c in cadena.lower():
        pos = vocales.find(c)
        if pos == 0:
            salida += "apa"
        elif pos == 1:
            salida += "epe"
        elif pos == 2:
            salida += "ipi"
        elif pos == 3:
            salida += "opo"
        elif pos == 4:
            salida += "upu"         
        else:
            salida += c

print(salida)