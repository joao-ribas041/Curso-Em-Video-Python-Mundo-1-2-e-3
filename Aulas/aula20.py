""" def linha():
    print('-' * 30)


def titulo(msg):
    print('-' * 30)
    print(f'{msg:^30}')
    print('-' * 30)


titulo('CURSO EM VIDEO')
titulo('APRENDA PYTHON')
titulo('GUSTAVO GUANABARA') """


""" def soma(a, b):
    s = a + b
    print(s)


soma(4, 5)
soma(8, 9)
soma(2, 1) """


def soma(*valores):
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)
