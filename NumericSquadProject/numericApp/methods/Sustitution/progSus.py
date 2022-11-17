import sympy as sm 
import numpy as np 
import math

x = sm.symbols('x')

def progSus(L,b,n):
    if(L[0][0]==0):
        return
    else:
        z=np.zeros(n)
        sum3=0
        z[0] = b[0]/L[0][0]
        for k in range(1,n):
            if(L[k][k]==0):
                print("Element ",k, " on the diagonal of L, is zero")
            return
        else:
            for r in range(k):
                sum3=sum3+(L[k][r]*z[r])
                z[k]=(b[k]-sum3)/L[k][k]
                sum3=0
    return z