class Jugador:
    nombre = "Default"
    fuerza = 0
    defensa = 0
    vida = 0
    
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida


    def reduccionVida(self):
        self.vida = 0
        print(self.__nombre, "Has perdido el duelo")