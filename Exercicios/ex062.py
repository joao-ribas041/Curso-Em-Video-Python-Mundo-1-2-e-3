# Melhore o DESAFIO 051, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar 0 termos.

termo = int(input('Digite um termo: '))
razão = int(input('Digite a razão: '))
cont = int(1)
conttermos = int(0)
termoextra = int(10)

while termoextra != 0:
    while cont <= termoextra:
        print('{}'.format(termo), end='')
        print(' > ' if cont < termoextra else ' > PAUSA', end='')
        termo += razão
        cont += 1
        conttermos += 1
    print()
    termoextra = int(input('Quantos termos você quer a mais? '))
    cont = 1
print('Progressão finalizada com {} termos mostrados.'.format(conttermos))
