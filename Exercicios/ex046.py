# Faça um programa que mostre na tela a contagem regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep

for c in range(10, -1, -1):
    sleep(1)
    print('Faltam apenas {}.'.format(c))
print('BOM BOM POW')
