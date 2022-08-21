# Refaça o DESAFIO 51, lendo o primeiro termo e a razão da PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

termo = int(input('Digite o termo: '))
razão = int(input('Digite a razão: '))
cont = 1

while cont <= 10:
    print('{}'.format(termo), end='')
    print(' > ' if cont < 10 else '.', end='')
    termo += razão
    cont += 1
