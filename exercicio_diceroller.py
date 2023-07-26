import random

# Abaixo os unicodes necessários para montar os dados.
# print('\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518')
# ● ┌ ─ ┐ │ └ ┘
# Abaixo o dado montado:
# '┌─────────┐'
# '│         │'
# '│         │'
# '│         │'
# '└─────────┘'

arte_dado = {
    1: ('┌─────────┐',
        '│         │',
        '│    ●    │',
        '│         │',
        '└─────────┘'),
    2: ('┌─────────┐',
        '│  ●      │',
        '│         │',
        '│      ●  │',
        '└─────────┘'),
    3: ('┌─────────┐',
        '│  ●      │',
        '│    ●    │',
        '│      ●  │',
        '└─────────┘'),
    4: ('┌─────────┐',
        '│  ●   ●  │',
        '│         │',
        '│  ●   ●  │',
        '└─────────┘'),
    5: ('┌─────────┐',
        '│  ●   ●  │',
        '│    ●    │',
        '│  ●   ●  │',
        '└─────────┘'),
    6: ('┌─────────┐',
        '│  ●   ●  │',
        '│  ●   ●  │',
        '│  ●   ●  │',
        '└─────────┘'),

}

dados = []
total = 0
numero_de_dados = int(input('Quantos dados deseja rolar? '))

# O loop abaixo adiciona os valores aleatórios a lista dados.
for dado in range(numero_de_dados):
    dados.append(random.randint(1, 6))

# O loop a seguir imprime os dados um abaixo do outro:
# for dado in range(numero_de_dados):
#    for linha in arte_dado.get(dados[dado]):
#        print(linha)

# O loop a seguir imprime os dados um ao lado do outro:
for line in range(5):
    for dado in dados:
        print(arte_dado.get(dado)[line], end='')
    print()

# Loop para a soma dos valores aleatórios.
for dado in dados:
    total += dado
print(f'Soma dos valores: {total} ')
