# Faça um programa que leia a média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.
aluno = {}
aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['media'] = float(input(f'Digite a média de {aluno["nome"]}: '))
if aluno['media'] >= 6:
    aluno['situacao'] = 'APROVADO'
else:
    aluno['situacao'] = 'REPROVADO'

print(f'\nO nome é {aluno["nome"]}.')
print(f'A média foi de {aluno["media"]}.')
print(f'A situação de {aluno["nome"]} é {aluno["situacao"]}')
