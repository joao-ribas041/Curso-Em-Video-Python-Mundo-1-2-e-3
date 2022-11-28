# Crie um programa que tenha uma função leiaInt(), que vai funcionar de forma semelhante
# à função input do Python, só que fazendo a validação para aceitar apenas um valor numérico.
# Ex:
# n = leiaInt('Digite um n')

def leiaInt(str):
    while True:
        resultado = input(str)
        msg = 'Erro, por favor digite um numero inteiro valido'

        if resultado in '':
            print(msg)
        else:
            if resultado not in '1234567890':
                print(msg)
            else:
                return int(resultado)


n = leiaInt('Digite um número: ')
print(f'Voce acabou de digitar o valor {n}')
