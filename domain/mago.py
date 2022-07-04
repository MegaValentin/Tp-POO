from domain.campeon import Campeon

class Mago(Campeon):

    def __init__(self, nombre, fuerza, defensa, vida, libro):
        super().__init__(nombre, fuerza, defensa, vida)
        self.libro = libro

    def atributos(self):
        super().atributos()
        print("Libro: ", self.libro)

    def cambiar_objeto(self):
        opcion = int(input("Elige un libro: (1) Libro oscuro, daño 10. (2) Libro de los mares, daño 8 "))
        if opcion == 1:
            self.libro = 10
        elif opcion == 2:
            self.libro = 8
        else:
            print("El numero de librp es icorrecto")

    def golpe_objeto(self, enemigo):
        return self.fuerza*self.libro - enemigo.defensa