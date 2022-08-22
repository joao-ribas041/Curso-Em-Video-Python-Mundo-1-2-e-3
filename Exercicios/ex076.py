# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

tuplaProdutos = 'Caneta', 2, 'Lapis', 1.5, 'Borracha', 2.5, 'Penal', 4.5, 'Caderno', 10

print('-'*40)
print(f'{"Lista de preços":^40}')
print('-'*40)

for c in range(0, len(tuplaProdutos)):
    if c % 2 == 0:
        print(f'{tuplaProdutos[c]:.<30}', end='')
    else:
        print(f'R${tuplaProdutos[c]:>7.2f}')
print('-'*40)
