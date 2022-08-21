# Escreva o programa que pergunte o salario de um funcionario e calcule o valor do seu aumento.
# Para salarios superiores a R$1.250,00, calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de 15%

salario = float(input('Digite seu salario: R$'))
a1 = 10
a2 = 15

if salario > 1250.0:
    aumento = salario+(salario*a1/100)
else:
    aumento = salario+(salario*a2/100)
print('Seu salario subiu de R${:.2f} para R${:.2f}.'.format(salario, aumento))
 