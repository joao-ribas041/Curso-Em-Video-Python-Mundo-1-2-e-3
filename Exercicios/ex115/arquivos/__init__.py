import os
from interface import linha


def cadastrar(nome='', idade=0):
    tamLinha = 40
    strIdade = str(f'{idade} anos')
    calcIdade = tamLinha - len(strIdade)
    frase = f'{nome:<{calcIdade}}{strIdade:>}'
    try:
        with open('Pessoas.txt', 'a', newline='') as arquivo:
            arquivo.write(frase + os.linesep)
    except:
        print(f'\nErro ao cadastrar {nome}')
    else:
        print(f'\n{nome} cadastrado com sucesso.')


def listarCadastros():
    try:
        print(linha())
        print(f'{"Pessoas cadastradas":^{len(linha())}}')
        print(linha())
        with open('Pessoas.txt', 'r') as arquivo:
            for pessoa in arquivo:
                print(pessoa)
    except:
        print(linha())
        print(f'{"Sem pessoas cadastrada na lista.":^{len(linha())}}')
        print(linha())
