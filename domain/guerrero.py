from campeon import Campeon
import logging

from domain.personaje import Personaje

logging.basicConfig(filename="logs/TP-OPP", level=logging.INFO)

'''Clase hija que extiende de Campeon'''

class Guerrero(Personaje):

    def __init__(self, nombre, fuerza, defensa, vida, espada):
        super().__init__(nombre, fuerza, defensa, vida)
        self.__espada = espada

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


x = Guerrero("mati", 10, 40,100, 20)

x.atributos()