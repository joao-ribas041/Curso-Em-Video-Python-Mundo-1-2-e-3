# Crie um programa que leia varios numeros inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
# (desconsiderando o flag)

n = soma = cont = int(0)
while n != 999:
    n = int(input('Digite um valor [999 para parar]: '))
    if n != 999:
        soma += n
        cont += 1
print()
print('a ultima soma resultou em {}'.format(soma))
print('A quantidade de numeros informados foi de {}.'.format(cont))
print()
