# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

maior = 0
menor = 0
ano = date.today().year

for c in range(0, 7, 1):
    nasc = int(input('Digite o ano de nascimento {}: '.format(c)))
    if ano - nasc >= 21:
        maior += 1
    else:
        menor += 1

print('{} pessoas são maiores de idade.'.format(maior))
print('{} pessoas são menores de idade.'.format(menor))
