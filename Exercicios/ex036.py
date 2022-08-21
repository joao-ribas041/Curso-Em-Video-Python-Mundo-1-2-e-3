# Escreva um programa para aprovar um emprestimo bancario para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela nao pode exceder 30% do salario ou entao o emprestimo será negado.

valor_casa = float(input(('Qual o valor da casa que deseja financiar? R$')))
salario_comprador = float(input('Digite o seu salário: R$'))
anos_financiamento = int(
    input('Quantos anos pretende pagar esse financiamento? '))
print('-='*15)


valor_parcela = valor_casa / (anos_financiamento * 12)
vmaximo_parcela = salario_comprador * 30 / 100

print('Quantidade de parcelas: {} meses.'.format(anos_financiamento * 12))
print('Valor da parcela: R${:.2f}'.format(valor_parcela))

if valor_parcela > vmaximo_parcela:
    print('Empréstimo negado! a parcela excedeu 30% do seu salario.')
elif valor_parcela < vmaximo_parcela:
    print('Empréstimo aprovado!')
elif valor_parcela == vmaximo_parcela:
    print('Você esta no limite da prestação, reduza o valor da parcela aumento o tempo do financiamento.')
