# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: Mirim
# - Até 14 anos: Infantil
# - Até 19 anos: Junior
# - Até 25 anos: Sênior
# - Acima: Master

from datetime import date

nascimento = int(input('Digite seu ano de nascimento: '))
ano = date.today().year
idade = ano - nascimento
print('Sua idade: {} anos.'.format(idade))

if idade <= 9:
    print('Atléta Mirim.')
elif idade <= 14:
    print('Atléta Infantil.')
elif idade <= 19:
    print('Atléta Junior.')
elif idade <= 25:
    print('Atléta Senior.')
else:
    print('Atléta Master.')
