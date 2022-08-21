# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condiçao de pagamento:
# - À vista dinheiro/cheque: 10% de desconto.
# - À vista no cartão: 5% de desconto.
# - Em até 2x no cartão: preço normal.
# - 3x ou mais no cartão: 20% de juros.

valor_produto = float(100)
condição = int(input('''Qual será a forma de pagamento?
[1]À vista no dinheiro/cheque 10% off
[2]À vista no cartão 5% off
[3]Em até 2x no cartão
[4]3x ou mais no cartão 20% de juros.
Sua opção: '''))

if condição == 1:
    valor_final = valor_produto - (valor_produto * 10 / 100)
    print('Você tem 10% de desconto no dinheiro, o valor final ficou R${:.2f}.'.format(
        valor_final))
elif condição == 2:
    valor_final = valor_produto - (valor_produto * 5 / 100)
    print('Você tem 5% de desconto no cartão, o valor final ficou R${:.2f}.'.format(
        valor_final))
elif condição == 3:
    valor_final = valor_produto
    print('Você irá pagar R${:.2f}.'.format(valor_final))
    print('O valor da parcela ficou R${:.2f} em 2x'.format(valor_final / 2))
elif condição == 4:
    valor_final = valor_produto + (valor_produto * 20 / 100)
    print('Acima de 3x juros de 20%, valor final R${:.2f}.'.format(
        valor_final))
    parcela = int(input('Ira parcelar em quantas vezes? '))
    print('O valor da parcela em {}x ficou de R${:.2f}.'.format(
        parcela, valor_final / parcela))
else:
    print('Opção invalida, tente novamente.')
