# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = float(0)
menor = float(0)

for c in range(0, 5, 1):
    peso = float(input('Digite o peso pessoa {}: '.format(c)))
    if c == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('Maior peso: {}.'.format(maior))
print('Menor peso: {}.'.format(menor))
