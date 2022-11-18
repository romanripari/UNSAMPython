# def add(x, y):
#     assert isinstance(x, int), 'Necesito un entero (int)'
#     assert isinstance(y, int), 'Necesito un entero (int)'
#     return x + y

# x = 3
# y = 2

# print(add(x,y))

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

rta = tiene_a ('wwwwwwwwwwwwwwwwwwww')
print(rta)