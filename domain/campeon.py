#Misma elavoracion de la clase Personajes pero sin modificadores de accesos
#Todos los atributos y metodos son unicos
#Clase padre

class Campeon:

    nombre = "Default"
    fuerza = 0
    defensa = 0
    vida = 0
    
    #Self hace referencia a si mismo
    def __init__(self, nombre, fuerza, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        print(self.nombre, ":", sep = "")
        print("Fuerza:", self.fuerza)
        print("Defensa:", self.defensa)
        print("Vida:", self.vida)

    def __str__(self) -> str:
        return self.nombre  + ": " + str(self.fuerza) + " " + str(self.defensa) + " " + str(self.vida)

    def subir_nivel(self, fuerza, defensa):
        self.fuerza = self.fuerza + fuerza
        self.defensa = self.defensa + defensa

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")
    
    def daño(self, enemigo):
        return  self.fuerza - enemigo.defensa

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a ", enemigo.nombre)
        if enemigo.esta_vivo():
            print("la vida de ", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()

    
 