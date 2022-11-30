# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
# Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(),
# mas com uma validação de dados para aceitar apenas valores que sejam monetários.
from utilidades import moeda, dado

v = dado.leiaDinheiro('Digite o valor: R$')
pa = float(input('Porcentagem de aumento: '))
pr = float(input('Porcentagem de redução: '))
moeda.resumo(v, pa, pr)

