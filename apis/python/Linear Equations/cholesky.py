import numpy as np
from cmath import sqrt
from prettytable import PrettyTable
from Sustitution.sustitutions import *

def cholesky(A):
    n = len(A)
    #L = np.zeros((n,n), dtype=np.complex_)
    #U = np.zeros((n,n), dtype=np.complex_)
    L = [[0 for j in range(n)] for i in range(n)]
    U = [[0 for j in range(n)] for i in range(n)]

    for k in range(n):
        suma1 = 0
        for p in range(0,k):
            suma1 += L[k][p]*U[p][k]
        L[k][k] = sqrt(A[k][k]-suma1) #Complex number handled
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
        print("\nStage ",  k, ":" )

        print("\nMatrix L:")
        table = PrettyTable()
        table.field_names = [f"x{i}" for i in range(n)]
        for row in L:
            table.add_row(['({0.real:.4f} + {0.imag:.2f}i)'.format(i) for i in row])
        print(table)
        
        print("\nMatrix U:")
        table = PrettyTable()
        table.field_names = [f"x{i}" for i in range(n)]
        for row in U:
            table.add_row(['({0.real:.4f} + {0.imag:.2f}i)'.format(i) for i in row])
        print(table)
    return L,U

#Fill matrix
A = np.array([[4,-1,0,3],[1,15.5,3,8],[0,-1.3,-4,1.1],[14,5,-2,30]])
b = np.array([[1],[1],[1],[1]])
L,U = cholesky(A)
n = len(A)

#Apply sustitution
z=sustProg(L,b,n)
x=sustRegr(U,z,n)

#Show answer
ans = PrettyTable()
ans.field_names = [f"x{i}" for i in range(n)]
ans.add_row(["%.5f"%i for i in x])
print("\nAnswer: ")
print(ans)