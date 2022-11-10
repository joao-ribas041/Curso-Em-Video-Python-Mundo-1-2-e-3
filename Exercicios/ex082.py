# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas
# os valores pares e os valores impares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.
l_base = []
l_par = []
l_impar = []
while True:
    l_base.append(int(input('Digite um valor: ')))
    opc = str(input('Deseja continuar? [S/N] '))
    if opc in 'Nn':
        break

print('-'*15)
for numero in l_base:
    if numero % 2 == 0:
        l_par.append(numero)
    else:
        l_impar.append(numero)
print('-'*15)
print(f'Lista completa: {l_base}')
print(f'Numeros pares: {l_par}')
print(f'Numeros impares: {l_impar}')
