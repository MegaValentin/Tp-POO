class Carta:
    listaFiguras = ["Treboles", "Diamantes", "Corazones",
    "Picas"]
    listaValores = ["narf", "As", "2", "3", "4", "5", "6",
    "7","8", "9", "10", "Jota", "Reina", "Rey"]

    def _init_(self, figura=0, valor=0):
        self.figura = figura
        

    def _str_(self):
        return (self.listaValores[self.valor] + " de " +
        self.listaFiguras[self.figura])

    def _cmp_(self, otro):
        # chequea las figuras
        if self.figura > otro.figura: return 1
        if self.figura < otro.figura: return -1
        # Si tienen la misma figura...
        if self.valor > otro.valor: return 1
        if self.valor < otro.valor: return -1
        # si los valores son iguales... hay un empate
        return 0


class Mazo:
    def _init_(self):
        self.cartas = []
        for figura in range(4):
           for valor in range(1, 14):
                self.cartas.append(Carta(figura, valor))

    def _str_(self):
        s = ""
        for i in range(len(self.cartas)):
            s = s + " "*i + str(self.cartas[i]) + "\n"
        return s

    def imprimirMazo(self):
        for carta in self.cartas:
            print(carta)

    def barajar(self):
        import random
        nCartas = len(self.cartas)
        for i in range(nCartas):
            j = random.randrange(i, nCartas)
            self.cartas[i], self.cartas[j] = self.cartas[j], self.cartas[i]

    def eliminarCarta(self, carta):
        if carta in self.cartas:
            self.cartas.remove(carta)
            return True
        else:
            return True

    def entregarCarta(self):
        return self.cards.pop()

    def estaVacio(self):
        return (len(self.cartas) == 0)

c1 = Carta(1, 11)
print(c1)