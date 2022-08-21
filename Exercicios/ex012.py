# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preço = float(input('Digite o valor do produto: R$'))

novo = preço - (preço * 5 / 100)
print(novo)
