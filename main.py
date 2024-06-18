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

def exibir_cartas(cartas):
    print("Essas são suas cartas:")
    i = 1
    for carta in cartas:
        print(f"{i}. {carta.nome}")
        i += 1
    print()

def jogada_jogador(cartas_jogador):
    print("Qual carta você vai jogar? (Digite o número da lista em que ele está)")
    carta_jogada = input()
    verificar_opcao(carta_jogada, cartas_jogador)

def jogada_computador(cartas_computador):


def verificar_opcao(carta_jogada, cartas_jogador):
    while True:
        if carta_jogada.isnumeric():
            carta_jogada = int(carta_jogada)
            if carta_jogada > 0 and carta_jogada <= len(cartas_jogador):
                carta_jogada = cartas_jogador[carta_jogada - 1]
                break
            else:
                print("Opção inválida!")
                print()
        else:
            print("Opção inválida!")
            print()

def jogo():
    baralho = Baralho()
    cartas_jogador = baralho.distribuirCartas()
    cartas_computador = baralho.distribuirCartas()
    exibir_cartas(cartas_jogador)
    digite_enter()

    carta_topo = baralho.primeiraCarta()
    print(f"A carta inicial é um {carta_topo.nome}")
    digite_enter()

    jogador_atual = "Jogador"
    print("Vamos lá! Você começa")

    while len(cartas_jogador) > 0 and len(cartas_computador) > 0:
        if jogador_atual == "Jogador":
            exibir_cartas(cartas_jogador)
            jogada_jogador(cartas_jogador)
            jogador_atual = "Computador"
        
        if jogador_atual == "Computador":
            jogada_computador(cartas_computador)


def digite_enter():
    input("Digite ENTER para continuar.")
    print()

while True:
    bem_vindo()
    jogo()
    print()
    print("""Deseja jogar novamente?
          1. Sim
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