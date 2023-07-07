import time

meu_tempo = int(input('Digite o tempo em segundos: '))

for x in range(meu_tempo, 0, -1):
    segundos = x % 60
    minutos = int(x / 60) % 60
    # % para pegar o resto da divisão para limitar a quantidade de minutos em 60
    horas = int(x / 3600)
    print(f'{horas:02}:{minutos:02}:{segundos:02}')
    # :02 para limitar a mostragem em duas casas precedido de 0
    time.sleep(1)

print('Tempo esgotado!')