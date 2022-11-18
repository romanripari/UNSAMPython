# %%
class Lote:
    
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio
    def costo(self):
        return self.cajones * self.precio
    def vender(self, c):
        self.cajones -= c
    def __repr__(self):
        return f'Lote({self.nombre},{self.cajones},{self.precio})'    #agrego método especial __str__() para dar formato a la impresion de objeto
    def __str__(self):
        return f'({self.nombre}, {self.cajones}, {self.precio})'

m = Lote('Mandarina', 100, 45.7)

# %%
m
# %%
eval('m.__repr__()')
# %%
# %%
print(eval('m.__repr__()'))