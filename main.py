from cartas import Baralho, CartaComum, CartaEspecial, CartaCoringa
import random

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
    print("""
    Regras do Uno:
    
    - O objetivo do jogo é ser o primeiro jogador a se livrar de todas as suas cartas.
    - Cada jogador deve jogar uma carta que tenha a mesma cor ou número da carta no topo.
    - Se o jogador não puder jogar, ele deve comprar uma carta do baralho.
    
          
    Cartas Especiais:
    - +2: O próximo jogador compra duas cartas e perde a vez.
    - Bloqueio: O próximo jogador perde a vez.
    - Inverter: Inverte a direção do jogo.
    - Coringa: O jogador escolhe uma nova cor.
    - +4: O jogador escolhe uma nova cor e o próximo jogador compra quatro cartas e perde a vez.
    
    
    Pronto?
    """)


def exibir_cartas(cartas):
    print("Essas são suas cartas:")
    i = 1
    for carta in cartas:
        print(f"{i}. {carta.nome}")
        i += 1
    print()

def jogada_jogador(cartas_jogador, topo, baralho):
    while True:
        print("Qual carta você vai jogar? (Digite o número da lista ou a letra C para comprar uma carta)")
        carta_jogada = input()
        
        if carta_jogada.upper() == "C":
            carta_nova = baralho.comprarCarta(1)
            cartas_jogador.extend(carta_nova)
            print("Você comprou: " + carta_nova[0].nome)
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
            print(f"O computador jogou a carta {carta.nome}, ficando com {len(cartas_computador)} cartas.")
            return carta
    cartas_computador.extend(baralho.comprarCarta(1))
    print(f"O computador comprou uma carta. Agora ele está com {len(cartas_computador)} cartas.")
    return topo

def jogada_valida(carta, topo):
    if isinstance(carta, CartaCoringa):
        return True
    elif isinstance(topo, CartaCoringa):
        return True
    elif isinstance(carta, CartaComum) and isinstance(topo, CartaComum):
        return carta.numero == topo.numero or carta.cor == topo.cor
    elif isinstance(carta, CartaEspecial) and isinstance(topo, CartaEspecial):
        return carta.tipo == topo.tipo or carta.cor == topo.cor
    elif isinstance(carta, CartaEspecial) and isinstance(topo, CartaComum):
        return carta.cor == topo.cor
    elif isinstance(carta, CartaComum) and isinstance(topo, CartaEspecial):
        return carta.cor == topo.cor
    return False

def aplicar_efeito(carta, jogador_atual, cartas_jogador, cartas_computador, baralho):
    if isinstance(carta, CartaComum):
        return False
    elif isinstance(carta, CartaEspecial):
        if carta.tipo == "+2":
            if jogador_atual == "Jogador":
                print("O computador comprou 2 cartas")
                cartas_computador.extend(baralho.comprarCarta(2))
                print(f"O computador está com {len(cartas_computador)} cartas.")
            else:
                print("Você comprou duas cartas:")
                cartas_compradas = baralho.comprarCarta(2)
                cartas_jogador.extend(cartas_compradas)
                for carta in cartas_compradas:
                    print(f"- {carta.nome}")
                print(f"Agora você está com {len(cartas_jogador)} cartas.")
            return True
        elif carta.tipo == "Bloqueio":
            if jogador_atual == "Jogador":
                print("O computador foi bloqueado.")
            else:
                print("Você está bloqueado.")
            return True
        elif carta.tipo == "Inverter":
            print("A direção da partida mudou, mas como só tem dois jogadores isso não faz diferença.")
            return False
    elif isinstance(carta, CartaCoringa):
        if carta.nome == "+4":
            if jogador_atual == "Jogador":
                print("O computador comprou 4 cartas")
                cartas_computador.extend(baralho.comprarCarta(4))
                print(f"O computador agora está com {len(cartas_computador)} cartas.")
            else:
                print("Você comprou quatro cartas:")
                cartas_compradas = baralho.comprarCarta(4)
                cartas_jogador.extend(cartas_compradas)
                for carta in cartas_compradas:
                    print(f"- {carta.nome}")
                print(f"Você agora está com {len(cartas_jogador)} cartas.")
            cor = escolher_cor(jogador_atual, cartas_computador)
            carta.cor = cor
            return True 
        elif carta.nome == "Coringa":
            cor = escolher_cor()
            carta.cor = cor
            return False

def escolher_cor(jogador, cartas_computador):
    cores = ["Vermelho", "Azul", "Verde", "Amarelo"]
    if jogador == "Jogador":
        print("""Escolha uma cor:
            1. Vermelho
            2. Azul
            3. Verde
            4. Amarelo""")
        while True:
            opcao = input()
            if opcao in ["1", "2", "3", "4"]:
                cor = cores[int(opcao) - 1]
                print(f"Você escolheu a cor {cor}")
                return cor
            else:
                print("Opção inválida!")
    else:
        for carta in cartas_computador:
            if isinstance(carta, (CartaComum, CartaEspecial)):
                cor = carta.cor
                print(f"O computador escolheu a cor {cor}")
                return cor
        cor = random.choice(cores)
        print(f"O computador escolheu a cor {cor}")
        return cor

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
            bloqueado = aplicar_efeito(topo, jogador_atual, cartas_jogador, cartas_computador, baralho)
            if bloqueado:
                jogador_atual = "Jogador"
            else:
                jogador_atual = "Computador"
        else:
            topo = jogada_computador(cartas_computador, topo, baralho)
            bloqueado = aplicar_efeito(topo, jogador_atual, cartas_jogador, cartas_computador, baralho)
            if bloqueado:
                jogador_atual = "Computador"
            else:
                jogador_atual = "Jogador"
        digite_enter()

    if len(cartas_jogador) == 0:
        print("Você ganhou!")
    else:
        print("Você perdeu!")

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
