""" def contador(i, f, p):
    
-> Faz uma contagem e mostra na tela.
: param i: início da contagem
: param f: fim da contagem
: param p: passo da contagem
: return: sem retorno
Função criada por Gustavo Guanabara do canal CursoemVideo.

    c = i
    while c <= f:
        print(c, end=' ')
        c += p
    print('fim')


contador(2, 10, 2)
help(contador) """


""" def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)
print(f'Os resultados foram {r1}, {r2} e {r3}')


def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')


n1 = 2
funcao()
print(f'N1 fora vale {n1}')
 """


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()

print(f'Os resultados são {f1}, {f2} e {f3}')


def ParOuImpar(num=0):
    if num % 2 == 0:
        return True
    else:
        return False


n = int(input('Digite um numero: '))
if ParOuImpar(n):
    print('É par')
else:
    print('É impar')
