# Maria Eduarda Guedes Alves
# Metodo da Bisseccao - Exercicio 3.1

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
    print(f'\na: {a}\nb: {b}\nx: {x}\nf(x): {f_x}\ne: {e}')

    while abs(f_x) >= e:  
        # Mudando intervalo    
        if f(a)*f_x < 0:
            b=x
        else: a=x 

        # Renovando valor de x
        x = (b+a)/2; f_x = f(x)

        # Imprimindo valores
        print(f'\n\na: {a}\nb: {b}\nx: {x}\nf(x): {f_x}\ne: {e}')

    return x

print('\n============ Buscando Raiz ==============')
val = bisseccao(f,a,b,e) 

print('\n============ Resultados ==============')
print(f'Raiz da Equacao de Kepler: {val}\nf(x) = {f(val)}\n')
