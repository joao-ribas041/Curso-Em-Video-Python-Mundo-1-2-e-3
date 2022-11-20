# Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo
# um sistema de visualização de detalhes do aproveitamento de cada jogador.
jogadores = []
jogador = {}
gols = []
maior_participacao = 0

while True:
    gols_totais = 0
    jogador['nome'] = str(input('Digite o nome do jogador: ')).capitalize()
    jogador['partidas'] = int(
        input(f'Quantas partidas {jogador["nome"]} jogou? '))
    if maior_participacao < jogador['partidas']:
        maior_participacao = jogador['partidas']

    for i in range(0, jogador['partidas']):
        gol = int(
            input(f'Quantos gols {jogador["nome"]} fez no {i+1}o. jogo: '))
        gols.append(gol)
        gols_totais += gol

    jogador['gols-por-partida'] = gols[:]
    jogador['gols-totais'] = gols_totais
    gols.clear()
    jogadores.append(jogador.copy())
    jogador.clear()

    continua = str(input('Deseja continuar? [S/N] ')).upper()
    print()
    if continua in 'Nn':
        break

print(maior_participacao)
print('-'*40)
print(f'{"cod":^3} {"nome":<8} {"Partidas":<8} {"gols"} {"Total":>7}')
print('-'*40)
for i, j in enumerate(jogadores):
    print(
        f'{i:^3} {j["nome"]:<8} {j["partidas"]:<8} {j["gols-por-partida"]} {j["gols-totais"]:>7}')
print('-'*40)
print(f'len: {len(jogadores)}')
while True:
    consulta = int(input('Deseja mostrar dados de qual jogador? \n'))
    if consulta == 999:
        break
    elif consulta > len(jogadores) - 1 or consulta < 0:
        print(f'Não existe o codigo {consulta}.\n')
    else:
        print(f'-- Levantamento do jogador {jogadores[consulta]["nome"]}')
        for i, gol in enumerate(jogadores[consulta]['gols-por-partida']):
            print(
                f'  No jogo {i}, {jogadores[consulta]["nome"]} fez {gol} gols.')
print('Finalizado.')
