# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

numeros = []

while True:
    numeros.append(int(input('Digite um valor: ')))
    opc = str(input('Quer Continuar? [S/N] '))
    if opc in 'Nn':
        break
print('-'*15)
print(f'Você Digitou {len(numeros)} numeros.')
numeros.sort()
print(f'Valores ordenados: {numeros}')

if 5 in numeros:
    print('O valor 5 está na lista.')
else:
    print('O valor 5 não está na lista')
