import sympy as sm 
import numpy as np 
from numericApp.methods.LinearEquations.Sustitution.sustitutions import *
from prettytable import PrettyTable

x = sm.symbols('x')

def prettyPrint(name,matrix):
    n = len(matrix)
    print(f"{name}: ")
    table = PrettyTable()
    table.field_names = [f"{name}{i}" for i in range(n)]
    table.add_rows(matrix)
    table.add_column("",[f"{name}{i}" for i in range(n)])
    print(table)

def LUGauss(A,b):
    A = np.array(A)
    b = np.array(b)
    
    n,m = A.shape
    L=np.zeros((n,n))
    U=np.zeros((n,n))
    U[0]=A[0]
    stages = []
    for k in range(n-1):
        L[k,k]=1
        for i in range(k+1,n):
            m=A[i,k]/A[k,k]
            L[i,k]=m
            for j in range(k,n):
                A[i,j]=A[i,j]-m*A[k,j]
                U[i,j]=A[i,j]
        # print("Stage ", k+1)
        # prettyPrint("L",L)
        # prettyPrint("U",U)
        stages.append([L,U])
    L[n-1,n-1]=1
    z=sustProg(L,b,n)
    x=sustRegr(U,z,n) 
    return stages,x

def LUGaus(A,b):
    stages,x = LUGauss(A,b)
    return stages,x

A = np.array([[4,-1,0,3],[1,15.5,3,8],[0,-1.3,-4,1.1],[14,5,-2,30]],dtype='float')
b = np.array([[1],[1],[1],[1]], dtype ='float')


# stages,x = LUGaus(A,b)
# print(stages)
# table = PrettyTable()
# table.field_names = [f"x{i}" for i in range(len(A))]
# table.add_row(x)
# print("\nX:")
# print(table)