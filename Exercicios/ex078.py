# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior valor e o menor valor digitado e
# as suas respectivas posiçoes na lista.

lista = list()
posMaior = list()
posMenor = list()
maior = menor = cont = 0
for r in range(0, 5):
    lista.append(float(input(f'Digite um valor para posição {r}: ')))

# maior = max(lista)
# menor = min(lista)

for c, l in enumerate(lista):
    if c == 0:
        maior = menor = l
    else:
        if maior < l:
            maior = l
        if menor > l:
            menor = l

for p, l in enumerate(lista):
    if maior == l:
        posMaior.append(p)
    if menor == l:
        posMenor.append(p)
    p += 1

print('')
print(f'Maior valor {maior} na posição {posMaior}.')
print(f'menor valor: {menor} na posição {posMenor}.')
