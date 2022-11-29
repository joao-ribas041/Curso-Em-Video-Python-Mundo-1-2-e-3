# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.
import moeda

preco = float(input('Digite um valor: '))
porc = float(input('Digite a porcentagem: '))

print(
    f'Aumentando {porc}% de R$ {preco:.2f} temos R$ {moeda.aumentar(preco, porc):.2f}')
print(
    f'Reduzindo {porc}% de R$ {preco:.2f} temos R$ {moeda.diminuir(preco, porc):.2f}')
print(
    f'Dobrando R$ {preco:.2f} temos R$ {moeda.dobro(preco):.2f}')
print(
    f'A metade de R$ {preco:.2f} é R$ {moeda.metade(preco):.2f}')
