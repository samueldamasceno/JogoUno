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

def jogada_computador(cartas_computador):
    print("")

def jogada_jogador(cartas_jogador, topo, baralho):
    while True:
        print("Qual carta você vai jogar? (Digite o número da lista ou a letra C para comprar uma carta)")
        carta_jogada = input()
        
        if carta_jogada.upper() == "C":
            cartas_jogador.extend(baralho.comprarCarta(1))
            return topo
        elif carta_jogada.isnumeric():
            carta_jogada = int(carta_jogada)
            if carta_jogada > 0 and carta_jogada <= len(cartas_jogador):
                carta_selecionada = cartas_jogador[carta_jogada - 1]
                if jogada_valida(carta_selecionada, topo):
                    cartas_jogador.remove(carta_selecionada)
                    return carta_selecionada
                else:
                    print("Você não pode jogar essa carta!")
            else:
                print("Esse número não está entre as opções")
        else:
            print("Opção inválida! Digite um número ou 'C' para comprar uma carta.")

def jogada_computador(cartas_computador, topo, baralho):
    for carta in cartas_computador:
        if jogada_valida(carta, topo):
            cartas_computador.remove(carta)
            return carta
    cartas_computador.extend(baralho.comprarCarta(1))
    return topo

def jogada_valida(carta, topo):
    if carta.numero == topo.numero or carta.cor == topo.cor:
        return True
    else:
        return False

def jogo():
    baralho = Baralho()
    cartas_jogador = baralho.distribuirCartas()
    cartas_computador = baralho.distribuirCartas()
    exibir_cartas(cartas_jogador)
    digite_enter()

    topo = baralho.primeiraCarta()
    print(f"A carta inicial é um {topo.nome}")
    digite_enter()

    jogador_atual = "Jogador"
    print("Vamos lá! Você começa")

    while len(cartas_jogador) > 0 and len(cartas_computador) > 0:
        if jogador_atual == "Jogador":
            exibir_cartas(cartas_jogador)
            topo = jogada_jogador(cartas_jogador, topo, baralho)
            jogador_atual = "Computador"
        else:
            topo = jogada_computador(cartas_computador, topo, baralho)
            jogador_atual = "Jogador"
        digite_enter()


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