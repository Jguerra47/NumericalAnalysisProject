import sympy as sm
import numpy as np


x = sm.symbols('x')

def fixedPoint(f, xi, tol, g, maxIter):
    f = sm.sympify(f)
    g = sm.sympify(g)
    if(type(f.subs(x, xi)) is sm.core.numbers.ComplexInfinity):
        return "complex numbers not supported",[]
    if(float(f.subs(x,xi)) == 0):
        return(str(xi) + " is a root"),[]

    else:
        ite = 0
        error = tol + 1
        matrix = []
        while(error >= tol and ite <= maxIter):
            xn = float(g.subs(x,xi))
            fxi = float(f.subs(x,xi))
            error = abs(xn - xi)
            matrix.append([ite,xi,xn,fxi,error])
            # print(matrix[-1])
            ite += 1
            xi = xn

        if error < tol:
            message = str(round(xi,8)) + " is root with tolerance " + str(tol)
            return message,matrix
        else:
            message = "No root was found"
            return message,matrix

# f =  sm.sympify("log(sin(x)^2 + 1)-(1/2)-x")
# g =  sm.sympify("log(sin(x)^2 + 1)-(1/2)")
# xi = -0.5
# tol = 1e-7
# niter = 100

# fixedPoint(f, xi,tol ,g, niter)