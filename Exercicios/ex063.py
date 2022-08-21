# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequencia de Fibonacci.
# Ex:
# 0 > 1 > 1 > 2 > 3 > 5 > 8

elementos = int(input('Quantos termos você quer ver? '))
n = 0
n1 = 1
n2 = 0

print('{} > {}'.format(n, n1), end='')
while elementos-1 != 1:
    n2 = n + n1
    print(' > {}'.format(n2), end='')
    n = n1
    n1 = n2
    elementos -= 1
print(' > FIM')
