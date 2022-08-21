# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binario
# 2 para octal
# 3 para hexadecimal

n = int(input('Digite um numero: '))
opçao = int(input('''Para qual base deseja converter?  
[1] para binário.
[2] para octal.
[3] para hexacecimal.
Sua opção: '''))

if opçao == 1:
    print('O numero {} convertido para BINÁRIO é igual a {}.'.format(n, bin(n)[2:]))
elif opçao == 2:
    print('O numero {} convertido para OCTAL é igual a {}.'.format(n, oct(n)[2:]))
elif opçao == 3:
    print('O numero {} convertido para HEXADECIMAL é igual a {}.'.format(n, hex(n)[2:]))
else:
    print('Opção invalida, tente novamente.')