import math as math

# Abrindo arquivo para leitura
with open('file.txt', 'r') as file:
    f=eval(file.readline())
    x0=eval(file.readline())
    x1=eval(file.readline())
    e=eval(file.readline())

def sec(x0, x1, f_x0, f_x1):
    return (f_x1*x0 - f_x0*x1) / (f_x1-f_x0)

def secante(f, x0, x1, e):
    x2 = sec(x0, x1, f(x0), f(x1))
    f_x2 = f(x2)

    # Imprimindo valores
    print(f'\n\t  x0 |\t\tx1 |\t      x2 |\t\t f(x2) |\t\t   e |\n')
    print(f'{x0:12f}  {x1:12f}  {x2:12f}  {f_x2}  \t{e}')

    while abs(f_x2) >= e: 
        x0, x1 = x1, x2
        x2 = sec(x0, x1, f(x0), f(x1))
        f_x2 = f(x2)

        print(f'{x0:12f}  {x1:12f}  {x2:12f}  {f_x2}  \t{e}')
    print(f'\n\t  x0 |\t\tx1 |\t      x2 |\t\t f(x2) |\t\t   e |')

    return x2
    
print('\n============ Buscando Raiz ==============')
val = secante(f, x0, x1, e) 

print('\n============ Resultados ==============')
print(f'Valor: {round(val,5)}\nf(x) = {round(f(val),5)}\n')
