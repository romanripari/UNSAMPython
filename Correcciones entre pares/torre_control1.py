# %% torre_control.py

class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola 
        y devuelve su valor. 
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve 
        True si la cola esta vacia, 
        False si no.'''
        return len(self.items) == 0
    
class TorreDeControl:
    
    def __init__(self):
        self.arribos = Cola()
        self.partidas = Cola()

    def nuevo_arribo(self, ID_vuelo):
        self.arribos.encolar(ID_vuelo)

    def nueva_partida(self, ID_vuelo):
        self.partidas.encolar(ID_vuelo)
        
    def asignar_pista(self):
        if self.arribos.esta_vacia() == True:
            if self.partidas.esta_vacia() == True:
                print('No hay vuelos en espera.')
            else:
                despegue = self.partidas.desencolar()
                print('El vuelo', str(despegue), 'despegó con éxito.' )
        else:
            aterrizaje = self.arribos.desencolar()
            print('El vuelo', str(aterrizaje), 'aterrizó con éxito.')

    def ver_estado(self):
        vuelos_salientes = 'Vuelos esperando para despegar: '
        vuelos_entrantes = 'Vuelos esperando para aterrizar: '
        for i, vuelo in enumerate(self.partidas.items):
            if i == len(self.partidas.items) - 1:
                vuelos_salientes += vuelo 
            else:
                vuelos_salientes += vuelo + ', '
        for i, vuelo in enumerate(self.arribos.items):
            if i == len(self.arribos.items) - 1:
                vuelos_entrantes += vuelo
            else:
                vuelos_entrantes += vuelo + ", "
        print(vuelos_entrantes)
        print(vuelos_salientes)

torre = TorreDeControl()
torre.nuevo_arribo('AR156')
torre.nueva_partida('KLM1267')
torre.nuevo_arribo('AR32')
torre2 = TorreDeControl()
torre2.nueva_partida("partida1")
torre2.nueva_partida("partida2")
torre2.ver_estado()
torre2.asignar_pista()
torre2.nueva_partida("partida4")
torre2.ver_estado()
# torre.asignar_pista()
# torre.asignar_pista()
# torre.asignar_pista()
# torre.ver_estado()
# torre.asignar_pista()
# torre.asignar_pista()


# %%
