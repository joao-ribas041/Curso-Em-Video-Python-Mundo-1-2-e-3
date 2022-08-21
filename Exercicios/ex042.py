# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triangulo será formado:
# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes

n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
n3 = float(input('Digite o terceiro valor: '))
triangulo = (False)

if (n1 + n2) > n3 and (n2 + n3) > n1 and (n1 + n3) > n2:
    print('{} com {} e {} podem formar um triangulo.'.format(n1, n2, n3))
    if n1 == n2 == n3:
        print('Equilátero!')
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print('Isóceles!')
    elif n1 != n2 != n3 != n1:
        print('Escaleno!')
else:
    print('{} com {} e {} não pode formar um triangulo.'.format(n1, n2, n3))
