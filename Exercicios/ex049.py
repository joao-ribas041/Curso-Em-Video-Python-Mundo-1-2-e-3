# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando o laço for.

print('TABUADA')
tabuada = int(input('Digite um valor: '))
i = int(input('Tabuada do 0 até o ... '))
print()
print('Tabuada do {}'.format(tabuada))
for t in range(0, i+1):
    print('{} x {:2} = {}'.format(tabuada, t, tabuada*t))
print('fim')
