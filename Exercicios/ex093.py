# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida. No final,
# tudo isso será guardado em um dicionário, incluindo o total de gols
# feitos durante o campeonato.

jogador = {}
gols = []
gols_totais = 0

jogador['nome'] = str(input('Digite o nome do jogador: '))
jogador['qtd-partidas'] = int(
    input(f'Quantas partidas {jogador["nome"]} jogou? '))

for i in range(1, jogador['qtd-partidas'] + 1):
    gols.append(
        int(input(f'Quantos gols {jogador["nome"]} fez no {i}o. jogo? ')))
jogador['gols-por-partida'] = gols

for gol in jogador['gols-por-partida']:
    gols_totais += gol
jogador['gols-totais'] = gols_totais

print('-'*30)
print(jogador)
print('-'*30)
for k, v in jogador.items():
    print(f'{k} tem o valor {v}')
print('-'*30)
print(f'O jogador {jogador["nome"]} jogou {jogador["qtd-partidas"]}')
for i, gol in enumerate(jogador['gols-por-partida'], 1):
    print(f' -> Na partida {i}, {jogador["nome"]} fez {gol} gols.')
print(f'Com um total de {jogador["gols-totais"]} gols.')
print('-'*30)
