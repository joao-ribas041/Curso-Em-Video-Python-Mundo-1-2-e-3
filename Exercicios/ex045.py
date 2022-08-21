# Crie um programa que faça o computador jogar Jokenpô com você.
# PEDRA, PAPEL,  TESOURA

import random

pedra = ('Pedra')
papel = str('Papel')
tesoura = str('Tesoura')

ia = [pedra, papel, tesoura, papel, pedra, tesoura, pedra, tesoura, papel]
random.shuffle(ia)

print()
print('Vamos jogar Jokenpô?')
print('''Escolha:
[1] para {}.
[2] para {}.
[3] para {}.'''.format(pedra, papel, tesoura))
opção = int(input('Digite sua opção: '))

if opção == 1:
    escolha = pedra
elif opção == 2:
    escolha = papel
elif opção == 3: 
    escolha = tesoura
else:
    print('Opção errada, tente novamente')

print('-='*30)

if ia[1] == pedra and escolha == pedra or ia[1] == papel and escolha == papel or ia[1] == tesoura and escolha == tesoura:
    print('I.A: {}.'.format(ia[1]))
    print('VOCÊ: {}.'.format(escolha))
    print()
    print('EMPATE')
    print()
elif ia[1] == pedra and escolha == tesoura or ia[1] == papel and escolha == pedra or ia[1] == tesoura and escolha == papel:
    print('I.A: {}.'.format(ia[1]))
    print('VOC Ê: {}.'.format(escolha))
    print()
    print('VOCÊ PERDEU!')
    print()
else:
    print('I.A: {}.'.format(ia[1]))
    print('VOCÊ: {}.'.format(escolha))
    print()
    print('VOCÊ VENCEU!')
    print()
