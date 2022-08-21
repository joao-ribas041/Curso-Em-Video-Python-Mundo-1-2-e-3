# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
print('')

if n1 > n2:
    print('Maior: {}.'.format(n1))
    print('Menor: {}.'.format(n2))
elif n2 > n1:
    print('Maior: {}.'.format(n2))
    print('Menor: {}.'.format(n1))
else:
    print('O numero {} e {} são iguais respectivamente'.format(n1, n2))
