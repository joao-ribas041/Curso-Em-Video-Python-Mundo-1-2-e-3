# Adapte o código do desafio 107, criandouma função chamada moeda() que consiga
# mostrar os valores como um valor monetário formatado.
import moeda

v = float(input('Digite o valor: R$'))
p = float(input('Digite a porcentagem: '))

print(f'A metade de {moeda.moeda(v)} é {moeda.moeda(moeda.metade(v))}.')
print(f'O dobro de {moeda.moeda(v)} é {moeda.moeda(moeda.dobro(v))}.')
print(
    f'Aumentando {p:.0f}% de {moeda.moeda(v)} temos {moeda.moeda(moeda.aumentar(v, p))}.')
print(
    f'Diminuindo {p:.0f}% de {moeda.moeda(v)} temos {moeda.moeda(moeda.diminuir(v, p))}.')
