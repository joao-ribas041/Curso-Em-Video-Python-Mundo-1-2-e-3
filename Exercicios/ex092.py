# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade) em um dicionário se por acaso o CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date

cadastro = {}
ano_atual = date.today().year
aposentadoria = 35

cadastro['nome'] = str(input('Digite o nome: '))
ano = int(input('Digite o ano de nascimento: '))
cadastro['idade'] = ano_atual - ano
cadastro['ctps'] = int(
    input('Carteira de trabalho (0 - não tem): '))

if cadastro['ctps'] == 0:
    print('-'*30)
    print(cadastro)
    for k, v in cadastro.items():
        print(f'{k} tem o valor {v}')
else:
    cadastro['ano-contratacao'] = int(input('Ano de contratação: '))
    cadastro['salario'] = float(input('Salario contratação: R$ '))
    cadastro['aposentadoria'] = (
        cadastro['ano-contratacao'] - ano) + aposentadoria

    print('-'*30)
    print(cadastro)
    for k, v in cadastro.items():
        print(f'{k} tem o valor {v}')
