# Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados.

# EX:
# Digite um numero: 1834

# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 1

print('')
print('-'*10)
print('')

num = int(input('Digite um numero de 0 até 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Numero informado: {}.'.format(num))
print('Unidade: {}.'.format(u))
print('Dezena: {}.'.format(d))
print('Centena: {}.'.format(c))
print('Milhar: {}.'.format(m))

# numero = str(num)
# numero = numero[0:4]

# print('Unidade: {}.'.format(numero[3]))
# print('Dezena: {}.'.format(numero[2]))
# print('Centena: {}.'.format(numero[1]))
# print('Milhar: {}.'.format(numero[0]))
