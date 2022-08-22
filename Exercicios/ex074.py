# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint, random

randomtupla = (randint(0, 100), randint(0, 100), randint(
    0, 100), randint(0, 100), randint(0, 100))

print('Valores sorteados: ', end='')
for c in randomtupla:
    print(f'{c} ', end='')
print(f'\nO maior valor foi: {max(randomtupla)}')
print(f'O menor valor foi: {min(randomtupla)}')

'''menor = maior = c = int(0)
while c < 5:
    if c == 0:
        menor = randomtupla[c]
        maior = randomtupla[c]
    else:
        if menor > randomtupla[c]:
            menor = randomtupla[c]
        if maior < randomtupla[c]:
            maior = randomtupla[c]
    c += 1

print()
print(f'Numeros ordenado: {sorted(randomtupla)}')
print(f'Maior numero: {maior}')
print(f'Menor numero: {menor}')'''
