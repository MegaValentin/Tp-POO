from campeon import Campeon
import logging

from domain.personaje import Personaje

logging.basicConfig(filename="logs/TP-OPP", level=logging.INFO)


'''Clase hija que extiende de Campeon'''

class Arquero(Personaje):

    def __init__(self, nombre, fuerza, defensa, vida, arco):
        super().__init__(nombre, fuerza, defensa, vida)
        self.__arco = arco

    def get_arco(self):
        return self.__arco

    def set_arco(self, arco):
        if arco < 0:
            print("Error al ingresar un numero negativos")
        else:
            self.__arco = arco

    '''Funcion que hace referencia a un ataque especial'''

    def special_move(self):
        opcion = int(input("Elige un movimiento especial: (1)flechas multiples-->daño 15, (2)Flecha dorada-->daño 10"))
        if opcion == 1:
            Arquero.set_arco(15)
        elif opcion == 2:
            Arquero.set_arco(10)
        else:
            logging.info("El numero de moviemiento es incorrecto")

    '''Funcion que hace referencia a las caracteristicas del objeto de la carta '''

    def status(self):
        super().status()
        logging.info("Arco: %s", str(self.__arco))
    
    '''funcion que hace referencia a un ataque critico'''

    def special_hit(self, enemigo):
        return self.fuerza*self.__arco - enemigo.defensa
  
x = Arquero("mati", 10, 20, 100, 20)
x.status()