# Pedido lanchonete

comidas = []
preços = []
total = 0

while True:
    comida = input('Digite o lanche ou bebida que deseja comprar (aperte S para sair) : ')
    if comida.upper() == 'S':
        break
    else:
        preço = float(input(f'Digite o preço do(a) {comida}: R$ '))
        comidas.append(comida)
        preços.append(preço)

print('----- SEU PEDIDO -----')

for comida in comidas:
    print(comida, end=' ')
for preço in preços:
    total += preço

print()
print(f'O total a ser pago pelo seu pedido é: R${total:.2f} ')