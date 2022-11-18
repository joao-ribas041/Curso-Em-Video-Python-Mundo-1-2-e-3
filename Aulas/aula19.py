""" pessoas = {'nome': 'Joao', 'sexo': 'M', 'idade': 20}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print('')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

pessoas['nome'] = 'Mariana'
for k, v in pessoas.items():
    print(f'{k} = {v}')
 """

""" brasil = []
estado1 = {'uf': 'Paraná', 'sigla': 'PR'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['uf']) """

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa": '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())


for e in brasil:
    for k, v in e.items():
        print(f'{k} é {v}')
