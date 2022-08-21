# Crie um programa que leia o nome de uma cidade e diga se ela começa ou nao com o nome "SANTO".

print('')
print('-'*10)
print('')

cidade = str(input('Digite o nome de sua cidade: ')).strip().title()
cidadedividido = cidade.split()
print("O nome da cidade {} com o nome 'Santo'.".format(cidade[:5] == 'Santo'))
