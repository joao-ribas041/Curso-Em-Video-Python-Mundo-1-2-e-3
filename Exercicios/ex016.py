# Crie um programa que leia um numero Real qualquer pelo teclado e mostre na tela a sua porção inteira.
# EX: Digite um numero: 6.127 (O numero 6.127 tem a parte inteira 6).

from math import trunc
n = float(input('Digite um valor: '))
print('O numero {} tem a parte inteira {}'.format(n, trunc(n)))
