import sympy as sm 
import numpy as np
from numericApp.Exceptions.exception import CustomException
from numericApp.methods.LinearEquations.Sustitution.regSus import regSus

x = sm.symbols('x')

def partialPivot(Ab,n):
    auxM = abs(Ab[n,n])
    auxI = n
    for i in range(n,len(Ab)):
        print(abs(Ab[i,n]))
        if auxM < abs(Ab[i,n]):
            auxI = i
            auxM = abs(Ab[i,n])
            
    Ab[n,:],Ab[auxI,:] = Ab[auxI,:].copy(),Ab[n,:].copy()
    print(Ab)
    return Ab

def partialPivotElimination(Ab,n):
    procedure = []
    for k in range(n):
        # Ab = partialPivot(Ab,n)
        Ab = partialPivot(Ab,k)

        for i in range(k+1,n):
            if(Ab[k][k] == 0):
                raise CustomException("The system has multiple solutions")
                
            multiplier = Ab[i][k]/Ab[k][k]
            
            for j in range(k, n+1):
                Ab[i,j] = Ab[i,j] - multiplier*Ab[k,j]
        procedure.append(Ab.tolist().copy())
    return Ab, procedure

def gaussPartialPivot(A,b):
    #Validation
    aux = np.array(A)
    if not np.linalg.det(aux):
        raise CustomException("The determinant of the matrix cannot be zero")

    Ab = np.append(A,b, axis = 1)
    n = len(Ab)
    Ab, procedure = partialPivotElimination(Ab,n)
    x = regSus(Ab,n)

    # for i in range(1,5):
    #     print("x" + str(i) + " = " + str(x[i-1]))
    return x, procedure


# A = np.array([[10,20,-60.8319,8],[1,1,-2.1416,0],[17,-14,40.9823,20],[1,4,-12.5664,1]],dtype='float')
# b = np.array([[1],[1],[1],[1]], dtype ='float')

# gausPartialPivot(A,b,4)