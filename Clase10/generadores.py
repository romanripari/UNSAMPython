# %%
def regresiva(n):
    print('Cuenta regresiva desde', n)
    while n > 0:
        yield n
        n -= 1

for x in regresiva(10):
    print(x, end=' ')
# %%
x = regresiva(10)

# %%
x
# %%
x.__next__()

# %%
def filematch(filename, substr):
    with open(filename, 'r') as f:
        for line in f:
            if substr in line:
                yield line
# %%
for line in open('../Data/camion.csv'):
    print(line, end='')
print('***')
for line in filematch('../Data/camion.csv', 'Naranja'):
    print(line, end='')
# %%
a = [1,2,3,4]
b = (2*x for x in a)
b
# %%
for i in b:
   print(i, end=' ')

'''
(<expresión> for i in s if <condición>)
Que puede leerse como .... el valor es <expresión> para cada elemento i perteneciente a s siempre y cuando <condición> se cumpla.
'''
# %%
b = (2*x for x in a)
print(sum(b))
print(sum(2*x for x in a))
# %%
a = [1,2,3,4]
b = (x*x for x in a)
c = (-x for x in b)
for i in c:
  print(i, end=' ')

# %%

f = open('lote.py', encoding='utf8')
lines = (line for line in f if '#' in line)
for line in lines:
    print(line)
f.close()
# %%
import itertools
a = [1,2,3,4]
b = (x*x for x in a)

itertools.filterfalse(a, b)
# %%
nums = [1, 2, 3, 4, 5]
cuadrados = (x*x for x in nums)
cuadrados
# %%
for n in cuadrados:
    print(n)
# %%
from datetime import datetime 
nums = [2] *100000000
t1 = datetime.now()
print(sum([x*x for x in nums]))    # una lista por comprensión
t2 = datetime.now()
print(sum(x*x for x in nums))      # una expresión generadora
t3 = datetime.now()
print(t2-t1, " tardó el primero")
print(t3-t2, " tardó el segundo")
print("porcentaje de efectividad del 1 sobre el 2:", (t3-t2) / (t2-t1) * 100 )
# %%
