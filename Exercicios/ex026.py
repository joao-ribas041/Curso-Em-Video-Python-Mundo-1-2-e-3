# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A".
# Em que posição ela aparece a priemira vez.
# Em que posição ela aparece a ultima vez.

frase = str(input('Digite uma frase: ')).lower()

print('A letra A aparece {} vezes no texto.'.format(frase.count('a')))
print('A primeira letra a aparece na posição {}.'.format(frase.find('a')+1))
print('A ultuma letra a aparece na posição {}.'.format(frase.rfind('a')))
