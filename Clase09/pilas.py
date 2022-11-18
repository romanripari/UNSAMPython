# %%
class Pila:
    def __init__(self):
        self.elementos = []

    def apilar(self, x):
        self.elementos.append(x)
        
    def desapilar(self):
        if self.esta_vacia():
            raise ValueError('La Pila esta vacia')
        return self.elementos.pop()
    def esta_vacia(self):
        return len(self.elementos) == 0

class Pila():
    def __init__(self):
        self.elementos = []
        
    def apilar(self,elemento):
        self.elementos.append(elemento)
        
    def desapilar(self):
        return self.elementos.pop()
        
    def esta_vacia(self):
        return len(self.elementos) == 0

def mostrar_x_del_estado(estado):
    print(f"Ejecutando {estado['función']}(), x vale {estado['variables']['x']}")

pila_de_llamadas = Pila()
#la ejecución está en la línea 3 de g(). El estado tiene x=10.
estado = {'función': 'g', 'próxima_línea_a_ejecutar': 3, 'variables': {'x': 10, 'b': 45}}
mostrar_x_del_estado(estado)
#sigo ejecutando, toca llamar a f(): incremento y apilo el estado.
estado['próxima_línea_a_ejecutar'] = 5
pila_de_llamadas.apilar(estado)
#llamo a f y ejecuto primeras líneas
estado = {'función': 'f', 'próxima_línea_a_ejecutar': 3, 'variables': {'x': 50, 'a': 20}}
mostrar_x_del_estado(estado)
#termina ejecución de f: se desapila el estado:
estado = pila_de_llamadas.desapilar()
mostrar_x_del_estado(estado)
# %%
