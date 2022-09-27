import sympy as sm 
import numpy as np 
import math
import matplotlib.pyplot as plt

x = sm.symbols('x')

def elimination(Ab,n):    
                                                                
    for k in range(n):
        
        for i in range(k+1,n):
            
            if(Ab[k][k] == 0):
                print("División por 0, no es posible realizar eliminación Gaussiana")
                return Ab
                break
                
            multiplicador = Ab[i][k]/Ab[k][k]
            
            for j in range(k, n+1):
                Ab[i,j] = Ab[i,j] - multiplicador*Ab[k,j]
        print()
        print("=============================")
        print(Ab)
    
    return Ab 

def gausSimple(A,b,n):
    Ab = np.append(A,b, axis = 1)
    Ab = elimination(Ab,n)


    A = Ab[:,0:n-1]
    b = Ab[:,n-1]

    x = regSus(Ab,n)

    for i in range(1,n+1,1):
        print("x" + str(i) + " = " + str(x[i-1]))

A = np.array([[10,20,-60.8319,8],[1,1,-2.1416,0],[17,-14,40.9823,20],[1,4,-12.5664,1]],dtype='float')
b = np.array([[1],[1],[1],[1]], dtype ='float')

gausSimple(A,b,4)