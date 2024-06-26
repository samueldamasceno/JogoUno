import random

class CartaComum:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.nome = f"{numero} {cor}"

class CartaEspecial:
    def __init__(self, tipo, cor):
        self.tipo = tipo
        self.cor = cor
        self.nome = f"{tipo} {cor}"

class CartaCoringa:
    def __init__(self, nome):
        self.nome = nome
    

class Baralho:
    def __init__(self):
        self.cartas = []

        numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        cores = ["Vermelho", "Azul", "Verde", "Amarelo"]
        cartasEspeciais = ["+2", "Inverter", "Bloqueio"]
        coringas = ["+4", "Coringa"]

        for cor in cores:
            for numero in numeros:
                carta = CartaComum(numero, cor)
                self.cartas.append(carta)
            for cartaEspecial in cartasEspeciais:
                for i in range(2):
                    carta = CartaEspecial(cartaEspecial, cor)
                    self.cartas.append(carta)
        for coringa in coringas:
            for i in range(4):
                carta = CartaCoringa(coringa)
                self.cartas.append(carta)
    
    def embaralhar(self):
        random.shuffle(self.cartas)

    def primeiraCarta(self):
        while True:
            carta = self.cartas.pop(0)
            if isinstance(carta, CartaComum):
                return carta
            else:
                self.cartas.append(carta)

    def distribuirCartas(self):
        self.embaralhar()
        cartas_distribuidas = []
        for i in range(7):
            cartas_distribuidas.append(self.cartas.pop(0))
        return cartas_distribuidas

    def comprarCarta(self, quantidade):
        if quantidade > len(self.cartas):
            return []
        cartas_compradas = []
        for i in range(quantidade):
            cartas_compradas.append(self.cartas.pop(0))
        return cartas_compradas;
