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
        return f'Lote(\'{self.nombre}\', {self.cajones}, {self.precio})'

class MiLote(Lote):
    def __init__(self, nombre, cajones, precio, factor):
        # Fijate como es el llamado a `super().__init__()`
        super().__init__(nombre, cajones, precio)
        self.factor = factor
    def rematar(self):
        self.vender(self.cajones)
    def costo(self):
        # Fijate cómo usamos `super`
        return 1.25 * super().costo()