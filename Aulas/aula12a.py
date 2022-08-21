nome = str(input('Qual é o seu nome? '))
if nome == 'João':
    print('Que lindo nome você tem.')
elif nome == 'Pedro' or nome == 'Felipe' or nome == 'Igor' or nome == 'Lucas':
    print('Que nome popular você tem aqui no Brasil!')
elif nome in 'Mariana Osmarine Regiane Maria Iara':
    print('Belo nome feminino.')
else:
    print('Que nome normal você tem.')

print('Tenha um bom dia, {}!'.format(nome))
