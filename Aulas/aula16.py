#lanche = 'Hámburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita'
'''Tuplas são Imutáveis
lanche[1] = 'Refrigerante'
print(lanche[1])'''

# print(lanche)
# print(sorted(lanche))

'''for comida in lanche:
    print(f'Eu vou comer {comida}.')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}.')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}.')
print('Comi bastante.')'''


a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(len(c))

# conta quantas vezes tem o valor x
print(c.count(5))

# em que posição esta o numero x
print(c.index(5))

pessoa = ('João', 19, 'M', 75.30)
# Apaga da memoria os valores da Tupla
del(pessoa)
print(pessoa)
