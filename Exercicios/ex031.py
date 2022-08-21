# Desenvolva um programa que pergunte a distancia de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200km
# e R$0,45 para viagens mais longas.

distancia = int(input('Digite a distancia da viagem: '))

if distancia <= 200:
    valor = float(0.50)
else:
    valor = float(0.45)
print('O valor da viagem de {}Km é de R${:.2f}.'.format(distancia, distancia*valor))