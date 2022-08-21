# Crie um algoritimo que leia um numero e mostre o seu dobro, triplo e a raiz quadrada.
n1 = int(input('Digite um numero: '))
do = n1*2
tri = n1*3
#ra = n1**(1/2)
ra = pow(n1, (1/2))

print('Dobro: {}.'.format(do))
print('Triplo: {}.'.format(tri))
print('Raiz: {:.2f}.'.format(ra))
