# import math
# x = math.sqrt(10)

# import urllib.request
# u = urllib.request.urlopen('http://www.python.org/')
# data = u.read()

# print(data)

def sumcount2(n):
    '''
    Devuelve la suma de los primeros n enteros
    '''
    total = 0
    for i in range(n+1):
        total += i
    return total

def sumcount(n):
    '''
    Devuelve la suma de los primeros n enteros
    '''
    total = 0
    while n > 0:
        total += n
        n -= 1
    return total

print(sumcount(100))
print(sumcount2(100))

numero_valido=False
while not numero_valido:
    try:
        a = input('Ingresá un número entero: ')
        n = int(a)
        numero_valido = True
    except ValueError:
        print('No es válido. Intentá de nuevo.')
print(f'Ingresaste {n}.')