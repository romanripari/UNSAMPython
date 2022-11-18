import math 

def volumen(radio:float ) -> float:
    return math.pi * radio ** 3 * 4 / 3

radio = float(input("Ingrese el radio de la esfera: "))

print(f"El volumen es {volumen(radio)}")
