from domain.campeon import Campeon

class Guerrero(Campeon):

    def __init__(self, nombre, fuerza, defensa, vida, espada):
        super().__init__(nombre, fuerza, defensa, vida)
        self.espada = espada

    def cambiar_objeto(self):
        opcion = int(input("Elige un arma: (1) Espada larga, daño 10. (2) Espada corta, daño 8 "))
        if opcion == 1:
            self.espada = 10
        elif opcion == 2:
            self.espada = 8
        else:
            print("El numero de arma es icorrecto")

    def atributos(self):
        super().atributos()
        print("Espada: ", self.espada)

    def special_hit(self, enemigo):
        return self.fuerza*self.espada - enemigo.defensa


gust = Guerrero("facha", 30, 50, 100, 5)

gust.atributos()
