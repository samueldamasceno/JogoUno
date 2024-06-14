import random

class CartaComum():
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor

class CartaEspecial():
    def __init__(self, nome, cor=None):
        self.nome = nome
        self.cor = cor


class Baralho():
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
                carta = CartaEspecial(coringa)
                self.cartas.append(carta)