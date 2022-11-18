# %%
class Jugador:
    def __init__(self, x, y):
        # Todo dato guardado en `self` es propio de esa instancia        self.x = x
        self.y = y
        self.salud = 100

    def mover(self, dx, dy):
        self.x += dx
        self.y += dy
    def izquierda(self, dist):
        #mover(-dist, 0)      # NO! Refiere a una función global `mover`.
        self.mover(-dist, 0) # Sí. Llama al método `mover` definido antes.

    def lastimar(self, pts):
        self.salud -= pts


# %%
a = Jugador(2, 3)    # Clase Jugador definida antes
b = Jugador(10, 20)
 
# %%
