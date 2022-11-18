def add(x, y):
    return x + y

# print(add(3, 4))               # 7
# print(add('Hola', 'mundo'))    # 'Holamundo'
# print(add('3', '4'))           # '34'
# print(add(3, '4'))

def grok():
    ...
    raise RuntimeError('Epa!')   # Levanta una excepción acá

def spam():
    grok()                        # Esta llamada va a levantar una excepción

def bar():
    try:
        spam()
    except RuntimeError as e:     # Acá atrapamos la excepción
        ...
def foo():
    try:
        bar()
    except RuntimeError as e:     # Por lo tanto la excepción no llega acá
        ...

def grok():
    raise RuntimeError('Epa!')

def bar():
    try:
      grok()
    except RuntimeError as e:   # Excepción atrapada
        print('Fracasé. Motivo:', e)
        raise
                   # Ejecuta estos comandos
        
        ...

bar()