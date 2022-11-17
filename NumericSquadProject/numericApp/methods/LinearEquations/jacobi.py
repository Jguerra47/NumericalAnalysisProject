from prettytable import PrettyTable
from numpy import linalg
import numpy as np
table = PrettyTable()
 
def prettyPrint(name,matrix):
    n = len(matrix)
    table = PrettyTable()
    table.field_names = [f"{name}{i}" for i in range(n)]
    table.add_rows(matrix)
    table.add_column("",[f"{name}{i}" for i in range(n)])
    print(table)
 
def calculateNewJacobi(x0,a,b):
    x = []
    n = len(a)
    for i in range(0,n):
        sumi = 0
        for j in range(0,n):
            if(j != i):
                sumi = sumi + a[i][j]*x0[j]
        value = (b[i]- sumi)/a[i][i]
        x.append(value)
    return x
 
def norm(x):
    return linalg.norm(x) #norm2
        
 
def minus(x1,x0):
    x = []
    for i in range(0,len(x1)):
        x.append(x1[i]-x0[i])
    return x
    
def jacobi(niter,tol,x0,a,b):
    cont = 0
    dispersion = tol + 1
    matrix = []
    matrix.append([0,0] + x0)
    while(dispersion > tol and cont < niter ):
        x1 = calculateNewJacobi(x0,a,b)
        dispersion = norm (minus(x1, x0)) 
        x0 = x1
        cont = cont +1
        matrix.append([cont,dispersion] + x1)
    return [ matrix[-1][2+i] for i in range(len(matrix[-1])-2) ],matrix

def jacobi_Ans(a,b,initialValues):
    n = len(a)
    x,matrix = jacobi(100,1e-7,initialValues,a,b)
    
    # print("matrix")
    # print(matrix)

    D = np.diag((np.diag(a)))
    L = np.tril(a,-1)
    U = np.triu(a,1)

    Tmatrix = -1*np.dot(linalg.inv(D), U+L)


    # print("T Matrix:")
    # prettyPrint("T",Tmatrix)

    valor1 = np.linalg.eig(Tmatrix)
    lista = []
    for i in range(len(valor1)):
        lista.append(abs(valor1[i]))
    value = max(lista[0])
    
    # print("The spectral radius is: ")
    # print(value)
    
    # table = PrettyTable()
    # table.field_names = [f"x{i}" for i in range(n)]
    # table.add_row(x)
    # print("\nX:")
    # print(table)
    return x,Tmatrix,matrix,value

a = [[4, -1,   0,  3],
    [1, 15.5, 3,  8],
    [0, -1.3, -4, 1.1],
    [14, 5,   -2, 30]]
b = [1,1,1,1]
initialValues = [0,0,0,0]
jacobi_Ans(a,b,initialValues)