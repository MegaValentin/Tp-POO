import logging
from campeon import Campeon

logging.basicConfig(filename="logs/TP-OPP", level=logging.INFO)


'''Clase hija que extiende de Campeon'''

class Arquero(Campeon):

    def __init__(self, nombre, fuerza, defensa, vida, arco):
        super().__init__(nombre, fuerza, defensa, vida)
        self.__arco = arco

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
  
