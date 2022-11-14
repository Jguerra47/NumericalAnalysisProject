import numpy as np
from Sustitution.sustitutions import *
from prettytable import PrettyTable

def pivot_matrix(M):
    m = len(M)                                                                                                                                                                                           
    id_mat = [[float(i ==j) for i in range(m)] for j in range(m)]
                                                                                                                                                                                           
    for j in range(m):
        row = max(range(j, m), key=lambda i: abs(M[i][j]))
        if j != row:                                                                                                                                                                                                                           
            id_mat[j], id_mat[row] = id_mat[row], id_mat[j]

    return id_mat
    
def prettyPrint(name,matrix):
    n = len(matrix)
    print(f"{name}: ")
    table = PrettyTable()
    table.field_names = [f"{name}{i}" for i in range(n)]
    table.add_rows(matrix)
    table.add_column("",[f"{name}{i}" for i in range(n)])
    print(table)

def lu_decomposition(A):
    n = len(A)
                                                                                                                                                                                                   
    L = [[0] * n for i in range(n)]
    U = [[0] * n for i in range(n)]
                                                                                                                                                                                       
    P = pivot_matrix(A)
    PA = np.dot(P, A)
                                                                                                                                                                                              
    for j in range(n):                                                                                                                                                                                               
        L[j][j] = 1.0

        for i in range(j+1):
            s1 = sum(U[k][j] * L[i][k] for k in range(i))
            U[i][j] = PA[i][j] - s1
                                                                                                                                                             
        for i in range(j, n):
            s2 = sum(U[k][j] * L[i][k] for k in range(j))
            L[i][j] = (PA[i][j] - s2) / U[j][j]

        print(f"stage {j+1}")
        prettyPrint("L",L)
        prettyPrint("U",U)
    return (P, L, U)


A = [[4,-1,0,3],[1,15.5,3,8],[0,-1.3,-4,1.1],[14,5,-2,30]]
b = [[1],[1],[1],[1]]
n = len(A)
P, L, U = lu_decomposition(A)

z=sustProg(L,b,n)
x=sustRegr(U,z,n)


table = PrettyTable()
table.field_names = [f"x{i}" for i in range(len(A))]
table.add_row(x)
print("\nX:")
print(table)