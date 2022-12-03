def leiaInt(msg):
    while True:
        try:
            r = int(input(msg))
        except:
            print('Erro, por favor digite um valor valido.')
            continue
        else:
            return r


def leiaStr(msg):
    while True:
        try:
            m = str(input(msg))
        except:
            print('Erro, por favor digite um nome válido.')
            continue
        else:
            return m
