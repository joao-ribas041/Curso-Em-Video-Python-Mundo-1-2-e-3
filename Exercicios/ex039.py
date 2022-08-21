# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se ja passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que faltou ou que passou do prazo.

from datetime import date
print()
nasc = int(input('Em que ano você nasceu? '))
ano_atual = date.today().year
idade = ano_atual - nasc

if idade < 16:
    print('Você é muito novo para se alistar.')
elif idade >= 16 and idade < 18:
    tempo_alistamento = 18 - idade
    print('Você ainda irá se alistar no serviço militar, faltam apenas {} anos. seu alistamento sera em {}'.format(
        tempo_alistamento, (tempo_alistamento + ano_atual)))
elif idade == 18:
    print('Você está no tempo de alistamento, procure a junta militar.')
elif idade > 18:
    tempo_alistamento = idade - 18
    print('Você passou em {} anos do tempo de alistamento. seu alistamento deveria ter ocorrido em {}.'.format(
        tempo_alistamento, -(tempo_alistamento - ano_atual)))
