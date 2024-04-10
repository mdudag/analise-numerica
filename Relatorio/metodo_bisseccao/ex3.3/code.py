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

    # Para análise inicial, para ver se já encontramos a raiz
    x = (b+a)/2; f_x = f(x)

    print(f'\na: {a}\nb: {b}\nx: {x}\nf(x): {f_x}\ne: {e}')
    while abs(f_x) >= e:     # mais simples e direto 
        if f(a)*f_x < 0:
            b=x
        else: a=x 

        # e = (b-a) / a        # (bk-ak) / ak     
        x = (b+a)/2; f_x = f(x)
        print(f'\n\na: {a}\nb: {b}\nx: {x}\nf(x): {f_x}\ne: {e}')

    return x

T01 = bisseccao(f0,a0,b0,e0) 
print(f'T01 = {T01}, f0(T01) = {f0(T01)}\n')

print(' ==========================')

T09 = bisseccao(f1,a1,b1,e1) 
print(f'T09 = {T09}, f0(T09) = {f0(T09)}\n')

tempSub = T09-T01
print(f'tempSub: {tempSub}\n')
