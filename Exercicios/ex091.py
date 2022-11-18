# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter
jogo = {}

for i in range(1, 5):
    jogo['jogador' + str(i)] = randint(1, 6)

for k, v in jogo.items():
    print(f'o {k} tirou {v}.')
    sleep(0.5)

rank_jogo = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('\nRanking dos jogadores (Maior - Menor):')
for i, rank in enumerate(rank_jogo, 1):
    print(f'{i}o. lugar - {rank[0]} com {rank[1]}.')
    sleep(0.5)
