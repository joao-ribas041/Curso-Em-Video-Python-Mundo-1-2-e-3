# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

ntupla = (int(input('Digite um numero: ')),
          int(input('Digite outro numero: ')),
          int(input('Digite mais um numero: ')),
          int(input('Digite o ultimo numero: ')))

print()
print('Valores: ')
for c in ntupla:
    print(c, end=' ')

print(f'\nQuantas vezes apareceu o numero 9? {ntupla.count(9)} vezes')
if 3 in ntupla:
    print(f'Posição do primeiro valor 3? {ntupla.index(3)}')
else:
    print('Valor 3 em nenhuma posição.')
print('Numeros Pares: ')
for c in ntupla:
    if c % 2 == 0:
        print(c, end=' ')
