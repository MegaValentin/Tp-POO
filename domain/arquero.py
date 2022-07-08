from campeon import Campeon
import logging

logging.basicConfig(filename="logs/TP-OPP", level=logging.INFO)

class Arquero(Campeon):

    def __init__(self, nombre, fuerza, defensa, vida, arco):
        super().__init__(nombre, fuerza, defensa, vida)
        self.arco = arco

    def get_arco(self):
        return self.arco

    def special_move(self):
        opcion = int(input("Elige un movimiento especial: (1)flechas multiples-->daño 15, (2)Flecha dorada-->daño 10"))
        if opcion == 1:
            self.arco = 15
        elif opcion == 2:
            self.arco = 10
        else:
            logging.info("El numero de moviemiento es incorrecto")

    def atributos(self):
        super().atributos()
        logging.info("Arco: %s", str(self.arco))
    
    def special_hit(self, enemigo):
        return self.fuerza*self.arco - enemigo.defensa
  
x = Arquero("mati", 10, 20, 100, 20)
x.atributos()