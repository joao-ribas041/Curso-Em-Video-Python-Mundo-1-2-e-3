# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.

pMaiores = qtdHomens = mMenores = int(0)

while True:
    print('-'*30)
    print('CADASTRE UMA PESSOA')
    print('-'*30)

    idade = int(input('Idade: '))
    while True:
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if sexo == 'M' or sexo == 'F':
            break
    if idade >= 18:
        pMaiores += 1
    if sexo == 'M':
        qtdHomens += 1
    if sexo == 'F' and idade < 20:
        mMenores += 1

    print('-'*30)
    while True:
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continua == 'N' or continua == 'S':
            break
    if continua == 'N':
        break

print(' FIM ')
print(f'Total de pessoas acima dos 18 anos: {pMaiores}.')
print(f'Total de Homens cadastrados: {qtdHomens}.')
print(f'Mulheres abaixo dos 18: {mMenores}.')
