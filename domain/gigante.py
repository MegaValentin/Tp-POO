
import logging

from campeon import Campeon

logging.basicConfig(filename="logs/TP-OPP", level=logging.INFO)

'''Clase hija que extiende de Campeon'''

class Gigante(Campeon):

    def __init__(self, nombre, fuerza, defensa, vida, bate):
        super().__init__(nombre, fuerza, defensa, vida)
        self.__bate = bate
    
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
    def get_bate(self):
        return self.__bate
    
    def set_bate(self, bate):
        if bate< 0:
            print("Error al ingresar un numero negativos")
        else:
            self.__bate = bate
    
    def special_move(self):
        opcion = int(input("Elige un movimiento especial: (1)Aplastar-->daño 20, (2)Demoler-->daño 15"))
        if opcion == 1:
           Gigante.set_bate(20)
        elif opcion == 2:
            Gigante.set_bate(15)
        else:
            logging.info("El numero de movimiento es incorrecto")

    def status(self):
        super().status()
        logging.info("Bate: %s", str(self.__bate))
    
    def special_hit(self, enemigo):
        return self.fuerza*self.bate - enemigo.defensa
        
