import math as math

# Abrindo arquivo para leitura
with open('file.txt', 'r') as file:
    f0=eval(file.readline())
    x00=eval(file.readline())
    x10=eval(file.readline())
    e0=eval(file.readline())

    f1=eval(file.readline())
    x01=eval(file.readline())
    x11=eval(file.readline())
    e1=eval(file.readline())

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
    
print('\n============ Buscando Raiz de T0.9 ==============')
T01 = secante(f0, x00, x10, e0)

print('\n============ Buscando Raiz de T0.9 ==============')
T09 = secante(f1, x01, x11, e1)

tempSub = T09-T01

print('\n============ Resultados ==============')
print(f'\nT01 = {T01} \t g(T01) = {f0(T01)}')
print(f'T09 = {T09} \t g(T09) = {f1(T09)}')
print(f'Tempo de Subida: {round(tempSub,5)}\n')
