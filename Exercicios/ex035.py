# Desenvolva um programa que leia o comprimento de três retas e diga ao usuario se elas podem ou nao formar um triangulo.
r1 = float(input('Digite o primeiro numero: '))
r2 = float(input('Digite o segundo numero: '))
r3 = float(input('Digite o terceiro numero: '))


if (r1 + r2) > r3 and (r2 + r3) > r1 and (r1 + r3) > r2:
    print('Parabéns, voce conseguiu formar um triangulo.')
else:
    print('Não é possivel formar um triangulo com essas medidas.')
