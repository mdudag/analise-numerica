# Maria Eduarda Guedes Alves
# Metodo da Eliminacao de Gauss - Exercicio 4.3

# ==================== Guardando Entradas ====================
import numpy as np

matriz = []

with open('file.txt', 'r') as file:
    n=eval(file.readline())         # Tamanho da matriz A
    # Elementos da matriz A com o vetor b
    for i in range(n):
        elementos = list(map(float, file.readline().split())) # Separar os elementos da linha e converte-los para float
        matriz.append(elementos)        # Adicionar a linha a matriz

col=n+1     # quantidade de colunas: matriz A + vetor b
A = np.array(matriz).reshape(n,col)
bi = np.delete(A, np.s_[0:col-1], axis=1)   # Guardando o vetor b

# ==================== Modificando A e b ====================

print('\n==================== Modificando A e b ====================')
print(f'\nA0:\n{A}\n')

i=0
while i<n-1:
    pivo=A[i][i]

    # Pivoteamento
    if pivo==0:
        l = np.argmax(A[i+1:, i])
        if A[l][i]>0:
            A[i][i], A[l][i] = A[l][i], A[i][i].copy()
        else: i+=1; continue

    j=i+1
    while j<n:
        mL = A[j][i]/pivo

        k=i
        while k<col:
            A[j][k] -= mL * A[i][k]
            k+=1
        j+=1
    i+=1
    print(f'\nA{i}:\n{np.round(A,5)}\n') # Arredondando vetor com 5 casas decimais
     
# Separando a matriz A do vetor b
bf = np.delete(A, np.s_[0:col-1], axis=1)
A = np.delete(A, col-1, axis=1)

# ==================== Encontrando Valor de x ====================

x = np.empty((n,1))     # Criando x

i=n-1      
while i>=0:   
    x[i][0] = bf[i][0]
    
    j=i+1
    while j<n:
        x[i][0] -= A[i][j]*x[j][0]
        j+=1

    x[i][0] /= A[i][i]
    i-=1

# ==================== Impressoes ==================== 

print('\n==================== Impressoes Finais ====================')
# Valores arredondados com 5 casas decimais
print(f'\nMatriz A:\n{np.round(A, 5)}\n'
      f'\nVetor b inicial: \n{bi}\n'
      f'\nVetor b final: \n{np.round(bf, 5)}\n' 
      f'\nVetor x:\n{np.round(x, 5)}\n')

# ==================== Teste ==================== 

print('\n==================== Testando x nas Equacoes ====================\n')

f = [lambda x1,x2,x3,x4,x5,x6,x7,x8,x9: -x1 + (x2+x4)/4,
     lambda x1,x2,x3,x4,x5,x6,x7,x8,x9: -x2 + (x1+x3+x5)/4,
     lambda x1,x2,x3,x4,x5,x6,x7,x8,x9: -x3 + (x2+x6)/4,
     lambda x1,x2,x3,x4,x5,x6,x7,x8,x9: -x4 + (x1+x5+x7)/4,
     lambda x1,x2,x3,x4,x5,x6,x7,x8,x9: -x5 + (x2+x4+x6+x8)/4,
     lambda x1,x2,x3,x4,x5,x6,x7,x8,x9: -x6 + (x3+x5+x9)/4,
     lambda x1,x2,x3,x4,x5,x6,x7,x8,x9: -x7 + (x4+x8+1)/4,
     lambda x1,x2,x3,x4,x5,x6,x7,x8,x9: -x8 + (x5+x7+x9+1)/4,
     lambda x1,x2,x3,x4,x5,x6,x7,x8,x9: -x9 + (x6+x8+1)/4]

j=0
for i in f:
    j+=1 
    print(f'Equacao {j}: {np.round(i(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8]), 5)}')
print()
