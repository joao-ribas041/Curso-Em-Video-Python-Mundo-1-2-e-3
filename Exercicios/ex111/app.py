# Crie um pacote chamado utilidades que tenha dois módulos internos chamados moeda e dado.
# Transfira todas as funções utilizadas nos desafios 107, 108 e 109
# para o primeiro pacote e mantenha tudo funcionando.

from utilidades import moeda

v = float(input('Digite o valor: R$'))
pa = float(input('Porcentagem de aumento: '))
pr = float(input('Porcentagem de redução: '))

moeda.resumo(v, pa, pr)
