import logging

from campeon import Campeon

from giant import Giant
from archer import Archer
from wizard import Wizard
from warrior import Warrior
class Game:
    card1 =  Warrior("CACHO", 30, 10, 100, 14)
    card2 =  Warrior("GAREN", 20, 2, 100, 16)
    card3 =  Warrior("DARIUS", 25, 5, 100, 15)
    card4 = Wizard("LUX", 30, 25, 100, 20)
    card5 = Wizard("ZYRA", 30, 25, 100, 20)
    card6 = Wizard("NAMI", 30, 25, 100, 20)
    card7 = Archer("ROBIN HOOD", 30, 25, 100, 20)
    card8 = Archer("FACHA", 30, 25, 100, 20)
    card9 = Archer("PUNTITA", 30, 25, 100, 20)
    card10 = Giant("GALIO", 30, 25, 100, 20)
    card11 = Giant("GRAGAS", 30, 25, 100, 20)
    card12 = Giant("TRUNDLE", 30, 25, 100, 20)

    def alliedSelection(x):

        if x == 1 :
            campeonA =Game.card1
            logging.info(Game.card1.status())
        elif x == 2  :
            campeonA =Game.card2
            logging.info(Game.card2.status())
        elif x == 3 :
            campeonA =Game.card3
            logging.info(Game.card3.status())
        elif x == 4 :
            campeonA =Game.card4
            logging.info(Game.card4.status())
        elif x == 5 :
            campeonA =Game.card5
            logging.info(Game.card5.status())
        else: 
            logging.info("Solamente hay 5 campeones para elegir")
        
    def enemySelection(y):

        if y == 1 :
            campeonE = Game.card1
            logging.info(Game.card1.status())
        elif y == 2:
            campeonE =Game.card2
            logging.info(Game.card2.status())
        elif y == 3 :
            campeonE =Game.card3
            logging.info(Game.card3.status())
        elif y == 4 :
            campeonE =Game.card4
            logging.info(Game.card4.status())
        elif y == 5 :
            campeonE =Game.card5
            logging.info(Game.card5.status())
        else: 
            logging.info("Solamente hay 5 campeones para elegir")

    


        
