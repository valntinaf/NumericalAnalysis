# Una forma de factorizar matrices, es la factorización LU, en donde se buscan dos matrices L y U, triangular
# inferior y superior respectivamente que multiplicadas sean la matriz original.
import numpy as np

def lu(matriz):
    A = np.array(matriz)
    n = A.shape
    L = np.zeros(n)
    U = np.zeros(n)
    epsilon = np.finfo(np.float).eps
    for j in range(n[0]):
        if abs(A[j,j]) < epsilon:
            print('ERROR: pivote nulo')
            return None
        L[j,j] = 1.0
        for i in range(j+1,n[0]):
            L[i,j] = A[i,j]/A[j,j]
            for k in range(j+1,n[0]):
                A[i,k] = A[i,k] - L[i,j]*A[j,k]
        for k in range(j,n[0]):
            U[j,k] = A[j,k]

    return L, U

A=[[3,2,1],[4,9,1],[1,9,3]]
L,U=lu(A)
print(L)
print(U)
