# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiuscolas
# O nome com todas minuscolas.
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome.

print('')
print('-'*10)
print('')
nome = str(input('Digite o nome: ')).strip()

nome = nome.upper()
print('Com letras maiuscolas: {}.'.format(nome))
nome = nome.lower()
print('Com letras minuscolas: {}.'.format(nome))

nomedividido = nome.split()
print('O nome tem {} caracteres ao todo.'.format(len(nome) - nome.count(' ')))

print('O primeiro nome tem {} caracteres.'.format(len(nomedividido[0])))
