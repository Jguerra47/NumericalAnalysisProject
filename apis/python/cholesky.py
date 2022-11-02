import numpy as np
from cmath import sqrt
from prettytable import PrettyTable

def cholesky(A,n):
    #L = np.zeros((n,n), dtype=np.complex_)
    #U = np.zeros((n,n), dtype=np.complex_)
    L = [[0 for j in range(n)] for i in range(n)]
    U = [[0 for j in range(n)] for i in range(n)]

    for k in range(n):
        suma1 = 0
        for p in range(0,k):
            suma1 += L[k][p]*U[p][k]
        L[k][k] = sqrt(A[k][k]-suma1) #Soporte para numeros complejos
        U[k][k] = L[k][k]
        for i in range(k,n):
            suma2 = 0
            for p in range(k):
                suma2+=L[i][p]*U[p][k]
            L[i][k] = (A[i][k]-suma2)/(U[k][k])
        for j in range(k+1,n):
            suma3 = 0
            for p in range(k):
                suma3+= L[k][p]*U[p][j]
            U[k][j]= (A[k][j]-suma3)/(L[k][k])
        print("\nEtapa ",  k, ":" )

        print("\nMatriz L:")
        table = PrettyTable()
        table.field_names = [f"x{i}" for i in range(n)]
        for row in L:
            table.add_row(['({0.real:.4f} + {0.imag:.2f}i)'.format(i) for i in row])
        print(table)
        
        print("\nMatriz U:")
        table = PrettyTable()
        table.field_names = [f"x{i}" for i in range(n)]
        for row in U:
            table.add_row(['({0.real:.4f} + {0.imag:.2f}i)'.format(i) for i in row])
        print(table)
    #print ("\n\n\n Prueba: (analiza con la matriz ingresada)\n", np.dot(L,U))
    return L,U

#Llenar con la matriz y su tamaño
A = [[4,-1,0,3],[1,15.5,3,8],[0,-1.3,-4,1.1],[14,5,-2,30]]
n = 4
cholesky(A,n)