from domain.guerrero import Guerrero
from domain.mago import Mago

personaje_1 = Guerrero("Garen", 10, 3, 100, 10)
personaje_2 = Mago("Lux", 5, 3, 100, 20)

def combate(jugador_1, jugador_2):
    turno = 0
    while jugador_1.esta_vivo() and jugador_2.esta_vivo:
        print("\n Turno:", turno)
        print(">>> Accion de ", jugador_1.nombre, ":", sep="")
        jugador_1.atacar(jugador_2)
        print(">>> Accion de ", jugador_2.nombre, ":", sep="")
        jugador_2.atacar(jugador_1)
        turno +=1

    if jugador_1.vida == 0:
        print("\nHa ganado", jugador_2.nombre)
    elif jugador_2.vida == 0:
        print("\nHa ganado", jugador_1.nombre)
    else:
        print("\nEmpate")

combate(personaje_1, personaje_2)