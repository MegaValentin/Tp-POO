import logging
from controller.cartas import Cartas

logging.basicConfig(filename="logs/TP-OPP", level=logging.INFO)

class Mazo(Cartas):
    
    campeones = Cartas.listaCampeones

    def __init__(self):
        self.cartas = []
        for campeones in range(12):
            


            
