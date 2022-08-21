# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o valor do seu salario: R$'))
aumento = salario + (salario * 10 / 100)
print('o novo salario com o reajuste de 10% é de R${:.2f}.'.format(aumento))