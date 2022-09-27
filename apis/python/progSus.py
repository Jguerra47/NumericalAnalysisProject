import sympy as sm 
import numpy as np 
import math
import matplotlib.pyplot as plt

x = sm.symbols('x')

def progSus(L,b,n):
    if(L[0][0]==0):
        return
    else:
        z=np.zeros(n)
        suma3=0
        z[0] = b[0]/L[0][0]
        for k in range(1,n):
            if(L[k][k]==0):
                print("Elemento",k, " en la diagonal de L, es cero")
            return
        else:
            for r in range(k):
                suma3=suma3+(L[k][r]*z[r])
                z[k]=(b[k]-suma3)/L[k][k]
                suma3=0
    return z