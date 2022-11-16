# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = [0, 0, 0]
soma_pares = 0

for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f'Digite um valor para [{i}, {j}]: '))

print('-='*15)
print('Matriz: ')
for i in range(3):
    for j in range(3):
        print(f'[{matriz[i][j]:^5}]', end='')
    print()

for lista in matriz:
    for valor in lista:
        if valor % 2 == 0:
            soma[0] = soma[0] + valor
        if matriz[0][2]:
            soma[1] = soma[1] + valor

print(f'A soma dos valores pares: {soma[0]}')
print(f'A soma dos valores da terceira coluna: {soma[1]}')
