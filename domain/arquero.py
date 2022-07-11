import logging
from campeon import Campeon

logging.basicConfig(filename="logs/TP-OPP", level=logging.INFO)

'''Clase hija que extiende de Campeon'''
class Arquero(Campeon):

    # Metodo Constructor
    def __init__(self, nombre, fuerza, defensa, vida, arco):
        self.nombre = nombre
        self.__fuerza = fuerza
        self.__defensa = defensa
        self.__vida = vida
        self.__arco = arco

    def __str__(self) -> str:
        return self.nombre  + ": " + str(self.__fuerza) + " " + str(self.__defensa) + " " + str(self.__vida) + " " + str(self.__arco)
   
    ## GET Y SET ##
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
    ## GET y SET

    def status(self):
        logging.info( "%s",str(self.nombre))
        logging.info("Fuerza: %s ", str(self.__fuerza))
        logging.info("Defensa: %s ", str(self.__defensa))
        logging.info("Vida: %s", str(self.__vida))
        logging.info("Espada: %s", str(self.__arco))
    
    def esta_vivo(self):
        return self.__vida >= 0
    
    def morir(self):
        self.__vida = 0
        logging.info(" ha muerto %s", str(self.nombre ))

    '''Funcion que hace referencia a un ataque especial'''
    def special_move(self):
        opcion = int(input("Elige un movimiento especial: (1)flechas multiples-->daño 15, (2)Flecha dorada-->daño 10"))
        if opcion == 1:
            self.__arco = 15
        elif opcion == 2:
            self.__arco = 10
        else:
            logging.info("El numero de moviemiento es incorrecto")

    '''funcion que hace referencia a un ataque critico'''
    def special_hit(self, enemigo):
        return self.__fuerza*self.__arco - enemigo.__defensa

    def damage(self, enemigo):
        blow = self.__fuerza - enemigo.__defensa
        if blow < 0 :
            blow = 0
            logging.info("null blow")
            
            return blow
    
    def attack(self, enemigo):
        daño = self.damage(enemigo)
        enemigo.vida = enemigo.vida - daño
        logging.info("%s ha realizado %i puntos de daño a %s", str(self.nombre),  int(daño),  str(enemigo.nombre))
        if enemigo.esta_vivo():
            logging.info("la vida del enemigo es: %s", int(enemigo.vida))
        else:
            enemigo.morir()
  
