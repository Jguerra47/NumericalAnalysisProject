import sympy as sm 
import numpy as np 
import math
import matplotlib.pyplot as plt

x = sm.symbols('x')

def fixedPoint(f, xi, tol, g, maxIter):
    if(f.subs(x,xi) == 0):
        print(str(xi) + " is a root")

    else:
        ite = 0
        error = tol + 1

        while(error >= tol and ite < maxIter):
            xn = g.subs(x,xi)

            error = abs(xn - xi)

            ite += 1

            xi = xn

        if error < tol:
            print(str(round(xi,4)) + " is root with tolerance " + str(tol) + " in " + str(ite) + " iteration")
        else:
            print("No root was found")

f =  sm.exp(-x) - x
g =  sm.exp(-x)
xi = 0.5
tol = 0.005
niter = 100

fixedPoint(f, xi,tol ,g, niter)