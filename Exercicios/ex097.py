# Faça um programa que tenha uma função chamado escreva(), que receba um
# texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
# Ex:
# escreva('Olá, Mundo')
# Saída:
# ---------------
#    Olá, Mundo
# ---------------

def escreva(txt):
    comp = len(txt) + 4
    linha = '~' * comp
    print(linha)
    print(f'{txt: ^ {len(linha)} }')
    print(linha)


escreva('Olá, Mundo')
escreva('Oi')
