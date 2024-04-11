# Maria Eduarda Guedes Alves
# Metodo da bisseccao - Exercicio 3.6

import math as math

# Abrindo arquivo para leitura e obtenção dos dados
with open('file.txt', 'r') as file:
    f=eval(file.readline())
    a=eval(file.readline())
    b=eval(file.readline())
    e=eval(file.readline())     
    
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

        # Imprimindo valores
        print(f'{a:12f}  {b:12f}  {x:12f}  {f_x}  \t{e}')
    print(f'\n\t  a |\t\tb |\t      x |\t\t f(x) |\t\t   e |')
    
    return x

print('\n============ Buscando Raiz ==============')
val = bisseccao(f,a,b,e) 

print('\n============ Resultados Aproximados ==============\n')
print(f'Inclinacao: {round(val,5)}\nf(x) = {round(f(val),5)}\n')
