import sympy as sm 
import numpy as np 
import math
import matplotlib.pyplot as plt

x = sm.symbols('x')

def CompoundTrapeze(a,b,f,n):
    deltaX = (b-a)/n
    A = 0
    for i in range(n):
        xi =  a + i * deltaX
        fxi = float(f.subs(x,xi))
        if i > 0 and i < n:
            fxi = 2*fxi
        A = A + fxi
    A = A * (deltaX/2)
    return A

f = sm.ln(sm.sin(x) ** 2+1)-(1/2)
a = 1
b = 10
n = 20
print(CompoundTrapeze(a,b,f,b))