# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n1 = int(input('Digite um valor: '))
contador = 0

if n1 <= 1:
    print('{} NÃO É PRIMO'.format(n1))
else:
    for i in range(1, n1+1):
        if n1 % i == 0:
            contador += 1

    if contador == 2:
        print('{} É PRIMO'.format(n1))
    else:
        print('{} NÃO É PRIMO'.format(n1))
