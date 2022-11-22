import sympy as sm 
import numpy as np

x = sm.symbols('x')

def regSus(Ab,n):
    x = np.zeros(n)
    
    n = n-1
    
    k = Ab[n-1][n+1]/Ab[n][n]
    
    
    x[n] =(Ab[n][n+1]/Ab[n][n])
    
    for i in range(n-1,-1,-1):
        sum = 0
        for p in range(i+1,n+1):
            k = x[p]
            sum = sum + (Ab[i][p]*x[p])
          
        x[i] =(Ab[i][n+1]-sum)/Ab[i][i]
        
    return x