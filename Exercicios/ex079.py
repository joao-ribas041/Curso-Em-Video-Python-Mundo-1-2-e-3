# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os
# em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados em ordem crescente.

from operator import index


lista = list()
x = int()

while True:
    x = input('Digite um valor: ')
    if lista.count(x) == 0:
        lista.append(x)
    else:
        print('Valor ja existe.')

    while True:
        continua = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
        if continua in "SN":
            break
    print()
    if continua == "N":
        break
print('-='*10)
lista.sort()
print(f'Você digitou os valores {lista}')
