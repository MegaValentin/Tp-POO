from domain.campeon import Campeon
import logging

logging.basicConfig(filename="logs/TP-OPP", level=logging.INFO)

class Guerrero(Campeon):

    def __init__(self, nombre, fuerza, defensa, vida, espada):
        super().__init__(nombre, fuerza, defensa, vida)
        self.espada = espada

    def special_move(self):
        opcion = int(input("Elige un movimiento especial: (1) Golpe duro, daño 10. (2) Corte, daño 8 "))
        if opcion == 1:
            self.espada = 10
        elif opcion == 2:
            self.espada = 8
        else:
            logging.info("El numero de movimiento es icorrecto")

    def atributos(self):
        super().atributos()
        logging.info("Espada: %s", str(self.espada))

    def special_hit(self, enemigo):
        return self.fuerza*self.espada - enemigo.defensa


