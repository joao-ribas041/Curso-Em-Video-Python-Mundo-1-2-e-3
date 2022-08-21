# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, do zero até vinte.
# Seu programa deverá ler um número pelo teclado(entre 0 e 20) e mostrá-lo por extenso.

numeros = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
           'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

n = int(input('Digite um numero entre 0 e 20: '))
while n > 20 or n < 0:
    n = int(input('Opção Invalida, Digite novamente: '))
print(numeros[n])
