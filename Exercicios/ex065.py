# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lido.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

soma = maior = media = menor = somador = int(0)
continuar = str('S')

while continuar in 'Ss':
    n = int(input('Digite um valor: '))
    soma += n
    somador += 1
    if somador == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]

print()
print('Maior: {}.'.format(maior))
print('Menor: {}.'.format(menor))
media = soma / somador
print('Média: {}.'.format(media))
print('Quantidade de numeros digitados: {}.'.format(somador))
