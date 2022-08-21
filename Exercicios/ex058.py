# Melhore o jogo do DESAFIO 28 onde o computador vai "pensar" em um numero entre 0 e 10.
# Só que agora o jogador vai tentar advinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

sorteio = randint(0, 10)
jogadas = int(0)
acertou = False

while not acertou:
    print()
    print(sorteio)
    chute = int(input('Digite um numero: '))

    if chute == sorteio:
        acertou = True
        print('-='*15)
        print('Parabéns, voce acertou.')
        print('Computador: {}.'.format(sorteio))
        print('Você: {}.'.format(chute))
    else:
        print('-='*15)
        print('Você errou, tente novamente.')
        print('Computador: {}.'.format(sorteio))
        print('Você: {}.'.format(chute))
    jogadas += 1
print('Quantidade de jogadas até acertar: {}.'.format(jogadas))
print('fim')
