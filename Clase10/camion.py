'''
camion.py
'''
class Camion:

    def __init__(self, lotes):
        '''Generador de camiones con Lotes.lotes'''
        self.lotes = lotes

    def __iter__(self):
        '''Devuelve el próximo lote'''
        return self.lotes.__iter__()

    def __contains__(self, nombre):
        '''Expresión generadora: Devuelve True o False
            si existe al menos un lote con lote.nombre = nombre'''
        return any((lote.nombre == nombre for lote in self.lotes))

    def precio_total(self):
        '''Expresión generadora: Devuelve el costo total,
            sumando el costo para cada lote'''
        return sum((l.costo() for l in self.lotes))

    def contar_cajones(self):
        '''Devuelve la cantidad total para cada lote.nombre'''
        from collections import Counter
        cantidad_total = Counter()
        for lote in self.lotes:
            cantidad_total[lote.nombre] += lote.cajones
        return cantidad_total

    def __str__(self):
        '''Devuelve una lista de todos los lotes contenidos'''
        texto = f'Camion con {len(self.lotes)} lotes\n'
        for lote in self.lotes:
            texto += f'Lote de {lote.cajones} cajones de \'{lote.nombre}\', pagados a ${lote.precio} cada uno.\n'
        return texto
    
    def __repr__(self):
        return f'Camion({[lote for lote in self.lotes]})'

    def __len__(self):
        return len(self.lotes)
    
    def __getitem__(self,a):
        return self.lotes[a]

'''
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
'''
