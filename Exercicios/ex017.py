# Faça um programa que leia o comprimento de um cateto oposto e do cateto adjacente de um triangulo retangulo,
# calcule e mostre o comprimento da hipotenusa.

from math import hypot

cat_op = float(input('Comprimento do cateto oposto: '))
cat_ad = float(input('Comprimento do cateto adjacente: '))

print('A hipotenusa vai medir {:.2f}'.format(hypot(cat_op, cat_ad)))
