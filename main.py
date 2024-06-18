from cartas import Baralho

def bem_vindo():
    print("Vamos jogar Uno?")
    print()
    print("""Você conhece as regras?
          1. Sim
          2. Não""")
    opcao = input()
    while True:
        if opcao == "1":
            print("Vamos lá!")
            print()
            break
        elif opcao == "2":
            regras()
            print()
            break
        else:
            print("Opção inválida!")
            print()

def regras():
    print("a")

def jogo():
    baralho = Baralho()

while True:
    bem_vindo()
    jogo()
    print()
    print("Deseja jogar novamente?")
    print("""1. Sim
         2. Não""")
    opcao = input()
    while True:
        if opcao == "1":
            print()
            break
        elif opcao == "2":
            print("Obrigado por ter jogado!")
            print()
            exit()
        else:
            print("Opção inválida!")
            print()