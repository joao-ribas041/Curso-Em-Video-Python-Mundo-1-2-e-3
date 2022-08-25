# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os
# em uma lista, já na posição correta de inserçao(sem usar o sort()).
# No final mostre a lista ordenada na tela.

lista = list()
maior = menor = x = int()

for c in range(0, 5):
    x = input(f'Digite um valor {c}: ')
    if c == 0:
        lista.append(x)
        print('Adicionado ao final da lista')
    else:
        maior = max(lista)
        menor = min(lista)
        if x > maior:
            lista.append(x)
            print('Adicionado ao final da lista.')
        elif x < menor:
            lista.insert(0, x)
            print('Adicionado na posição 0 da lista.')
        else:
            for pos, l in enumerate(lista):
                if l > x:
                    lista.insert(pos, x)
                    print(f'Adicionado na posição {pos}')
                    break

print('-='*20)
print(f'Lista: {lista}')
