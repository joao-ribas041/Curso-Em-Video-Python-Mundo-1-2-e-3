# faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele.

a = input('Digite um valor para comparação: ')
print('O tipo primitivo do valor é: ', type(a))
print('O valor tem espaços? ', a.isspace())
print('O valor tem numero? ', a.isnumeric())
print('O valor é alfabetico? ', a.isalpha())
print('O valor é alfanumerico? ', a.isalnum())
print('Está em maiúscolas? ', a.isupper())
print('Está em minúscolas? ', a.islower())
print('Está capitaliza? ', a.istitle())
