# Adicione ao módulo moeda.py criada nos desafios anteriores uma função chamada resumo(),
# que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.

import moeda

v = float(input('Digite o valor: R$'))
pa = float(input('Porcentagem de aumento: '))
pr = float(input('Porcentagem de redução: '))
moeda.resumo(v, pa, pr)
