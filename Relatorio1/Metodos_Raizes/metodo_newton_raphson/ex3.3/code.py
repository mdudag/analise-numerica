# Discente: Maria Eduarda Guedes Alves
# Metodo Newton-Raphson - Exercicio 3.6

import math as math
import sympy as sp
# === Abrindo arquivo para leitura ===
x=sp.Symbol('x')
with open('file.txt', 'r') as file:
    line_f0=file.readline() 
    x00=eval(file.readline())
    e0=eval(file.readline())

    line_f1=file.readline() 
    x01=eval(file.readline())
    e1=eval(file.readline())
    
f0=eval(line_f0)
f01=eval(line_f0, {"x": x, "math": sp})

f1=eval(line_f1)
f11=eval(line_f1, {"x": x, "math": sp})

def newton_raphson(f, f1, x0, e):
    # === Transformando a função em uma expressão sympy para usar a derivada de f: f_sp(x) ===
    f_deriv = sp.diff(f1(x), x)  # Derivada de f

    # === Função de convergência ===
    phi = lambda x0: x0 - f(x0)/(f_deriv.subs(x, x0)).evalf()
    x1 = phi(x0)

    f_x1 = f(x1)
    # Imprimindo valores
    print(f'\n\t  x0 |\t\tx1 |\t\t f(x) |\t\t   e |\n')
    print(f'{x0:12f}  {x1:12f}  {f_x1:12f}  \t{e}')

    while abs(f_x1) >= e:
        # Calculando valor, mais aproximado, de x_k+1 
        x0=x1
        x1 = phi(x0)
        f_x1 = f(x1)
        # Imprimindo valores
        print(f'{x0:12f}  {x1:12f}  {f_x1:12f}  \t{e}')
    print(f'\n\t  x0 |\t\tx1 |\t\t f(x) |\t\t   e |\n')

    return x1 

print('\n============ Buscando Raiz de T0.1 ==============')
T01 = newton_raphson(f0, f01, x00,e0) 

print('\n============ Buscando Raiz de T0.9 ==============')
T09 = newton_raphson(f1, f11, x01,e1) 

tempSub = T09-T01

print('\n============ Resultados ==============')
print(f'\nT01 = {T01} \t g(T01) = {f0(T01)}')
print(f'T09 = {T09} \t g(T09) = {f1(T09)}')
print(f'Tempo de Subida: {round(tempSub,5)}\n')
