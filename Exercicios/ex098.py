# Faça um programa que tenha um função chamada contador(), que receba
# três parâmetros: início, fim e passo e realize a contagem.
# Seu programa tem que realizar três contagens através da função criada:
# a)De 1 até 10, de 1 em 1
# b)De 10 até 0, de 2 em 2
# c)Uma contagem personalizada.

from time import sleep
linha = '~'*40


def contador(inicio, fim, passo):
    print(linha)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(0.5)

    if passo <= 0:
        passo = 1

    if fim > inicio:
        fim += 1
        for i in range(inicio, fim, passo):
            print(i, end=' ')
        print()

    # elif inicio > fim:
    else:
        fim -= 1
        passo *= -1
        for i in range(inicio, fim, passo):
            print(i, end=' ')
        print()


contador(1, 10, 1)
contador(10, 0, 2)
print(linha)
print('Sua Vez.')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
print('Fim')
