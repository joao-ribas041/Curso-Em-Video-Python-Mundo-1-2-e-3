# Rescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
def leiaInt(msg=''):
    aprovado = False
    valor = 0
    while not aprovado:
        try:
            var = str(input(msg))
        except KeyboardInterrupt:
            print('O usuário preferiu não informar os dados.')
        else:
            if var.isnumeric():
                valor = int(var)
                aprovado = True
            else:
                print('Erro, digite um numero inteiro válido.')
    return valor


def leiaFloat(msg=''):
    aprovado = False
    valor = 0

    while not aprovado:
        var = str(input(msg)).replace(',', '.').strip()

        if var.isalpha() or var == '':
            print('Erro, digite um numero real válido.')
        else:
            try:
                valor = float(var)
            except (ValueError, TypeError):
                print('Erro, digite um numero real válido.')
            except KeyboardInterrupt:
                print('O usuário preferiu não informar os dados.')
            except Exception as erro:
                print(
                    f'Erro, digite um numero real válido. Erro: {erro.__class__}')
            else:
                aprovado = True
    return valor


a = leiaInt('Digite um numero inteiro: ')
b = leiaFloat('Digite outro numero real: ')
print(f'O valor inteiro é {a} e o real é {b}')
