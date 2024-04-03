import numpy as np
# lambda x1, x2: 3*x1 - x2 + 1
matriz = []
vetor  = []
f = []

with open('file.txt', 'r') as file:
    n=eval(file.readline())
    i=0
    while i<n:
        f[i] = eval(file.readline())
    # Separar os elementos da linha e convertê-los para float
    elementos = list(map(float, file.readline().split()))
    # Adicionar a linha à matriz
    matriz.append(elementos)

    # Separar os elementos da linha e convertê-los para float
    elementos = list(map(float, file.readline().split()))
    vetor.append(elementos)


A = np.array(matriz).reshape(n,n)
b = np.array(vetor)

# ======
# M = np.empty(n,n)
# M[0] = A[0]

i=0
while i<n-1:
    pivo=A[i][i]

    j=i+1
    while j<n:
        mL = A[j][i]/pivo

        k=0
        while k<=n:
            A[j][k] = A[j][k] - mL * A[i][k]
            ++k
        ++j
    ++i

# ==== 
        
# Separando a matriz A do vetor b
A = np.remove(A, n-1, 1)
b = np.remove(A, np.s_[0:n-2], exit=1)

x = np.empty(n)

i=n-1; 
while i>=0:
    x[i] = b[i]
    
    j=i+1

    while j<n:
        x[i] -= A[i][j]*x[j]

    x[i] /= A[i][i]

# ==== teste
    
print(f'Equacao 1: {f[0](x[0], x[1], x[2])}')
print(f'Equacao 2: {f[1](x[0], x[1], x[2])}')
print(f'Equacao 3: {f[2](x[0], x[1], x[2])}')
