# Discente: Maria Eduarda Guedes Alves
# Método da Posicao Falsa - Exercicio 3.1

import math as math

# Abrindo arquivo para leitura e obtenção dos dados
with open('file.txt', 'r') as file:
    f0=eval(file.readline())
    a0=eval(file.readline())
    b0=eval(file.readline())
    e0=eval(file.readline())    

    f1=eval(file.readline())
    a1=eval(file.readline())
    b1=eval(file.readline())
    e1=eval(file.readline())

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

print('\n============ Buscando Raiz de T0.1 ==============')
T01 = posicao_falsa(f0,a0,b0,e0) 

print('\n============ Buscando Raiz de T0.9 ==============')
T09 = posicao_falsa(f1,a1,b1,e1) 

tempSub = T09-T01

print('\n============ Resultados ==============')
print(f'\nT01 = {T01} \t g(T01) = {f0(T01)}')
print(f'T09 = {T09} \t g(T09) = {f1(T09)}')
print(f'Tempo de Subida: {round(tempSub,5)}\n')
