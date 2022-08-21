# Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.
# ex:
# APOS A SOPA
# A SACADA DA CASA
# A TORRE DA DERROTA
# O LOBO AMA O BOLO
# ANOTARAM A DATA DA MARATONA

print()
frase0 = str(input('Digite uma frase: '))
frase1 = frase0.lower().replace(' ', '')
frase2 = str()
tfrase = len(frase1)

if frase1[0] == frase1[tfrase-1] and frase1[1] == frase1[tfrase-2] and frase1[2] == frase1[tfrase-3]:
    frase2 = frase1[::-1]
    '''for c in range(tfrase-1, -1, -1):
        frase2 += frase1[c]'''
    print()
    print('É um PALINDROMO.')
    print('NORMAL: {}.'.format(frase0))
    print('INVERT: {}.'.format(frase2))
else:
    print()
    print('{} NÃO é um PALINDROMO'.format(frase0))
