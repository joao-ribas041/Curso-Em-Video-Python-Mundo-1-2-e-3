""" teste = []
teste.append('João')
teste.append(20)

galera = []
galera.append(teste[:])
teste[0] = 'Mariana'
teste[1] = 19
galera.append(teste[:])

print(galera) """

""" galera = [['João', 20], ['Mariana', 19], ['Peter', 11], ['Alan', 45]]

for pessoas in galera:
    # print(pessoas)
    
    for pessoa in pessoas:
        print(pessoa) """

cadastro = []
pessoas = []

for c in range(0, 3):
    cadastro.append(str(input(f'Digite o nome {c}: ')))
    cadastro.append(int(input(f'Digite a idade {c}: ')))
    pessoas.append(cadastro[:])
    cadastro.clear()

for pessoa in pessoas:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade')
