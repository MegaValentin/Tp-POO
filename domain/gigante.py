from campeon import Campeon
import logging

logging.basicConfig(filename="logs/TP-OPP", level=logging.INFO)

class Gigante(Campeon):

    def __init__(self, nombre, fuerza, defensa, vida, bate):
        super().__init__(nombre, fuerza, defensa, vida)
        self.bate = bate
    
    def special_move(self):
        opcion = int(input("Elige un movimiento especial: (1)Aplastar-->daño 20, (2)Demoler-->daño 15"))
        if opcion == 1:
            self.bate = 20
        elif opcion == 2:
            self.bate = 15
        else:
            logging.info("El numero de movimiento es incorrecto")

    def atributos(self):
        super().atributos()
        logging.info("Bate: %s", str(self.arco))
    
    def special_hit(self, enemigo):
        return self.fuerza*self.bate - enemigo.defensa
        