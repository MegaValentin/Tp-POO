import logging

from campeon import Campeon

from gigante import Gigante
from arquero import Arquero
from mago import Mago
from guerrero import Guerrero

class Seleccion:
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

    def seleccionDePersonajeAliado(x):

        if x == 1 :
            campeonA =Seleccion.carta5
            logging.info(Seleccion.carta1.status())
        elif x == 2  :
            campeonA =Seleccion.carta5
            logging.info(Seleccion.carta2.status())
        elif x == 3 :
            campeonA =Seleccion.carta5
            logging.info(Seleccion.carta3.status())
        elif x == 4 :
            campeonA =Seleccion.carta5
            logging.info(Seleccion.carta4.status())
        elif x == 5 :
            campeonA =Seleccion.carta5
            logging.info(Seleccion.carta5.status())
        else: 
            logging.info("Solamente hay 5 campeones para elegir")
        
    def seleccionDePersonajeEnemigo(y):

        if y == 1 :
            campeonE = Seleccion.carta1
            logging.info(Seleccion.carta1.status())
        elif y == 2:
            campeonE =Seleccion.carta2
            logging.info(Seleccion.carta2.status())
        elif y == 3 :
            campeonE =Seleccion.carta3
            logging.info(Seleccion.carta3.status())
        elif y == 4 :
            campeonE =Seleccion.carta4
            logging.info(Seleccion.carta4.status())
        elif y == 5 :
            campeonE =Seleccion.carta5
            logging.info(Seleccion.carta5.status())
        else: 
            logging.info("Solamente hay 5 campeones para elegir")
        

        
