# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
linha = '~' * 40


def maior(*valores):
    print(linha)
    print('Analisando...')
    for v in valores:
        print(v, end=' ')
    print(f'Foram informado {len(valores)} valores.')
    maior = 0
    for i, valor in enumerate(valores):
        if i == 0:
            maior = valor
        else:
            if maior < valor:
                maior = valor
    print(f'O maior valor foi: {maior}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
