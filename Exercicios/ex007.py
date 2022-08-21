# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua media.
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2)/2
print('A media do aluno é de: {:.1f}'.format(media))

