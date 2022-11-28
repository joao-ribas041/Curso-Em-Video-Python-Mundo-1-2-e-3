# Faça um programa que tenha uma função notas() que pode receber várias notas de
# alunos e vai retornar um dicionário com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação(opcional)
# Adicione tambem as docstrings da função.

def notas(*notas, situacao=False):
    """
    :param: notas (float): notas da sala 
    :param: situacao (bool, optional): informa a situação com base na media. Defaults to False.

    Returns:
        dict: dicionario com as informações das notas
    """

    sala = {}
    maior = menor = media = 0
    sala['total'] = len(notas)

    for i, nota in enumerate(notas):
        media += nota
        if i == 0:
            maior = menor = nota
        else:
            if nota > maior:
                maior = nota
            if nota < menor:
                menor = nota

    media = media / len(notas)
    sala['maior'] = maior
    sala['menor'] = menor
    sala['media'] = media

    if situacao == True:
        if media < 6:
            sala['situação'] = 'RUIM'
        elif media < 7:
            sala['situação'] = 'RAZOAVEL'
        elif media < 9:
            sala['situação'] = 'BOA'
        else:
            sala['situação'] = 'EXELENTE'

    return sala


totalNotas = notas(6, 7, 4.5, 9, 3, situacao=True)
print(totalNotas)
help(notas)
