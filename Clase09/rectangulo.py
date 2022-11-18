# %%
class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'({self.x}, {self.y})'
    def __repr__(self):
        return f'Punto({self.x}, {self.y})'    
    def __add__(self, b):
        return Punto(self.x + b.x, self.y + b.y)

class Rectangulo:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    def __str__(self):
        return f'({self.p1.x}, {self.p1.y}), ({self.p2.x}, {self.p2.y})'
    def __repr__(self):
        return f'Rectangulo(Punto({self.p1.x}, {self.p1.y}), Punto({self.p2.x}, {self.p2.y}))'    
    def base(self):
        return abs(self.p1.x - self.p2.x)
    def altura(self):
        return abs(self.p1.y - self.p2.y)
    def desplazar(self, desplazamiento):
        self.p1 += desplazamiento
        self.p2 += desplazamiento

    def rotar(self):
        altura = self.altura()
        base = self.base()
        
        if self.p1.y > self.p2.y:
            self.p1.x += altura + base
            self.p1.y -= (altura + base)
        else:
            self.p2.x += altura
            self.p2.y -= altura
            self.p1.x += base
            self.p1.y -= base

ul = Punto(3,-2)
lr = Punto(1,2)
rect1 = Rectangulo(ul,lr)
print(rect1)
rect1.rotar()
print(rect1)


# %%
