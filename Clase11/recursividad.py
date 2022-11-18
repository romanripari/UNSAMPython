#%%

def granos_de_trigo(n):
    if n ==1:
        granos = 1
    else:
        granos = 2 * granos_de_trigo(n-1)
    return granos
granos_de_trigo(64)

# %%
from datetime import datetime
f = 8
t1 = datetime.now()
def fibonacci(n):
    if n==1 or n ==2:
        res = 1
    else:
        res = fibonacci(n-1) + fibonacci(n-2) 
    return res
fibonacci(f)
# %%
t2 = datetime.now()
def fib(n):
    """Precondición: n >= 0.
       Devuelve: el número de Fibonacci número n."""
    if n == 0 or n == 1:
        return n
    ant2 = 0
    ant1 = 1
    for i in range(2, n + 1):
        fibn = ant1 + ant2
        ant2 = ant1
        ant1 = fibn
    return fibn
fibonacci(f)
t3 = datetime.now()
print("El primero tardó", str(t2-t1))
print("El segundo tardó", str(t3-t2))
# %%
# Ejercicio 11.1 factorial
def factorial(n):
    """Precondición: n entero positivo
       Devuelve: n!"""
    if n == 1:
        return 1
    return n * factorial(n - 1)
factorial(3)
# %%
def factorial(n):
    if n == 1:
        r = 1
        return r

    f = factorial(n-1)
    r = n * f
    return r
factorial(70)
# %%
def factorial(n):
    """Precondición: n entero positivo
       Devuelve: n!"""
    fact = 1
    for num in range(n, 1, -1):
        fact *= num
    return fact
factorial(70)
# %%
def potencia(b,n):
    """Precondición: n >= 0
       Devuelve: b^n."""

    if n <= 0:
        # caso base
        return 1

    if n % 2 == 0:
        # caso n par
        p = potencia(b, n // 2)
        return p * p
    else:
        # caso n impar
        p = potencia(b, (n - 1) // 2)
        return p * p * b
print(potencia(37,2))

def potencia2(base, exp):
    'Calcula la potencia exp del número base, con exp entero mayor que 0.'
    resultado = 1
    for i in range(exp):
        resultado *= base
    return resultado
print(potencia2(37,2))
# %%
def potencia(b, n):
    """Precondición: n >= 0
       Devuelve: b^n."""
    pila = []
    while n > 0:
        if n % 2 == 0:
            pila.append(True)
            n //= 2
        else:
            pila.append(False)
            n = (n - 1) // 2
    p = 1
    while pila:
        es_par = pila.pop()
        if es_par:
            p *= p
        else:
            p *= p * b
    return p
print(potencia2(37,2))