# Discente: Maria Eduarda Guedes Alves
# Metodo de Jacobi - Exercicio 5.2

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

# Verificacao de colunas, depois linhas
i=0; ok=True
while i<2:
    j=0; ok=True
    while j<n and ok:
        matriz_soma = np.sum(A, axis=i)
        
        if A[j][j] <= matriz_soma[j]-A[j][j]:
            ok=False
        j+=1
    i+=1

    if ok==True: break

# ==================== Iteracoes de x ====================

print('\n==================== Iteracoes ====================')
if ok==True:    # Se o criterio foi atendido
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

        xcomp = np.max(np.abs(x1 - x0))/np.max(np.abs(x1))
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

print('\n==================== Aproximacao de A*x = b ====================\n')
print(f'Valor de b:\n{b}'
      f'\n\nValor de b resultante de A*x:\n{np.dot(A,x1)}\n')
