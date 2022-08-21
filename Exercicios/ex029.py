# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite

print('RADAR 80km/h')
velocidade = int(input('Digite a velocidade do carro: '))

if velocidade <= 80:
    print('Você esta dentro do limite de velocidade. Continue assim.')
else:
    multa = float((velocidade - 80) * 7.0)
    print('Voce foi multado! A multa foi de R${:.2f}'.format(multa))
