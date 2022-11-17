import numpy as np
from prettytable import PrettyTable
from numericApp.methods.LinearEquations.Sustitution.sustitutions import *

def crout(A):
    n = len(A)
    L = np.zeros((n,n))
    U = np.zeros((n,n))
    for i, j in zip(range(n), range(n)): U[i][j] = 1
    for i, j in zip(range(n), range(n)): L[i][j] = 1

    stages = []
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
        stages.append([L,U])
    return stages


def croutAns(A,b):
    stages = crout(A)
    n = len(A)
    # for k in range(len(stages)):
    #     print("\nStage ",  k+1, ":" )

    #     print("\nMatrix L:")
    #     table = PrettyTable()
    #     table.field_names = [f"x{i}" for i in range(n)]
    #     for row in stages[k][0]:#L
    #         table.add_row(["%.5f"%i for i in row])
    #     print(table)
                
    #     print("\nMatrix U:")
    #     table = PrettyTable()
    #     table.field_names = [f"x{i}" for i in range(n)]
    #     for row in stages[k][1]:#U
    #         table.add_row(["%.5f"%i for i in row])
    #     print(table)
    L = stages[-1][0]
    U = stages[-1][1]

    #Apply sustitution
    z = sustProg(L,b,n)
    x = sustRegr(U,z,n)
    
    # #Show answer
    # ans = PrettyTable()
    # ans.field_names = [f"x{i}" for i in range(n)]
    # ans.add_row(["%.5f"%i for i in x])
    # print("\nAnswer: ")
    # print(ans)
    return stages, x

#Fill matrix
A = np.array([[4,-1,0,3],[1,15.5,3,8],[0,-1.3,-4,1.1],[14,5,-2,30]])
b = np.array([[1],[1],[1],[1]])

croutAns(A,b)
