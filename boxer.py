from pyparsing import tokenMap
from slapped import Slapped

class Boxer(Slapped):
    vida = 10
    def __int__(self,toma):
        self.toma = toma

    def getToma(self):
        return self.toma

    def blow(self,vida):
       vida -=1
    blow(vida)