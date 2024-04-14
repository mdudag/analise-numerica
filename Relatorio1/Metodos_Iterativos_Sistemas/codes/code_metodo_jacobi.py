# Discente: Maria Eduarda Guedes Alves
# Metodo de Jacobi

# ==================== Guardando Entradas ====================

import numpy as np

matriz = []
vetor  = []

with open('file.txt', 'r') as file:
    n=eval(file.readline())     # Tamanho da matriz A

    for i in range(n):
        elementos = list(map(float, file.readline().split()))   # Separar os elementos da linha e converte-los para float    
        matriz.append(elementos)    # Adicionar a linha a matriz

    elementos = list(map(float, file.readline().split()))   # Separar os elementos da linha e converte-los para float
    vetor.append(elementos)     # Adicionar a linha ao vetor

    e=eval(file.readline())     # Precisao

A = np.array(matriz).reshape(n,n)
b = np.array(vetor).reshape(n,1)

# ==================== Condicao de Convergencia Diagonalmente Dominante ====================

def sumLinhas(linha):
    matriz_soma=0
    for i in linha:
        matriz_soma += i

    return matriz_soma

def max(x):
    max=x[0]
    for i in x[1:]:
        if i>max:
            max=i

    return max

# Verificacao de linhas, depois colunas
i=0; ok=True
while i<2:
    j=0; ok=True
    while j<n and ok:
        if i==0: matriz_soma = sumLinhas(A[i])    # Linhas
        else:    matriz_soma = sumLinhas(A[:,j])  # Colunas    
        
        if A[j][j] <= matriz_soma-A[j][j]:
            ok=False
        j+=1
    i+=1

    if ok==True: break

# ==================== Iteracoes de x ====================

print('\n==================== Iteracoes ====================')
if ok==False:    # Se o criterio não foi atendido
    print('\nCriterio nao atendido! \nNao há garantia de convergencia.')

x1=np.zeros((n,1))
print(f'\nx(0): \n{x1}')

c=1
while True:   # imitando estrutura "do while"
    x0=np.array(x1)

    i=0
    while i<n:
        xcomp=0
        x1[i][0] = b[i][0]

        j=0
        while j<n:
            if j!=i:
                x1[i][0] -= A[i][j]*x0[j][0]
            j+=1
        x1[i][0] /= A[i][i]
        
        i+=1

    xcomp = max(np.abs(x1 - x0))/max(np.abs(x1))
    
    print(f'\nx({c}): \n{x1}\n'
            f'\nValor de convergencia: {xcomp}\n')
    c+=1

    if xcomp < e: break

# ==================== Impressoes ==================== 

print('\n==================== Impressoes Finais ====================')
print(f'\nA:\n{A}\n'
      f'\nb:\n{b}\n'
      f'\ne: {e}\n'
      f'\nx de convergencia:\n{np.round(x1,4)}\n')
