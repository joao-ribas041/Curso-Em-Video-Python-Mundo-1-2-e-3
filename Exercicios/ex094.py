# Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os
# dicionários em uma lista. No final, mostre:
# A)Quantas pessoas foram cadastradas.
# B)A média de idade do grupo.
# C)Uma listas com todas as mulheres.
# D)Uma lista com todas as pessoas com idade acima da média.

grupo = []
pessoa = {}
idade_total = media = total_pessoas = 0

while True:
    pessoa['nome'] = str(input('Digite o nome: ')).capitalize()
    pessoa['sexo'] = str(
        input(f'Qual é o genero de {pessoa["nome"]}? [M/F] ')).upper()
    pessoa['idade'] = int(input(f'Qual é a idade de {pessoa["nome"]}? '))
    idade_total += pessoa['idade']
    grupo.append(pessoa.copy())
    pessoa.clear()

    resp = str(input('Deseja continuar? [S/N] '))
    print()
    if resp in 'Nn':
        break

total_pessoas = len(grupo)
media = idade_total / total_pessoas

print('-'*30)
print(f'Foram cadastrado {total_pessoas} pessoas na lista.')
print(f'A idade média do grupo é de {media} anos.')
print('-'*30)

print('Lista de mulheres no grupo: ', end='')
for i, p in enumerate(grupo):
    if p['sexo'] == 'F':
        print(p['nome'], end=', ') if i+1 < total_pessoas else print(
            p['nome'], end='.')
print()
print('-'*30)

print(f'Pessoas com idade acima da média: ', end='')
for p in grupo:
    if p['idade'] > media:
        print(p['nome'], end=' ')
print()
print('Finalizado.')
