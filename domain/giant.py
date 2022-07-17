import logging
from campeon import Campeon

logging.basicConfig(filename="logs/TP-OPP", level=logging.INFO)

'''Clase hija que extiende de Campeon'''
class Giant(Campeon):

    # Metodo Constructor
    def __init__(self, nombre, fuerza, defensa, vida, bate):
        self.nombre = nombre
        self.__fuerza = fuerza
        self.__defensa = defensa
        self.__vida = vida
        self.__bate = bate
    
    def __str__(self) -> str:
        return self.nombre  + ": " + str(self.__fuerza) + " " + str(self.__defensa) + " " + str(self.__vida) + " " + str(self.__bate)

    ##GET y SET##
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
    ##GET y SET##
    
    ## Funciones del Personaje ##
    def status(self):
        logging.info( "%s",str(self.nombre))
        logging.info("Fuerza: %s ", str(self.__fuerza))
        logging.info("Defensa: %s ", str(self.__defensa))
        logging.info("Vida: %s", str(self.__vida))
        logging.info("Bate: %s", str(self.__bate))
    
    def esta_vivo(self):
        return self.__vida >= 0

    def morir(self):
        self.__vida = 0
        logging.info(" ha muerto %s", str(self.nombre ))

    def special_move(self):
        opcion = int(input("Elige un movimiento especial: (1)Aplastar-->daño 20, (2)Demoler-->daño 15"))
        if opcion == 1:
           self.__bate = 20
        elif opcion == 2:
            self.__bate = 10
        else:
            logging.info("El numero de movimiento es incorrecto")

    def special_hit(self, enemigo):
        return self.__fuerza*self.__bate - enemigo.__defensa

    def special_attack(self, enemigo):
        specialDamage = self.special_hit(enemigo)
        enemigo.__vida = enemigo.__vida - specialDamage
        logging.info("%s ha realizado %s puntos de daño a %s", str(self.nombre),  str(specialDamage),  str(enemigo.nombre))
        if enemigo.esta_vivo():
            logging.info("la vida del enemigo es: %s", str(enemigo.__vida))
        else:
            enemigo.__morir()

    def damage(self, enemigo):
        return self.__fuerza - enemigo.__defensa

    def attack(self, enemigo):
        damage = self.damage(enemigo)
        enemigo.__vida = enemigo.__vida - damage
        logging.info("%s ha realizado %s puntos de daño a %s", str(self.nombre),  str(damage),  str(enemigo.nombre))
        if enemigo.esta_vivo():
            logging.info("la vida del enemigo es: %s", str(enemigo.__vida))
        else:
            enemigo.__morir()
