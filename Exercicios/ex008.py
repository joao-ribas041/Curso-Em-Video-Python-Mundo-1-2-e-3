# Escreva um programa que leia um valor em metros e exiba convertido em centimetros e milimetros.

m = float(input('Digite um valor: '))

km = m*10
hm = m*1
dam = m*0.1
# m
dm = m*10
cm = m*100
mm = m*1000

print('{} Kilometros.'.format(km))
print('{} hm.'.format(hm))
print('{} dam.'.format(dam))
print('{} metros.'.format(m))
print('{} dm'.format(dm))
print('{} centimetros.'.format(cm))
print('{} mlimetros.'.format(mm))
