'''n = cont = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    cont += n
#print('A soma vale {}'.format(cont))
print(f'A soma vale {cont}')'''

nome = 'José'
idade = 33
salário = 980.00

print(f'O {nome:-^20} tem {idade} anos e ganha R${salário:.2f}.')
