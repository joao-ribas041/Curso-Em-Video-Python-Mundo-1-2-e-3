from interface import cabecalho, menu
from arquivos import cadastrar, listarCadastros
from utilidades import leiaInt, leiaStr
from time import sleep

while True:
    cabecalho('Menu')
    resp = menu(['Cadastrar novas pessoas.',
                'Ver pessoas cadastradas.', 'Sair'])
    match resp:
        case 1:
            n = leiaStr('Digite o nome: ')
            i = leiaInt(f'Digite a idade de {n}: ')
            cadastrar(n, i)
        case 2:
            listarCadastros()
            sleep(2)
        case 3:
            break
print('Programa finalizado.')
