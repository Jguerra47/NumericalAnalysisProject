import sympy as sm 
import numpy as np 
import math
import matplotlib.pyplot as plt

x = sm.symbols('x')

def newton(f,x0 ,tol ,nIter): 
    dx = sm.diff(f,x)
    y0 = f.subs(x,x0)
    d0 = f.subs(x,x0)
    cont = 0 
    error = tol+1

    while(y0 != 0 and d0 != 0 and error > tol and cont < nIter):
        x1 = x0 -(y0/d0)
        y0 = f.subs(x,x1)
        d0 = dx.subs(x,x1)
        error = abs(x1-x0)
        x0 = x1
        cont = cont + 1
    
    if(y0 == 0):
        print(str(x0) + " is a root ")
    
    elif(error < tol):
        print(str(x0) + " is an approximate root with a tolerance of " + str(tol))
    
    else:
        print("Failed in " + str(nIter) + " iterations")
     

f = 2*x
x0 = -2
tol = 5*10**-2
nIter = 10

newton(f,x0,tol,nIter)