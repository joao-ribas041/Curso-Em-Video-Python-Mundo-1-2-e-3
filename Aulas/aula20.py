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


""" def soma(*valores):
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4) """


def dobra(lst):
    pos = 0
    while pos < len(lst):
        print(f'Valor {valores[pos]} dobrado: {lst[pos] * 2}')
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]

dobra(valores)
print(valores)
