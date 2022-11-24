# Faça um programa que tenha uma função chamado área(), que receba as dimensões
# de um terreno retangular (largura e comprimento) e mostre a area do terreno.


def area(largura, comprimento):
    print(
        f'A área de um terreno é de {largura}x{comprimento} é de {largura*comprimento}m².')


l = float(input('Digite a largura (m): '))
c = float(input('Digite o comprimento (m): '))
area(l, c)
