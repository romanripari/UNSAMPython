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
    '''Representa a una Torre de Control, con operaciones agregar arribos o partidas pendientes.
    Asigna pista prioritariamente para los arribos según orden de llegada, 
    y luego a las partidas según orden de llegada.
    '''
    def __init__(self):
        '''Crea arribos y partidas vacías'''
        self.arribos = Cola()
        self.partidas = Cola()

    def nuevo_arribo(self, x):
        '''Encola un arribo'''
        self.arribos.encolar(x)

    def nueva_partida(self, x):
        '''Encola una partida'''
        self.partidas.encolar(x)

    def ver_estado(self):
        '''Devuelve el estado de arribos y partidas'''
        texto = f'Vuelos esperando para aterrizar: {", ".join(self.arribos.items)}\n'\
                f'Vuelos esperando para despegar: {", ".join(self.partidas.items)}'   
        print(texto)

    def asignar_pista(self):
        '''Si hay arribos, le asigna pista al primero que se incorporó
            Si hay partidas, le asigna pista a la primera que se incorporó
            Si no hay vuelos en espera, lo informa'''
        if not self.arribos.esta_vacia():
            print(f'El vuelo {self.arribos.desencolar()} aterrizó con éxito.')
        elif not self.partidas.esta_vacia():
            print(f'El vuelo {self.partidas.desencolar()} despegó con éxito.')
        else:
            print('No hay vuelos en espera')
    
    def __str__(self):
        return f'(Arribos: {self.arribos.items}, Partidas: {self.partidas.items})'

    

