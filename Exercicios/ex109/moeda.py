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
