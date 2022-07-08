import logging
from controller.cartas import Cartas

logging.basicConfig(filename="logs/TP-OPP", level=logging.INFO)

class Mazo(Cartas):
    
    def __init__(self, campeones, numerosCartas):
        self.cartas = []
        for campeones in range(12):

            
