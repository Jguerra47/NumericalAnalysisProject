import numpy as np
from prettytable import PrettyTable

def crout(A,n):
    L = np.zeros((n,n))
    U = np.zeros((n,n))
    for i, j in zip(range(n), range(n)): U[i][j] = 1

    for k in range(n):
        suma1 = 0.0
        for p in range(0,k):
            suma1 += L[k][p]*U[p][k]
        L[k][k] = A[k][k] - suma1
        for i in range(k+1,n):
            suma2 = 0.0
            for p in range(k):
                suma2 += L[i][p]*U[p][k]
            L[i][k] = (A[i][k]-suma2)/(U[k][k])
        for j in range(k+1,n):
            suma3 = 0.0
            for p in range(k):
                suma3 += L[k][p]*U[p][j]
            U[k][j]= (A[k][j]-suma3)/(L[k][k])
        print("\nEtapa ",  k , ":")

        print("\nMatriz L:")
        table = PrettyTable()
        table.field_names = [f"x{i}" for i in range(n)]
        for row in L:
            table.add_row(["%.5f"%i for i in row])
        print(table)
        
        print("\nMatriz U:")
        table = PrettyTable()
        table.field_names = [f"x{i}" for i in range(n)]
        for row in U:
            table.add_row(["%.5f"%i for i in row])
        print(table)
    return L,U

#Llenar con la matriz y su tamaño
A = np.array([[4,-1,0,3],[1,15.5,3,8],[0,-1.3,-4,1.1],[14,5,-2,30]])
n = 4
crout(A,n)