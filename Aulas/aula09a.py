frase = 'Curso em Video Python'


# 3 aspas para escrever textos:
# print("""Lorem Ipsum is simply dummy text of the printing and typesetting industry.
# Lorem Ipsum has been the industry's standard dummy text ever since the
# 1500s, when an unknown printer took a galley""")


# sempre começa da contagem '0'


print('')
print('-'*10)
print('')
# PEGAR UMA LETRA
print(frase[9])

# Vai pegar do nº incial ao final
print(frase[9:13])  # para de contar no ultimo

# vai pegar as letras entre 9 e 21 pulando x casas
print(frase[9:21:2])

# Comprimento da frase
print(len(frase))

# conta as letras selecionadas
print(frase.count('o'))

# contagem de string com fatiamento
print(frase.count('o', 0, 13))

# Procura letras e informa a casa que ele começa
print(frase.find('deo'))

# Caso a palavra nao exista sera informado "-1" pois nao existe
print(frase.find('Android'))

print('Curso' in frase)

# trocar palavras(reescreve)
print(frase.replace('Python', 'Android'))

# Ira rescrever todas as letras em minusculas ficaram em maiuscolas(fora as que ja sao maiuscolas)
print(frase.upper())

# Ira rescrever todas as letras em minusculo(fora as que ja estao)
print(frase.lower())

# Vai jogar a string inteira pra minuscola, e deixara a primeira letra em maiuscola
print(frase.capitalize())

# Vai analisar quantas palavras tem com base nos espaços e vai fazer uma quebra de palavra
print(frase.title())

frase = '   Aprenda Python  '
# Remove espaços inuteis no inicio e no fim da frase
print(frase.strip())

# 'Right' remove espaços da direita
print(frase.rstrip())

# 'Left' remove espaços da esquerda
print(frase.lstrip())

# DIVISAO
frase = 'Curso em Video Python'
# Divide palavras na String(tecnicamente gera um lista)
dividido = frase.split()
print(dividido)
# Junçao
# Justa as palavras
print('-'.join(frase))
