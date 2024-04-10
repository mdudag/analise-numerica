# Abrindo arquivo para leitura e obtenção dos dados
with open('file.txt', 'r') as file:
    f=eval(file.readline())
    a=eval(file.readline())
    b=eval(file.readline())
    e=eval(file.readline())     # bi - ai

# Verificacao de raiz em [a,b]

if f(a)*f(b) >= 0:
    print('Nao existe raiz')
    exit()

# Para análise inicial, para ver se já encontramos a raiz
x = (b+a)/2; f_x = f(x)

while abs(f_x) > e:
    f_a = f(a); f_b = f(b)

    if f_a*f_x < 0:
        b=x
    else: a=x 

    x = (b+a)/2; f_x = f(x) 

print(f'x = {x}, f(x) = {f(x)}')
