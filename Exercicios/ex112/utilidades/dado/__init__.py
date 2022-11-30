def leiaDinheiro(msg):
    aprovado = False
    valor = 0
    while not aprovado:
        moeda = str(input(msg)).replace(',', '.').strip()

        if moeda.isalpha() or moeda == '':
            print('Por favor, informe um valor monetário válido.')
        else:
            valor = float(moeda)
            aprovado = True

    return valor
