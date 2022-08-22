# Crie um programa que tenha uma tupla com várias palavras(não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.


tuplaPalavras = 'Algodao', 'Bola', 'Tatuagem', 'Bone', 'Notebook', 'Moto', 'Diversao'

for pos, contador in enumerate(tuplaPalavras):
    print(f'\nNa palavra {contador.upper()} temos ', end='')
    for letras in contador:
        if letras in 'AaEeIiOoUu':
            print(letras, end=' ')
    print()
