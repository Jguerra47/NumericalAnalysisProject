import sympy as sm 
import numpy as np

from numericApp.methods.LinearEquations.Sustitution.regSus import regSus

x = sm.symbols('x')

def elimination(Ab,n):
    procedure = []  
                                                                
    for k in range(n):
        
        for i in range(k+1,n):
            
            if(Ab[k][k] == 0):
                print("Division by 0, Gaussian elimination is not possible.")
                return Ab, procedure #HANDLEAR ERROR 
                
            multiplier = Ab[i][k]/Ab[k][k]
            
            for j in range(k, n+1):
                Ab[i,j] = Ab[i,j] - multiplier*Ab[k,j]
        procedure.append(Ab.tolist().copy())
    return Ab, procedure


def gaussSimple(A,b):
    A = np.array(A)
    b = np.array(b)
    n = len(b)
    Ab = np.append(A,b, axis = 1)
    Ab, procedure = elimination(Ab,n)

    A = Ab[:,0:n-1]
    b = Ab[:,n-1]

    x = regSus(Ab,n)

    # for i in range(1,n+1,1):
    #     print("x" + str(i) + " = " + str(x[i-1]))
    return x, procedure

# A = np.array([[10,20,-60.8319,8],[1,1,-2.1416,0],[17,-14,40.9823,20],[1,4,-12.5664,1]],dtype='float')
# b = np.array([[1],[1],[1],[1]], dtype ='float')

# gaussSimple(A,b)