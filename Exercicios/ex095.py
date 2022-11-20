# Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo
# um sistema de visualização de detalhes do aproveitamento de cada jogador.
jogadores = []

jogador = {}
gols = []

while True:
    gols_totais = 0
    jogador['nome'] = str(input('Digite o nome do jogador: ')).capitalize()
    jogador['partidas'] = int(
        input(f'Quantas partidas {jogador["nome"]} jogou? '))
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
print('-'*30)
print(f'{"cod":^3} {"nome":<8} {"Partidas":<3} {"gols":<5} {"Total":<3}')
print('-'*30)
for i, j in enumerate(jogadores):
    print(
        f'{i+1:^3} {j["nome"]:<8} {j["partidas"]:<3} {j["gols-por-partida"]:<5} {j["gols-totais"]:<3}')
