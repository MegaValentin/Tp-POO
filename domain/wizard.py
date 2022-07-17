import logging
from domain.campeon import Campeon

logging.basicConfig(filename="logs/TP-OPP", level=logging.INFO)

'''Clase hija que extiende de Campeon'''
class Wizard(Campeon):

    #Metodo Constructor
    def __init__(self, nombre, fuerza, defensa, vida, libro):
        self.nombre = nombre
        self.__fuerza = fuerza
        self.__defensa = defensa
        self.__vida = vida
        self.__libro = libro
    
    def __str__(self) -> str:
        return self.nombre  + ": " + int(self.__fuerza) + " " + int(self.__defensa) + " " + int(self.__vida) + " " + int(self.__libro)

    ##GET Y SET##   
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
    ## GET y SET##

    ## Funciones del Personaje ##
    def status(self):
        logging.info( "%s",str(self.nombre))
        logging.info("Fuerza: %s ", str(self.__fuerza))
        logging.info("Defensa: %s ", str(self.__defensa))
        logging.info("Vida: %s", str(self.__vida))
        logging.info("Libro: %s", str(self.__libro))

    def esta_vivo(self):
        return self.__vida >= 0

    def morir(self):
        self.__vida = 0
        logging.info(" ha muerto %s", str(self.nombre )) 

    '''Funcion que hace referencia a un ataque especial del personaje'''
    def special_move(self):
        opcion = int(input("Elige un movimiento especial: (1) bolas de fuego, daño 40. (2) Picos de nieve, daño 50 "))
        if opcion == 1:
           self.__libro = 40
        elif opcion == 2:
            self.__libro = 50
        else:
            logging.info("El numero de movimiento es icorrecto")

    def special_hit(self, enemigo):
        return self.__fuerza*self.__libro - enemigo.__defensa

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


