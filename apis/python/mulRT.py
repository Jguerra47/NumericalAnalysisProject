import sympy as sm 
import numpy as np 
import math
import matplotlib.pyplot as plt

x = sm.symbols('x')

def mulRT(f, xi, tol, nIter):
    dx = sm.diff(f,x)
    dx2 = sm.diff(dx,x)

    if(f.subs(f,x) == 0):
        print(str(xi) + " es una raíz")
    
    else:
        iter = 0 
        error = tol +1
        while(error >= tol and iter < nIter):
            xn = xi - (f.subs(x,xi)*dx.subs(x,xi))/(((dx.subs(x,xi))**2) - f.subs(x,xi)*dx2.subs(x,xi))
            error = abs(xn-xi)
            iter = iter + 1
            xi = xn 

        if(error < tol):
            print(str(xi) + " es raíz con tolerancia " + str(tol) + " en la iteración " + str(iter))
        
        else:
            print("No se halló raíz")


f = x**3 - x**2 - 2*x + 2 + sm.sin(x-1)
xi = 0.5
tol = 0.005
nIter = 1000

mulRT(f,xi,tol,nIter)