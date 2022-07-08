import logging

from campeon import Campeon

logging.basicConfig(filename="logs/TP-OPP", level=logging.INFO)

'''Clase hija que extiende de Campeon'''

class Guerrero(Campeon):

    def __init__(self, nombre, fuerza, defensa, vida, espada):
        super().__init__(nombre, fuerza, defensa, vida)
        self.__espada = espada
    
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
    def get_espada(self):
        return self.__espada
        
    def set_espada(self, espada):
        if espada< 0:
            print("Error al ingresar un numero negativos")
        else:
            self.__espada = espada
    

    def special_move(self):
        opcion = int(input("Elige un movimiento especial: (1) Golpe duro, daño 10. (2) Corte, daño 8 "))
        if opcion == 1:
            Guerrero.set_espada(10)
        elif opcion == 2:
           Guerrero.set_espada(8)
        else:
            logging.info("El numero de movimiento es icorrecto")

    def status(self):
        super().status()
        logging.info("Espada: %s", str(self.__espada))

    def special_hit(self, enemigo):
        return self.fuerza*self.__espada - enemigo.defensa

   



