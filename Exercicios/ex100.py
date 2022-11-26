# Faça um programa que tenha uma lista chamada números é duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro de uma lista e a segunda função
# vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.

def sorteia(lista):
    from random import randint

    print('Sorteando os valores:', end=' ')
    for i in range(5):
        sort = randint(1, 10)
        lista.append(sort)
        print(sort, end=' ')
    print()


def somaPar(lst):
    soma = 0

    for v in lst:
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares de {lst}, temos {soma}')


valores = []
sorteia(valores)
somaPar(valores)
