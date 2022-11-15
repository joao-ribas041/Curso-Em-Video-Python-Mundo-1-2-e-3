# Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, Mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
cadastro = []
dados = []
maior = menor = 0
cont = 0

while True:
    cadastro.append(str(input('Digite o nome: ')))
    cadastro.append(float(input('Digite o peso: ')))
    if len(dados) == 0:
        maior = menor = cadastro[1]
    else:
        if maior > cadastro[1]:
            menor = cadastro[1]
        else:
            maior = cadastro[1]

    dados.append(cadastro[:])
    cadastro.clear()
    cont += 1

    continua = str(input('Deseja continuar? [S/N]: '))
    if continua in 'Nn':
        break

print(f'\nForam cadastrado {cont} pessoas.')
print(f'O maior peso foi {maior}kg de: ')
for dado in dados:
    if dado[1] == maior:
        print(f'[{dado[0]}] ', end='')

print(f'\nO menor peso foi {menor}kg de: ')
for dado in dados:
    if dado[1] == menor:
        print(f'[{dado[1]}] ', end='')
