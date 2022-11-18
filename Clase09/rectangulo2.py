class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_origen(self):
        n = (self.x**2 + self.y**2)**(1/2)
        return n

    def mover(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return f'({self.x},{self.y})'

    def __repr__(self):
        return f'Punto({self.x},{self.y})'

    def __add__(self, otro):
        return Punto(self.x + otro.x, self.y + otro.y)
    


class Rectangulo:

    def __init__(self, p1, p2):
        self.p1=p1
        self.p2=p2

    def base(self):
        return abs(self.p1.x - self.p2.x)
        

    def altura(self):
        return abs(self.p1.y - self.p2.y)
        

    def area(self):
        return self.base()*self.altura()
        

    def __str__(self):
        return f'''
Rectángulo dado por los puntos {self.p1} y {self.p2}.
Base= {self.base()}, Altura= {self.altura()} y Área= {self.area()}
                '''
        

    def __repr__(self):
        return f'Objeto Rectángulo ({self.p1},{self.p2})'
        

    def desplazar(self,desplaz):
        self.p1=p1.__add__(desplaz)
        self.p2=p2.__add__(desplaz)


    def rotar(self):
        if self.p1.x < self.p2.x:       ####casos 1 y 2

            if self.p1.y < self.p2.y:       #caso 1
                n1=Punto(self.p1.x + self.base(), self.p1.y)
                
            else:                           #caso 2
                n1=Punto(self.p2.x, self.p2.y)
            

        else:                           ####casos 3 y 4            self.p1.x > self.p2.x 

            if self.p1.y < self.p2.y:       #caso 3
                n1=Punto(self.p1.x, self.p1.y)

            else:                           #caso 4
                n1=Punto(self.p2.x + self.base(), self.p2.y)

        n2=Punto(n1.x + self.altura() , n1.y + self.base() )

        self.p1=n1
        self.p2=n2 

            

p1=Punto(1,1)
p2=Punto(2,2)


r=Rectangulo(p1,p2)

print(r)

r.rotar()
print(r)