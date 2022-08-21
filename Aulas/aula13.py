'''print()
print('MODO 1')
for c in range(0, 6):
    print(c)
print()
print('MODO 3')
for c in range(6, 0, -1):
    print(c)
print()
print('MODO 3')
for c in range(6, 0, -2):
    print(c)

n = int(input('Digite um numero: '))
for c in range(0, n+1):
    print(c)
print('fim')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for c in range(i, f, p):
    print(c)
print('fim')
'''

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('a soma de todos os valores é igual a: {}'.format(s))
