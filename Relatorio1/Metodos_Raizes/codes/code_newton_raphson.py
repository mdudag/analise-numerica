# Discente: Maria Eduarda Guedes Alves
# Metodo Newton-Raphson - Exercicio 3.6

import math as math
import sympy as sp
# === Abrindo arquivo para leitura ===
x=sp.Symbol('x')
with open('file.txt', 'r') as file:
    line_f =file.readline() 
    x0=eval(file.readline())
    e=eval(file.readline())

f=eval(line_f)
f1=eval(line_f, {"x": x, "math": sp})

def newton_raphson(f, x0, e):
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

print('\n============ Buscando Raiz ==============')
val = newton_raphson(f,x0,e) 

print('\n============ Resultados Aproximados ==============\n')
print(f'Valor: {round(val,5)}\nf(x) = {round(f(val),5)}\n')
