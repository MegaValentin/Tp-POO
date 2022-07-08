#Misma elavoracion de la clase Personajes pero sin modificadores de accesos
#Todos los atributos y metodos son unicos
#Clase padre
from abc import abstractclassmethod,ABC
import logging
logging.basicConfig(filename="logs/TP-OPP", level=logging.INFO)

'''Clase padre, que contiene los atributos y metodos basicos que heredan los personajes'''
@abstractclassmethod
class Campeon(ABC):
    nombre = "Default"
    fuerza = 0
    defensa = 0
    vida = 0
    
    #Self hace referencia a si mismo
    def __init__(self, nombre, fuerza, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.defensa = defensa
        self.vida = vida
#status
    def status(self):
        logging.info(self.nombre)
        logging.info("Fuerza: %s ", self.fuerza)
        logging.info("Defensa: %s ", self.defensa)
        logging.info("Vida: %s", self.vida)

    def __str__(self) -> str:
        return self.nombre  + ": " + str(self.fuerza) + " " + str(self.defensa) + " " + str(self.vida)

    def subir_nivel(self, fuerza, defensa):
        self.fuerza = self.fuerza + fuerza
        self.defensa = self.defensa + defensa

    def esta_vivo(self):
        return self.vida >= 0

    def morir(self):
        self.vida = 0
        logging.info(" ha muerto %s", str(self.nombre ))
    
    def damage(self, enemigo):
        blow = self.fuerza - enemigo.defensa
        if blow < 0 :
            blow = 0
            logging.info("null blow")
            
            return blow

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        logging.info("%s ha realizado %i puntos de daño a %s", str(self.nombre),  int(daño),  str(enemigo.nombre))
        if enemigo.esta_vivo():
            logging.info("la vida del enemigo es: %s", int(enemigo.vida))
        else:
            enemigo.morir()


 