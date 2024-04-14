# Discente: Maria Eduarda Guedes Alves
# Condicao da Matriz

# ==================== Guardando Entradas ====================

import numpy as np

matriz1 = []
matriz2 = []

with open('file.txt', 'r') as file:
    n=eval(file.readline())         # Tamanho da matriz A
    
    for i in range(n):
        # Elementos da matriz A com o vetor b
        elementos = list(map(float, file.readline().split())) # Separar os elementos da linha e converte-los para float
        matriz1.append(elementos)        # Adicionar a linha a matriz

    for i in range(n):
        # Elementos da matriz A com o vetor b
        elementos = list(map(float, file.readline().split())) # Separar os elementos da linha e converte-los para float
        matriz2.append(elementos)        # Adicionar a linha a matriz

Ai = np.array(matriz1).reshape(n,n)
Af = np.array(matriz2).reshape(n,n)

# ==================== Calculo da Condicao da Matriz ==================== 

def sumLinhas(A,n):
    matriz_soma=[]

    for i in range(n):
        soma=0

        for j in range(n):
            soma += A[i][j]
        matriz_soma.append(soma)

    return matriz_soma

def maxLinha(x):
    max=x[0]
    for i in x[1:]:
        if i>max:
            max=i

    return max

mAi = maxLinha(sumLinhas(np.abs(Ai),n))
mAf = maxLinha(sumLinhas(np.abs(Af),n))

condA = mAi*mAf

# ==================== Impressoes ==================== 

print('\n==================== Impressoes Finais ====================')
print(f'\nResultado do calculo com matriz A:     {mAi}'
      f'\nResultado do calculo com inversa de A: {mAf}'
      f'\nCondicao da matriz: {condA}\n')
