# Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.

from math import sin, cos, tan, radians

num = float(input('Digite um valor qualquer: '))
seno = sin(radians(num))
cosseno = cos(radians(num))
tangente = tan(radians(num))

print('o Seno de {} é igual a {:.2f}'.format(num, seno))
print('O Cosseno de {} é igual a {:.2f}'.format(num, cosseno))
print('A tangente de {} é igual a {:.2f}'.format(num, tangente))
