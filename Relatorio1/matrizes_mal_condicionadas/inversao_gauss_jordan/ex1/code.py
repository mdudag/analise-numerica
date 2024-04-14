# Discente: Maria Eduarda Guedes Alves
# Invercao pelo Metodo de Gauss-Jordan

# ==================== Guardando Entradas ====================

import numpy as np

matriz = []

with open('file.txt', 'r') as file:
    n=eval(file.readline())         # Tamanho da matriz A
    for i in range(n):
        # Elementos da matriz A
        elementos = list(map(float, file.readline().split())) # Separar os elementos da linha e converte-los para float
        matriz.append(elementos)        # Adicionar a linha a matriz

col=2*n     # quantidade de colunas: matriz A + matriz identidade

# Matriz identidade de tamanho n
i=0; I = np.zeros((n,n))
while i<n:
    I[i][i]=1; i+=1

Ai = np.array(matriz).reshape(n,n)  # Matriz A original

A = np.zeros((n, col))      # Cria uma nova matriz zerada com n linhas e n+3 colunas
A[:, :n] = Ai               # Copia a matriz Ai para a nova matriz
A[:, n:] = I                # Copia a matriz identidade para a nova matriz

print(f'A: \n{A}\n')

# ==================== Modificando A ====================

print('\n==================== Modificando A ====================')

# Modificacao de cima para embaixo
i=0
while i<n-1:
    pivo=A[i][i]

    j=i+1
    while j<n:
        mL = A[j][i]/pivo

        k=i
        while k<col:
            A[j][k] -= mL * A[i][k]
            k+=1
        j+=1
    A[i] = A[i]/pivo  # Dividindo toda linha do pivo atual por ele
    i+=1

    print(f'\nA:\n{np.round(A,5)}\n') # Arredondando vetor com 5 casas decimais

# Modificacao de baixo para cima
i=n-1
while i>0:
    pivo=A[i][i]

    j=i-1
    while j>=0:
        mL = A[j][i]/pivo

        k=i
        while k<col:
            A[j][k] -= mL * A[i][k]
            k+=1
        j-=1
    A[i][i:col] /= pivo  # Dividindo a linha do pivo atual por ele
    i-=1

    print(f'\nA:\n{np.round(A,5)}\n') # Arredondando vetor com 5 casas decimais

# Separando a matriz inversa de A 
Af = np.array(A[:, n:])

# ==================== Testando Matriz ====================

print('\n==================== Testando Matriz ====================')
# Verificando se o produto das matrizes e igual a matriz identidade
print(f'\nAqui deve aparecer uma matriz identidade:\n{np.round(np.dot(Ai,Af), 5)}\n')

# ==================== Impressoes ==================== 

print('\n==================== Impressoes Finais ====================')
# Valore arredondados com 5 casas decimais
print(f'\nMatriz Ai:\n{Ai}\n'
      f'\nMatriz Af: \n{np.round(Af, 8)}\n')
