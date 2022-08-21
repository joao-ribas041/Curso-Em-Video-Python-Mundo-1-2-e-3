# Faça um programa que calcule a soma entre todos os números impares que sao multiplos de três e que se encontram no intervalo de 1 até 500.

s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        s += c
print('')
print('A soma de todos os {} valores'.format(cont))
print('Soma dos impares: {}.'.format(s))
print('FIM')
