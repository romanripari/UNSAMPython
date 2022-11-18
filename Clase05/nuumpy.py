import numpy as np
from pprint import pprint
a = np.array([1, 2, 3, 4, 5, 6])
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)

print(np.zeros(2))
print(np.ones(13))
print(np.empty(2))
print(np.arange(5))
print(np.arange(73, 101, 6))
print(np.linspace(0, 10, num=4))
print("números impares entre el 1 y el 19 inclusive usando arange()")
print(np.arange(1, 10, 2))
print(np.linspace(1, 9, 5))

print(np.ones(2, dtype=np.int64))

arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
print(np.sort(arr))

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

print(np.concatenate((a, b)))

array_ejemplo = np.array([[[0, 1, 2, 3],
                            [4, 5, 6, 7]],
                           [[0, 1, 2, 3],
                            [4, 5, 6, 7]],
                           [[0 ,1 ,2, 3],
                            [4, 5, 6, 7]]])

print(array_ejemplo.ndim )
print(array_ejemplo.shape  )
print(array_ejemplo.size)

a = np.arange(6)
b = a.reshape(3, 2)
print(b)

a = np.array([1, 2, 3, 4, 5, 6])
print(a.shape)

vec_fila = a[np.newaxis, :]
vec_col = a[:, np.newaxis]
print(vec_fila.shape)
print(vec_col.shape)

data = np.array([1, 2, 3])
print(data[1], data[0:2], data[1:], data[-2:])

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a[a < 7])
five_up = (a >= 5)
print(a[five_up], "---", five_up )
c = a[(a > 2) & (a < 11)]
print(c)

b = np.nonzero(a < 5)
print(b)

lista_de_coordenadas = list(zip(b[0], b[1]))

pprint(lista_de_coordenadas)
print(a[b])

a = np.array([1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
print(a)
arr1 = a[3:8]
arr1[0] = 44
print(a)

# Operaciones

data = np.array([3, 2, 4, 71])
ones = np.ones(4, dtype=int)
print(data + ones)
print(data - ones)
print(data ** ones)
print(data / ones)

print(data * 1.6)
print(data.max())
print(data.min())
print(data.mean())
print(data.sum())
print(data.prod())
print(data.std())



a = np.array([[0.45053314, 0.17296777, 0.34376245, 0.5510652],
              [0.54627315, 0.05093587, 0.40067661, 0.55645993],
              [0.12697628, 0.82485143, 0.26590556, 0.56917101]])

print(a.min(axis=0))