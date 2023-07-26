import random

opcoes = ('pedra', 'papel', 'tesoura')
repetir = True

while repetir:
    # Isso é o mesmo que while repetir == True. É apenas uma forma abreviada.

    jogador = None
    computador = random.choice(opcoes)

    while jogador not in opcoes:
        # Enquanto a escolha do jogador não estiver contida em "opcoes", continue
        # o loop para sempre.
        jogador = str(input('Escolha a sua jogada (pedra, papel ou tesoura): '))

    print(f'Jogador: {jogador} ')
    print(f'Computador: {computador} ')

    if jogador == computador:
        print('EMPATE! ')
    elif jogador == 'papel' and computador == 'pedra':
        print('Você venceu! ')
    elif jogador == 'pedra' and computador == 'tesoura':
        print('Você venceu! ')
    elif jogador == 'tesoura' and computador == 'papel':
        print('Você venceu! ')
    else:
        print('O computador venceu!')

    if not str(input('Jogar novamente? (s/n)')).lower() == 's':
        # Se o jogador escolher não jogar novamente altere repetir para falso.
        repetir = False

print('Obrigado por jogar! ')
