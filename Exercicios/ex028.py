# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
#  e peça para o usuario tentar descobrir qual foi o numero escolhido pelo computador.
# O programa deverá escrever na tela se o usuario venceu ou perdeu.

from random import randint
from time import sleep
n = randint(0, 5)

print('-=-' * 10)
print('Vou pensar em um numero entre 0 e 5, tente advinhar...')
print('-=-' * 10)
chute = int(input('Em que numero voce pensou? '))
print('PROCESSANDO...')
sleep(2)

if chute == n:
    print('Parabéns! Você chutou o valor certo!')
else:
    print('Você errou! Tente em outra chance.')
print('O valor sorteado foi: {}.'.format(n))
