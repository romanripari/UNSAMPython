# %%
# Clase Canguro con la modificación del bug:
# canguro_malo.py
"""Este código continene un 
bug importante y dificil de ver
"""
class Canguro:
    """Un Canguro es un marsupial."""
    def __init__(self, nombre, contenido=[]):
        """Inicializar los contenidos del marsupio.
        nombre: string
        contenido: contenido inicial del marsupio, lista.
        """
        self.nombre = nombre
        # la LISTA contenido, al ser un objeto mutable, debe reiniciarse. 
        # Puede hacerse como copia
        # self.contenido_marsupio = contenido
        self.contenido_marsupio = contenido.copy()
    def __str__(self):
        """devuelve una representación como cadena de este Canguro.
        """
        t = [ self.nombre + ' tiene en su marsupio:' ]
        for obj in self.contenido_marsupio:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)
    def meter_en_marsupio(self, item):
        """Agrega un nuevo item al marsupio.
        item: objecto a ser agregado
        """
        self.contenido_marsupio.append(item)

# Mi clase Canguro:
class Canguro:
    def __init__(self, nombre, contenido_marsupio=[]):
        self.nombre = nombre
        self.contenido_marsupio = contenido_marsupio.copy()

    def meter_en_marsupio(self, cosas):
        if not isinstance(cosas, Canguro):
            self.contenido_marsupio.append(cosas)
        else:
            self.contenido_marsupio.append(str(cosas.nombre))

    def __str__(self):
        texto = f'{self.nombre} tiene en su marsupio:' + '\n'
        for cosas in self.contenido_marsupio:
            if not isinstance(cosas, Canguro):
                texto += cosas + '\n'
            else:
                texto += str(cosas.nombre) + '\n'
        return texto

madre_canguro = Canguro(nombre='Madre')
cangurito = Canguro(nombre='gurito')
madre_canguro.meter_en_marsupio('billetera')
madre_canguro.meter_en_marsupio('llaves del auto')
madre_canguro.meter_en_marsupio(cangurito)
cangurito.meter_en_marsupio('algo')
print(madre_canguro)
print(cangurito)
# %%
