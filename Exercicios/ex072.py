# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, do zero até vinte.
# Seu programa deverá ler um número pelo teclado(entre 0 e 20) e mostrá-lo por extenso.

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
continua = 'S'

while True:
    if continua in 'Ss':
        while True:
            n = int(input('Digite um numero entre 0 e 20: '))
            if 0 <= n <= 20:
                break
            n = int(input('Opção Invalida, Digite novamente: '))
        print(f'Você digitou o numero {numeros[n]}')
        print()
    continua = str(input('Deseja Continuar? [S/N]')).strip().upper()[0]
    if continua in 'Nn':
        break
print('FINALIZADO...')
