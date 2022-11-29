def aumentar(valor=0, porcentagem=0):
    valor += (valor * porcentagem) / 100
    return valor


def diminuir(valor=0, porcentagem=0):
    valor -= (valor * porcentagem) / 100
    return valor


def dobro(valor=0):
    return valor * 2


def metade(valor=0):
    return valor / 2
