linhas = int(input('Digite o número de linhas: '))
colunas = int(input('Digite o número de colunas: '))
símbolo = input('Digite um símbolo: ')

for x in range(linhas):
    for y in range(colunas):
        print(símbolo, end='')
    print()