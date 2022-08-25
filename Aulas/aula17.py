num = [2, 5, 9, 1]
num[2] = 3  # substitui na lista
num.append(7)  # adciona o numero na lista
num.sort(reverse=True)  # organiza de traz pra frente(reverse)
num.insert(2, 2)  # insere na posição x o valor y e reorganiza
# se tiver valores iguais ele remove o primeiro e vai seguindo a ordem
if 4 in num:
    num.remove(5)
else:
    print("Nao achei o numero 5")
print(num)
print(f'Essa lista tem {len(num)} elementos.')


"""valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

print('-'*15)
for c, v in enumerate(valores):
    print(f'na posição {c} encontrei o valor {v}!')
print('Finalizei a lista.')
"""


a = [2, 3, 4, 7]
# b = a
# b[2] = 8 # Python cria uma LIGAÇÃO ENTRE AS LISTAS, CUIDADO

b = a[:]  # cria a copia da lista
b[2] = 8
print(f'Lista A: {a}.')
print(f'Lista B: {b}.')
