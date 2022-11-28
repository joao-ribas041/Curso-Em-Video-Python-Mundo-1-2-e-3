# Crie um programa que tenha uma função leiaInt(), que vai funcionar de forma semelhante
# à função input do Python, só que fazendo a validação para aceitar apenas um valor numérico.
# Ex:
# n = leiaInt('Digite um n')

def leiaInt(txt):
    verificado = False
    valor = 0
    while True:
        resultado = str(input(txt))

        if resultado.isnumeric():
            valor = int(resultado)
            verificado = True
        else:
            print('Erro, por favor digite um numero inteiro valido')
        if verificado == True:
            break
    return valor


n = leiaInt('Digite um número: ')
print(f'Voce acabou de digitar o valor {n}')
