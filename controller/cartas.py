import logging

from domains.arquero import Arquero
from domains.guerrero import Guerrero
from domains.mago import Mago
from domains.gigante import Gigante

logging.basicConfig(filename="logs/TP-OPP", level=logging.INFO)

class Cartas:
    carta1 = Guerrero("CACHO", 30, 10, 100, 14)
    carta2 = Guerrero("GAREN", 20, 2, 100, 16)
    carta3 = Guerrero("DARIUS", 25, 5, 100, 15)
    carta4 = Mago("LUX", 30, 25, 100, 20)
    carta5 = Mago("ZYRA", 30, 25, 100, 20)
    carta6 = Mago("NAMI", 30, 25, 100, 20)
    carta7 = Arquero("ROBIN HOOD", 30, 25, 100, 20)
    carta8 = Arquero("FACHA", 30, 25, 100, 20)
    carta9 = Arquero("PUNTITA", 30, 25, 100, 20)
    carta10 = Gigante("GALIO", 30, 25, 100, 20)
    carta11 = Gigante("GRAGAS", 30, 25, 100, 20)
    carta12 = Gigante("TRUNDLE", 30, 25, 100, 20)

    listaCampeones = [carta1, carta2, carta3, carta4, carta5,
    carta6, carta7, carta8, carta9, carta10, carta11, carta12]
    

    def __init__(self, campeones = 0) :
        self.campeones = campeones
        

    def __str__(self):
        return (self.listaCampeones[self.campeones])
    
    def cartas(self):
        logging.info(self.campeones)
