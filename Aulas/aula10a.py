# tempo = int(input('Quantos anos tem seu carro?'))
# if tempo<=3:
#     print('Carro novo')
# else:
#     print('Carro velho')
# print('------fim------')

# if simplificado
# print('carro novo' if tempo<=3 else 'carro velho')

# nome = str(input('Qual é seu nome? '))
# if nome == 'João':
#     print('Que nome lindo voce tem.')
# else:
#     print('Seu nome é tao normal!')
# print('Bom dia {}!'.format(nome))


n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2

print('A sua média foi de {:.1f}.'.format(m))

if m >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
    print('Aprovado!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')
    print('Reprovado!')

print('FIM')
