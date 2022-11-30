def aumentar(valor=0, porcentagem=0, formatado=False):
    resultado = valor + (valor * porcentagem / 100)
    if resultado:
        resultado = moeda(resultado)
    return resultado


def diminuir(valor=0, porcentagem=0, formatado=False):
    resultado = valor - (valor * porcentagem / 100)
    if formatado:
        resultado = moeda(resultado)
    return resultado


def dobro(valor=0, formatado=False):
    resultado = valor * 2
    if formatado:
        resultado = moeda(resultado)
    return resultado


def metade(valor=0, formatado=False):
    resultado = valor / 2
    if formatado:
        resultado = moeda(resultado)
    return resultado


def moeda(valor):
    resultado = str(f'R$ {valor:.2f}').replace('.', ',')
    return resultado


def resumo(valor=0, porcAumento=0, porcReducao=0):

    linha = '~'*35
    print(linha)
    print(f'{"Resumo do valor":^{len(linha)}}')
    print(linha)
    print(f'Preço Analisado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'{porcAumento:.0f}% de aumento: \t{aumentar(valor, porcAumento, True)}')
    print(f'{porcReducao:.0f}% de reducao: \t\t{diminuir(valor, porcReducao, True)}')
    print(linha)
