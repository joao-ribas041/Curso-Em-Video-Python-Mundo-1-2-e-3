# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome='<desconhecido>', qtdGols=0):
    print(f'O jogador {nome} fez {qtdGols} gol(s) durante o campeonato.')


nome = str(input('Nome do jogador: '))
gols = str(input('Quantidade de gols marcado: '))

if nome in '' and gols in '':
    ficha()
elif nome in '':
    ficha(qtdGols=gols)
elif gols in '':
    ficha(nome)
else:
    ficha(nome, gols)
