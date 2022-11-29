def aumentar(valor=0, porcentagem=0):
    resultado = valor + (valor * porcentagem / 100)
    return resultado


def diminuir(valor=0, porcentagem=0):
    resultado = valor - (valor * porcentagem / 100)
    return resultado


def dobro(valor=0):
    resultado = valor * 2
    return resultado


def metade(valor=0):
    resultado = valor / 2
    return resultado
