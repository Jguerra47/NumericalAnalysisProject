import sympy as sm 
import numpy as np 
import math

x = sm.symbols('x')

def partialPivot(Ab,n):
    auxM = abs(Ab[n,n])
    auxI = n
    for i in range(n,len(Ab)):
      if auxM < abs(Ab[n,i]):
        auxI = i
    Ab[n,:],Ab[auxI,:] = Ab[auxI,:],Ab[n,:]
    
    return Ab

def partialPivotElimination(Ab,n):
    
    for k in range(n):
        # Ab = partialPivot(Ab,n)
        Ab = partialPivot(Ab,k)

        for i in range(k+1,n):
            
            if(Ab[k][k] == 0):
                print("Division by 0, Gaussian elimination is not possible.")
                return Ab
                
            multiplier = Ab[i][k]/Ab[k][k]
            
            for j in range(k, n+1):
                Ab[i,j] = Ab[i,j] - multiplier*Ab[k,j]
        print()
        print("================")
        print(Ab)
    
    return Ab

def gausPartialPivot(A,b,n):
    Ab = np.append(A,b, axis = 1)
    Ab = partialPivotElimination(Ab,n)
    x = regSus(Ab,n)

    for i in range(1,5):
        print("x" + str(i) + " = " + str(x[i-1]))


A = np.array([[10,20,-60.8319,8],[1,1,-2.1416,0],[17,-14,40.9823,20],[1,4,-12.5664,1]],dtype='float')
b = np.array([[1],[1],[1],[1]], dtype ='float')

gausPartialPivot(A,b,4)