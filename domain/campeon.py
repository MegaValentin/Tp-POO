#Misma elavoracion de la clase Personajes pero sin modificadores de accesos
#Todos los atributos y metodos son unicos
#Clase padre
from abc import abstractclassmethod,ABC
import logging
logging.basicConfig(filename="logs/TP-OPP", level=logging.INFO)

'''Clase padre, que contiene los atributos y metodos basicos que heredan los personajes'''

class Campeon(ABC):
    
    @abstractclassmethod
    def status(self):
        """puntos de vida, defensa, daño, objeto especial."""
        pass

    @abstractclassmethod  
    def esta_vivo(self):
        pass

    @abstractclassmethod
    def morir(self):
        """0 de vida"""
        pass
    
    @abstractclassmethod
    def special_move(self):
        pass

    @abstractclassmethod
    def special_hit(self):
        pass

    @abstractclassmethod
    def damage(self):
        """Daño hacia el enemigo"""
        pass
    
    def attack(self):
        pass


 