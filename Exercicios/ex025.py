# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

print('')
print('-'*10)
print('')

nome = str(input('Digite o nome: ')).strip().title()

print('O seu nome tem silva? {}'.format('Silva' in nome))
