# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em
# uma lista composta. No final, mostre um boletim contendo a média de cada um
# e permita que o usuário possa mostrar as notas de cada aluno individualmente.

sala = []
aluno = []
notas = []

while True:
    aluno.append(str(input('Nome do aluno: ')))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    aluno.append(notas[:])
    aluno.append((notas[0] + notas[1]) / 2)
    sala.append(aluno[:])
    aluno.clear()
    notas.clear()
    continua = str(input('Deseja continuar? [S/N] '))
    if continua in 'Nn':
        break

print('-='*15)
print(f'{"N.":<3}{"Nome":<12}{"Média":>11}')

for i, aluno in enumerate(sala):
    print(f'{i:<3} {aluno[0]:<12} {aluno[2]:>8.1f}')

while True:
    escolha = int(
        input(f'\nMostrar notas de qual aluno? (999 para finalizar): '))
    if escolha == 999:
        break
    print(
        f'Notas de {sala[escolha][0]} são: {sala[escolha][1]}')
print('Finalizado')
