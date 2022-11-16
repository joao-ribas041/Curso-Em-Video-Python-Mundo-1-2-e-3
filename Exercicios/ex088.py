# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear
# 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

# Mega sena = numeros entre 1 e 60, 6 numeros
from random import randint
from time import sleep

mega_sena = []
jogo = []
numero = 0
print('-='*15)
print('         MEGA SENA        ')
print('-='*15)
qtd_jogos = int(input('Deseja sortear quantos jogos? '))

for c in range(qtd_jogos):
    contador = 0
    while True:
        numero = randint(1, 60)
        if numero not in jogo:
            jogo.append(numero)
            contador += 1
        if contador >= 6:
            jogo.sort()
            mega_sena.append(jogo[:])
            jogo.clear()
            break

for c, game in enumerate(mega_sena, start=1):
    print(f'Jogo {c}: {game}')
    sleep(1)
