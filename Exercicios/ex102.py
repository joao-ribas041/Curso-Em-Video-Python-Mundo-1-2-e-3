# Crie um programa que tenha uma função fatorial() que receba dois parametros: o primeiro que
# indique o número a calcular e o outro chamado show, que será um valor lógico(opcional)
# indicando se será mostrado ou não na tela o processo de calculo do fatorial.

def fatorial(num=1, show=False):
    """-> Calcula o fatorial de um número
    :param num: Número a ser calculado
    :param show: (opcional) Para mostrar ou não a conta
    :return: Valor do fatorial
    """

    fat = 1
    for i in range(num, 0, -1):
        if show == True:
            print(f'{i} x', end=' ') if i > 1 else print(f'{i} =', end=' ')
        fat *= i
    return fat


print(fatorial(10, True))
help(fatorial)
