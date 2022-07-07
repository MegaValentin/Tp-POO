from campeon import Campeon
import logging

logging.basicConfig(filename="logs/TP-OPP", level=logging.INFO)

class Mago(Campeon):

    def __init__(self, nombre, fuerza, defensa, vida, libro):
        super().__init__(nombre, fuerza, defensa, vida)
        self.libro = libro

    def atributos(self):
        super().atributos()
        logging.info("Libro: %s", str(self.libro))

    def special_move(self):
        opcion = int(input("Elige un movimiento especial: (1) bolas de fuego, daño 10. (2) Picos de nieve, daño 8 "))
        if opcion == 1:
            self.libro = 10
        elif opcion == 2:
            self.libro = 8
        else:
            logging.info("El numero de movimiento es icorrecto")

    def special_hit(self, enemigo):
        return self.fuerza*self.libro - enemigo.defensa