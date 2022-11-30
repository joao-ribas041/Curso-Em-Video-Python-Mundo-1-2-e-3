# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
import moeda

v = float(input('Digite o valor: R$'))
p = float(input('Digite a porcentagem: '))

print(f'A metade de {moeda.moeda(v)} é {moeda.metade(v, True)}.')
print(f'O dobro de {moeda.moeda(v)} é {moeda.dobro(v, True)}.')
print(
    f'Aumentando {p:.0f}% de {moeda.moeda(v)} temos {moeda.aumentar(v, p, True)}.')
print(
    f'Reduzindo {p:.0f}% de {moeda.moeda(v)} temos {moeda.diminuir(v, p, True)}.')
