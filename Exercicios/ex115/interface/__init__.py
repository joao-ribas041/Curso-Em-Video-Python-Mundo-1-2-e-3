from utilidades import leiaInt


def linha():
    l = '~'*40
    return l


def cabecalho(msg):
    print(linha())
    print(f'{msg:^{len(linha())}}')
    print(linha())


def menu(lista):
    for i, opc in enumerate(lista, 1):
        print(f'{i} - {opc}')
    print(linha())
    opc = leiaInt('Sua opção: ')
    return opc
