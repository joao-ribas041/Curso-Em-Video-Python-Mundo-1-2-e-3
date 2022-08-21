# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles(desconsiderando o flag).

somador = cont = 0
while True:
    n = int(input('Digite um número para soma [999 finaliza]: '))
    if n == 999:
        break
    somador += n
    cont += 1

print(f'A soma dos {cont} valores foi {somador}!')
