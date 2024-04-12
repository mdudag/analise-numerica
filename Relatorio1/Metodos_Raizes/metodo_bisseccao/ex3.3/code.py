# Discente: Maria Eduarda Guedes Alves
# Metodo da Bisseccao - Exercicio 3.3

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
    
def bisseccao(f,a,b,e):
    # Verificacao de raiz em [a,b]
    if f(a)*f(b) >= 0:
        print('Nao existe raiz')
        exit()

    # Analisando se já encontramos a raiz
    x = (b+a)/2; f_x = f(x)

    # Imprimindo valores
    print(f'\n\t  a |\t\tb |\t      x |\t\t f(x) |\t\t   e |\n')
    print(f'{a:12f}  {b:12f}  {x:12f}  {f_x}  \t{e}')

    while abs(f_x) >= e:   
        # Mudando intervalo  
        if f(a)*f_x < 0:
            b=x
        else: a=x 

        # Renovando valor de x
        x = (b+a)/2; f_x = f(x)

        # Imprimindo novos valores
        print(f'{a:12f}  {b:12f}  {x:12f}  {f_x}  \t{e}')
    print(f'\n\t  a |\t\tb |\t      x |\t\t f(x) |\t\t   e |')
        
    return x

print('\n============ Buscando Raiz de T0.1 ==============')
T01 = bisseccao(f0,a0,b0,e0) 

print('\n============ Buscando Raiz de T0.9 ==============')
T09 = bisseccao(f1,a1,b1,e1) 

tempSub = T09-T01

print('\n============ Resultados ==============')
print(f'\nT01 = {T01} \t g(T01) = {f0(T01)}')
print(f'T09 = {T09} \t g(T09) = {f1(T09)}')
print(f'Tempo de Subida: {round(tempSub,5)}\n')
