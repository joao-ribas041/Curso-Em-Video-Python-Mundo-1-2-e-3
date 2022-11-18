# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
jogadores = []

for i in range(1, 5):
    jogador = {'nome': 'Jogador' + str(i), 'jogada': randint(1, 6)}
    print(f'O {jogador["nome"]} tirou {jogador["jogada"]}')
    jogadores.append(jogador.copy())
    sleep(1)

jogadores = sorted(jogadores, key=lambda i: i['jogada'], reverse=True)

print('Ranking dos jogadores (Maior - Menor):')
for i, jogador in enumerate(jogadores, 1):
    print(f'{i}o. lugar - {jogador["nome"]} com {jogador["jogada"]}.')
    sleep(1)
