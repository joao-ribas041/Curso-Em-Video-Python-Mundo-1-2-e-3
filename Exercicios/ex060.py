# Faça um programa que leia um numero qualquer e mostre o seu fatorial.
# Ex:
# 5! = 5x4x3x2x1=120

n1 = 0

while n1 == 0:
    n1 = int(input('Digite um numero para Fatorial: '))

cont = n1
fat = 1
print('{}! = '.format(n1), end='')

'''while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fat *= cont
    cont -= 1'''

for cont in range(n1, fat-1, -1):
    fat *= cont
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')

print('{}'.format(fat))
