# Discente: Maria Eduarda Guedes Alves
# Metodo de Eliminacao LU

# ==================== Guardando Entradas ====================

import numpy as np

matriz = []
vetor  = []

with open('file.txt', 'r') as file:
    n=eval(file.readline())

    elementos = list(map(float, file.readline().split()))   # Separar os elementos da linha e converte-los para float
    matriz.append(elementos)        # Adicionar a linha a matriz

    elementos = list(map(float, file.readline().split()))   # Separar os elementos da linha e converte-los para float
    vetor.append(elementos)         # Adicionar a linha ao vetor

A = np.array(matriz).reshape(n,n)
L = np.zeros((n,n))
U = np.empty((n,n)) 
b = np.array(vetor).reshape(3,1)

# ==================== Modificando LU ====================

print(f'\nA0:\n{A}\n')

i=0
while i<n-1:
    L[i][i]=1               # Diagonal principal de L com 1
    pivo=A[i][i]

    j=i+1
    while j<n:
        mL = A[j][i]/pivo
        L[j][i] = mL        # Adicionando mL na abaixo da diagonal principal de L

        k=0
        while k<n:
            A[j][k] -= mL * A[i][k]    # Modificando A
            k+=1
        j+=1
    i+=1
    print(f'\nA{i}:\n{A}\n')

   
L[n-1][n-1] = 1         # Posicao final que nao e preenchida no loop   
U=A

# ==================== Encontrando Valor de x ====================

x = np.empty((n,1))
y = np.empty((n,1))

# Vetor y
i=0  
while i<n-1:
    y[i][0] = b[i][0]

    j=0
    while j<i:
        y[i][0] -= L[i][j]*y[j][0]
        j+=1
    i+=1

# Vetor x
i=n-1
while i>=0:
    x[i][0] = y[i][0]

    j=i+1
    while j<n:
        x[i][0] -= U[i][j]*x[j][0]
        j+=1
    x[i][0] /= U[i][i]

    i-=1

# ==================== Impressoes ==================== 

print('\n==================== Impressoes Finais ====================')
# Valore arredondados com 5 casas decimais
print(f'\nMatriz L:\n{L}\n'
      f'\nMatriz U:\n{U}\n'
      f'\nVetor y:\n{y}\n'
      f'\nVetor x:\n{x}\n')
