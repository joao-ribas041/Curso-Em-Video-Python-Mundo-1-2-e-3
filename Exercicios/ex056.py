# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo.
# Qual é o nome do homem mais velho.
# Quantas mulheres têm menos de 20 anos.

maior = int(0)
nomemaior = str()
media = float(0)
qtdmulher = int(0)

for c in range(1, 5):
    print('----- {}ª pessoa -----'.format(c))
    nome = str(input('Digite o nome: ')).strip().capitalize()
    idade = int(input('Digite a idade: '))
    print('Selecione')
    print('1 para Masculino')
    print('2 para Feminino')
    sexo = int(input('selecione seu Sexo: '))
    if sexo == 1:
        genero = 'Masculino'
    else:
        genero = 'Feminino'
        if idade < 20:
            qtdmulher += 1
    if genero == 'Masculino' and idade > maior:
        maior = idade
        nomemaior = nome
    media += idade 

media = media / 4
print()
print('MÉDIA DE IDADE: {}'.format(media))
print('Homem Mais velho se chama {} e sua idade é {}'.format(nomemaior, maior))
print('Mulheres abaixo dos 20: {}'.format(qtdmulher))
