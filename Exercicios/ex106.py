# Faça um mini-sistema que utilize a interactive help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o funcionário digitar a palavra 'FIM', o programa se encerrará
# OBS: use cores.
def cores(cor):
    colors = {
        'preto': '\033[0;37;40m',
        'vermelho': '\033[0;30;41m',
        'verde': '\033[0;30;42m',
        'amarelo': '\033[0;30;43m',
        'azul': '\033[0;30;44m',
        'magenta': '\033[0;30;45m',
        'ciano': '\033[0;30;46m',
        'branco': '\033[0;30;47m',
        'fecha': '\033[m'
    }
    return colors[cor]


def msg(str, cor='preto'):
    tamanho = len(str) + 4
    linha = '~' * tamanho

    print(f'{cores(cor)}{linha}{cores("fecha")}')
    print(f'{cores(cor)}{str:^{tamanho}}{cores("fecha")}')
    print(f'{cores(cor)}{linha}{cores("fecha")}')


def ajuda(func):
    from time import sleep

    msg(f'Acessando o manual do comando {func}', 'branco')
    sleep(1)

    print(f'{cores("vermelho")}')
    print(help(func))
    print(cores('fecha'))


msg('Ajuda em Python', 'azul')
busca = str(input('Função ou biblioteca: '))
ajuda(busca)
