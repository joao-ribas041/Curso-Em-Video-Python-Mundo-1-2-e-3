'''for c in range(1, 5):
    n = int(input('Digite um valor: '))
print('Fim')'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Quantidade numeros pares: {}.'.format(par))
print('Quantidade numeros Impares: {}.'.format(impar))

n = 1
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [s/n] ')).upper()
print('Fim')
