# Discente: Maria Eduarda Guedes Alves
# Método da Posicao Falsa

import math as math

# Abrindo arquivo para leitura e obtenção dos dados
with open('file.txt', 'r') as file:
    f=eval(file.readline())
    a=eval(file.readline())
    b=eval(file.readline())
    e=eval(file.readline())

def posicao(a, b, f_a, f_b):
    return (a*f_b - b*f_a) / (f_b-f_a)

def posicao_falsa(f, a, b, e):
    # Verificacao de raiz em [a,b]
    if f(a)*f(b) >= 0:
        print('Nao existe raiz')
        exit()

    # Analisando se já encontramos a raiz
    x = posicao(a, b, f(a), f(b))
    f_x = f(x)

    # Imprimindo valores
    print(f'\n\t  a |\t\tb |\t      x |\t\t f(x) |\t\t   e |\n')
    print(f'{a:12f}  {b:12f}  {x:12f}  {f_x}  \t{e}')

    while abs(f_x) >= e:
        f_a = f(a); f_b = f(b)

        if f_a*f_x < 0:
            b=x
        else: a=x

        x = posicao(a, b, f_a, f_b)
        f_x = f(x)

        # Imprimindo valores
        print(f'{a:12f}  {b:12f}  {x:12f}  {f_x}  \t{e}')
    print(f'\n\t  a |\t\tb |\t      x |\t\t f(x) |\t\t   e |')

    return x

print('\n============ Buscando Raiz ==============')
val = posicao_falsa(f,a,b,e) 

print('\n============ Resultados ==============')
print(f'Valor: {val}\nf(x) = {f(val)}\n')
