# Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o numero solicitado for negativo.

while True:
    print('-'*35)
    n = int(input('Qual tabuada deseja vizualizar? '))
    print('-'*35)
    if n < 0:
        break
    for c in range(1, 11):
        tabuada = n*c
        print(f'{n} x {c} = {tabuada}')
print('FINALIZADO...')
