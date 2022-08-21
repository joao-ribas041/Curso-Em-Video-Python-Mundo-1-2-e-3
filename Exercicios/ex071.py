# Crie um programa que simule o funciomento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado(número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('='*30)
print('{:^30}'.format('BANCO JVRS'))
print('='*30)

saque = int(input('Digite o valor a ser sacado: R$'))
total = saque
cedula = int(50)
totalced = 0

while True:
    if total >= cedula:
        total -= cedula
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalced = 0
        if total == 0:
            break

print('='*30)
print('Volte sempre ao banco JVRS! tenha um ótimo dia.')

# com Logica matemática, While nao foi usado
'''s50 = int(50)
s20 = int(20)
s10 = int(10)
s1 = int(1)
qtdsaque = qtd50 = qtd20 = qtd10 = qtd1 = int(0)

while True:
    saque = int(input('Digite o valor que voce deseja sacar: R$'))
    qtdsaque = saque

    if qtdsaque % s50 == 0:
        qtd50 = qtdsaque // s50
        print(f'Total de {qtd50:.0f} cédulas de R${s50:.2f}')
        break
    else:
        qtd50 = qtdsaque // s50
        qtdsaque %= s50
        print(f'Total de {qtd50:.0f} cédulas de R${s50:.2f}')

    if qtdsaque % s20 == 0:
        qtd20 = qtdsaque // s20
        print(f'Total de {qtd20:.0f} cédulas de R${s20:.2f}')
        break
    else:
        qtd20 = qtdsaque // s20
        qtdsaque %= s20
        print(f'Total de {qtd20:.0f} cédulas de R${s20:.2f}')

    if qtdsaque % s10 == 0:
        qtd10 = qtdsaque // s10
        print(f'Total de {qtd10:.0f} cédulas de R${s10:.2f}')
        break
    else:
        qtd10 = qtdsaque // s10
        qtdsaque %= s10
        print(f'Total de {qtd10:.0f} cédulas de R${s10:.2f}')

    if qtdsaque % s1 == 0:
        qtd1 = qtdsaque // s1
        qtdsaque %= s1
        print(f'Total de {qtd1:.0f} cédulas de R${s1:.2f}')
        break

print('='*30)
print('Volte sempre ao banco JVRS! tenha um ótimo dia.')'''
