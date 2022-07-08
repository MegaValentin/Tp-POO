
import logging
logging.basicConfig(filename="logs/TP-OPP", level=logging.INFO)
class Personaje:

    nombre = "Default"
    fuerza = 0
    defensa = 0
    vida = 0
    
    #Self hace referencia a si mismo
    def __init__(self, nombre, fuerza, defensa, vida):
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__defensa = defensa
        self.__vida = vida

    def atributos(self):
        #cambiar print para probar en pantalla
        logging.info(self.nombre)
        logging.info("Fuerza: %s ", self.fuerza)
        logging.info("Defensa: %s ", self.defensa)
        logging.info("Vida: %s", self.vida)

    def subir_nivel(self, fuerza, defensa):
        self.__fuerza = self.__fuerza + fuerza
        self.__defensa = self.__defensa + defensa

    def esta_vivo(self):
        return self.__vida > 0

    def morir(self):
        self.__vida = 0
        print(self.__nombre, "esta murido")
    
    def daño(self, enemigo):
        return  self.__fuerza - enemigo.__defensa 

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.__vida = enemigo.__vida - daño
        print(self.__nombre, "ha realizado", daño, "puntos de daño", enemigo.__nombre)
        if enemigo.esta_vivo():
            print("la vida de ", enemigo.__nombre, "es", enemigo.__vida)
        else:
            enemigo.__morir()

    def get_fuerza(self):
        return self.__fuerza

    def set_fuerza(self, fuerza):
        if fuerza < 0:
            print("Error al ingresar un numero negativos")
        else:
            self.__fuerza = fuerza

    def get_defensa(self):
        return self.__defensa

    def get_vida(self):
        return self.__vida


mi_personaje = Personaje("mega", 10, 20, 100)

mi_personaje.set_fuerza(-30)
print(mi_personaje.atributos())

