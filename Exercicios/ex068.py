# Faça um programa que jogue par ou impar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
print('-='*17)
print('VAMOS JOGAR PAR OU IMPAR')
print('-='*17)
contVitorias = int(0)
while True:
    soma = int(0)
    nComp = randint(1, 10)
    nUsuario = int(input('Digite um valor: '))
    while True:
        opc = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
        if opc == 'P' or opc == 'I':
            break
    soma = nUsuario + nComp
    print('-'*34)
    print(f'Você jogou {nUsuario} e o computador {nComp}.', end=' ')
    if soma % 2 == 0:
        print(f'Total de {soma} deu PAR')
        if opc == 'P':
            print('-'*34)
            print('Você VENCEU!')
            contVitorias += 1
        else:
            print('-'*34)
            print('Você PERDEU!')
            break
    else:
        print(f'Total de {soma} deu IMPAR')
        if opc == 'I':
            print('-'*34)
            print('Você VENCEU!')
            contVitorias += 1
        else:
            print('-'*34)
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente....')
    print('-'*34)

print('=-'*17)
print(f'GAME OVER! Você venceu {contVitorias} vezes.')
