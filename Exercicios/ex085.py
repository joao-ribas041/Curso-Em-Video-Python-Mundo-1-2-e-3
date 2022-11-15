# Crie um programa onde o usuário posa digitar sete valores numéricos e cadastre-os
# em uma lista única que mantenha separado os valores pares e impares.
# No final, mostre os valores pares e impares em ordem crescente.
numeros = [[], []]


for r in range(1, 8):
    entrada = int(input(f'Digite o {r}o. valor: '))
    if entrada % 2 == 0:
        numeros[0].append(entrada)
    else:
        numeros[1].append(entrada)

numeros[0].sort()
numeros[1].sort()

print(f'Os valores pares são: {numeros[0]}.')
print(f'Os valores impares são: {numeros[1]}.')
