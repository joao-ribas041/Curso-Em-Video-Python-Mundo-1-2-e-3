# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro
# o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma
# pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.


def voto(nasc):
    from datetime import datetime
    idade = datetime.now().year - nasc

    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    elif idade >= 18:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


while True:
    nasc = int(input('\nDigite o ano de nascimento. [999] finaliza: '))
    if nasc == 999:
        break
    else:
        print(voto(nasc))


print('Finalizado')
