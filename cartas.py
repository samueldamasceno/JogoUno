import random

class CartaComum():
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor

class CartaEspecial():
    def __init__(self, nome, efeito):
        self.nome = nome
        self.efeito = efeito


class Baralho():
    def __init__(self):
        numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        cores = ["Vermelho", "Azul", "Verde", "Amarelo"]
        cartasEspeciais = ["+2", "+4", "Coringa", "Inverter", "Bloqueio"]
        self.cartas = []
        for cor in cores:
            for numero in numeros:
                carta = CartaComum(numero, cor)
                self.cartas.append(carta)