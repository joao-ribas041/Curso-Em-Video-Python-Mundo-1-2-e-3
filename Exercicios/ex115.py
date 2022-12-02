# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um texto simples.
# O sitema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.

def cadastrar(nome='', idade=0):
    import os

    tamLinha = 40
    strIdade = str(f'{idade} anos')
    calcIdade = tamLinha - len(strIdade)
    frase = f'{nome:<{calcIdade}}{strIdade:>}'

    with open('Pessoas.txt', 'a', newline='') as arquivo:
        arquivo.write(frase + os.linesep)


def listarCadastros():
    import os
    linha = '-' * 40
    try:
        print(linha)
        print(f'{"Pessoas cadastradas":^{len(linha)}}')
        print(linha)

        with open('Pessoas.txt', 'r') as arquivo:
            for pessoa in arquivo:
                print(pessoa)

    except:
        print(linha)
        print(f'{"Sem pessoas cadastradas na lista":^{len(linha)}}')
        print(linha)


def menu():
    linha = '~' * 40

    while True:
        print('\n' + linha)
        print(f'{"Menu":^{len(linha)}}')
        print(linha)
        print('1 - Cadastrar novas pessoas.')
        print('2 - Ver pessoas cadastradas.')
        print('3 - Sair')
        print(linha)
        try:
            escolha = int(input('Sua escolha: '))
        except:
            print('Opção Invalida. ')
        else:
            if escolha == 1:

                n = str(input('Digite um nome: '))
                i = int(input('Digite sua idade: '))
                cadastrar(n, i)
            elif escolha == 2:
                listarCadastros()
            elif escolha == 3:
                break
            else:
                print('Opção Invalida. ')


menu()
