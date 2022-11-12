# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com
# os parênteses aberto e fechados na ordem correta.
expressao = str(input('Digite a expressao para teste: '))
lista = []
for caracter in expressao:
    if caracter == '(':
        lista.append('(')
    elif caracter == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break

if len(lista) == 0:
    print('Expressao correta.')
else:
    print('Expressao errada.')
print(f'Lista da expressão: ')
