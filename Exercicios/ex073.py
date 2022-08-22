# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma Lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time do São Paulo.

times = ('Palmeiras', 'Fluminense', 'Flamengo', 'Corinthians', 'Athletico-PR', 'Internacional', 'Atletico-MG', 'America-MG', 'Bragantino',
         'Santos', 'Goias', 'São Paulo', 'Botafogo', 'Ceara SC', 'Fortaleza', 'Cuiabá', 'Avai', 'Coritiba', 'Atletico-GO', 'Juventude')

print('-='*20)
print(f'Lista de times do Brasileirão: {times}')
print('-='*20)
print(f'Os 5 primeiros são {times[:5]}')
print('-='*20)
print(f'OS 4 Ultimos são {times[-4:]}')
print('-='*20)
print(f'Em ordem alfabética: {sorted(times)}')
print('-='*20)
print(f'O São Paulo esta em {times.index("São Paulo")+1}ª posição.')
 