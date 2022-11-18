import itertools

numeros = 25
elijo = 15
res = 1
for _ in range(elijo):
    res = res * (numeros - _)
print(res)

def generador():
    a = range(25)
    combinations = list(itertools.permutations(a, 15))
    a = str(combinations)
    return a
    
print(len(generador()))