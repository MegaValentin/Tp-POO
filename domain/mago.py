import logging
from campeon import Campeon


logging.basicConfig(filename="logs/TP-OPP", level=logging.INFO)

'''Clase hija que extiende de Campeon'''

class Mago(Campeon):

    def __init__(self, nombre, fuerza, defensa, vida, libro):
        super().__init__(nombre, fuerza, defensa, vida)
        self.__libro = libro
    
    def get_fuerza(self):
        return self.__fuerza

    def set_fuerza(self, fuerza):
        if fuerza < 0:
            print("Error al ingresar un numero negativos")
        else:
            self.__fuerza = fuerza

    def get_defensa(self):
        return self.__defensa

    def set_defensa(self, defensa):
        if defensa < 0:
            print("Error al ingresar un numero negativos")
        else:
            self.__defensa = defensa

    def get_vida(self):
        return self.__vida
    
    def set_vida(self, vida):
        if vida < 0:
            print("Error al ingresar un numero negativos")
        else:
            self.__vida = vida
    def get_libro(self):
        return self.__libro

    def set_libro(self, libro):
        if libro< 0:
            print("Error al ingresar un numero negativos")
        else:
            self.__libro = libro
    
    def status(self):
        super().status()
        logging.info("Libro: %s", str(self.__libro))

    '''Funcion que hace referencia a un ataque especial del personaje'''

    def special_move(self):
        opcion = int(input("Elige un movimiento especial: (1) bolas de fuego, daño 10. (2) Picos de nieve, daño 8 "))
        if opcion == 1:
            Mago.set_libro(10)
        elif opcion == 2:
            Mago.set_libro(8)
        else:
            logging.info("El numero de movimiento es icorrecto")

    def special_hit(self, enemigo):
        return self.fuerza*self.__libro - enemigo.defensa