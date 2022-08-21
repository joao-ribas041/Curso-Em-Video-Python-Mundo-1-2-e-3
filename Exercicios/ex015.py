# Escreva um programa que pergute a quantidade de Km percorridos por um carro alugado 
# e a quantidade de dias pelso quais ele foi alugado. Calcule o preço a pagar, 
# sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.

dias = int(input('Quantos dias alugado? '))
km = int(input('Quantos km rodados? '))

valor_total = (dias * 60) + (km * 0.15)

print('O total do aluguel do carro de {} dias e {} km rodados é de R${:.2f}.'.format(dias, km, valor_total))
