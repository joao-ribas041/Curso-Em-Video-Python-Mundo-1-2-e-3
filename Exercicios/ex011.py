# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessaria para pinta-la,
# sabendo que cada litro de tinta, pinta uma area de 2m².

tin = float(10.0)
alt = float(input('Digite a Altura da parede: '))
lar = float(input('Digite a Largura da parede: '))

tot_par = alt*lar
pin = tot_par/tin

print('M² da parede: {}'.format(tot_par))
print('Litros de tinta necessaria: {}'.format(pin))
