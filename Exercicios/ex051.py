# Desenvolva um programa que leia o primeiro termo e a razão de um PA. No final, mostre os 10 primeiros termos dessa progressão.

n1 = int(input('Primeiro termo: '))
n2 = int(input('Digite a razão: '))
cont = 0
décimo = n1 + (10 - 1) * n2
for i in range(n1, décimo + n2, n2):
    print(i, end=' ')
