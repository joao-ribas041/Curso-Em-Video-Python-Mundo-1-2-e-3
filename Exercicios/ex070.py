# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar. No final, mostre:
# A) Qual é p total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# C) Qual é o nome do produto mais barato.

print('-'*40)
print('LOJA DO PREÇO BAIXO')
print('-'*40)

stotal = pbarato = float(0)
cont = pamil = int(0)
npbarato = str()

while True:
    nome = str(input('Nome do produto: ')).capitalize()
    preço = float(input('Preço: R$'))
    stotal += preço
    cont += 1

    if cont == 1 or preço < pbarato:
        pbarato = preço
        npbarato = nome

    if preço >= 1000:
        pamil += 1

    while True:
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continua == 'S' or continua == 'N':
            break
    if continua == 'N':
        break

print('{:-^40}'.format(' FINALIZADO '))
print(f'O total da compra foi de R${stotal:.2f}')
print(f'{pamil} produtos acima de R$1000.00')
print(f'O produto mais barato foi umª {npbarato} custando R${pbarato}')
