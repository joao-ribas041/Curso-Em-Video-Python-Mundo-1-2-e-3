# Crie um programa que leia dois valores e mostre um menu na tela:
# [1]somar
# [2]multiplicar
# [3]maior
# [4]novos números
# [5]sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso

from random import randint
from time import sleep

n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro numero: '))

opção = int(0)

while opção != 5:
    print()
    print('''------- Escolha -------
    [1] - Somar
    [2] - Multiplicar
    [3] - Maior
    [4] - Novos numeros
    [5] - Sair do programa''')
    opção = int(input('Digite um numero: '))

    if opção == 1:
        print()
        print('------- Soma -------')
        print('A soma de {} com {} é igual a: {}.'.format(n1, n2, n1+n2))
        sleep(3)

    if opção == 2:
        print()
        print('---- Multiplicação ----')
        print('A multiplicação de {} vezes {} é igual a: {}.'.format(n1, n2, n1*n2))
        sleep(3)

    if opção == 3:
        print()
        print('----- Maior -----')
        maior = 0
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior numero entre {} e {} é: {}.'.format(n1, n2, maior))
        sleep(3)

    if opção == 4:
        print()
        print('----- Digite novos numeros. -----')
        n1 = int(input('Digite um numero: '))
        n2 = int(input('Digite outro numero: '))
        sleep(1)

print('fim')
