# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostra quantos dolares ela pode comprar
# Considere
# US$ 1,00 = R$ 3,27

dolar = float(5.19)
print('US$'.format(dolar))
carteira = float(input('Digite o valor que voce tem na carteira: '))
total = carteira/dolar
print(total)
