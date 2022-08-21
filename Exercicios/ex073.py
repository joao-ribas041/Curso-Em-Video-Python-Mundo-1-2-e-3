# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma Lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time da Chapecoense.

times = ('Palmeiras', 'Fluminense', 'Flamengo', 'Corinthians', 'Athletico-PR', 'Internacional', 'Atletico-MG', 'America-MG', 'Bragantino',
         'Santos', 'Goias', 'São Paulo', 'Botafogo', 'Ceara SC', 'Fortaleza', 'Cuiabá', 'Avai', 'Coritiba', 'Atletico-GO', 'Juventude')

print(times[:5])
print(times[-5:])
print(sorted(times))
print(times.index('Santos')+1)
