# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.
# Ex: Ana Maria de Souza
# primeiro = Ana
# Ultimo = Souza

print('')
print('-'*10)
print('')

nome = str(input('Digite seu nome: ')).strip().title()
n = nome.split()


print('Primeiro nome: {}.'.format(n[0]))
print('Ultimo nome: {}.'.format(n[len(n)-1]))
