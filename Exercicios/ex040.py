# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de de 5.0: Reprovado
# - Média entre 5.0 e 6.9: Recuperação
# - Média de 7.0 ou superior: Aprovado

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5.0:
    print('Você foi reprovado, estude mais!!!')
elif media >= 5.0 and media < 7:
    print('Você está na recuperação, estude!')
elif media >= 7.0:
    print('Você foi aprovado, parabens!')
print('sua média foi de {:.1f}.'.format(media))
