import sympy as sm 
import numpy as np 
import math
import matplotlib.pyplot as plt

x = sm.symbols('x')

def falseRule(f, xi, xf, tol, niter):
    iter = 0 
    error = 1000
    if(f.subs(x,xi)*f.subs(x,xf) == 0):
        if(f.subs(x,xi) == 0):
            print(str(xi) + " is a root")
        else:
            print(str(xf) + " is a root")
    
    elif(f.subs(x,xi)*f.subs(x,xf) > 0):
        print("Invalid interval")
    
    else:
        fxi = f.subs(x,xi)
        fxf = f.subs(x,xf)
        pm = (fxf*xi-fxi*xf)/(fxf-fxi)
        fpm = f.subs(x,pm)
        
        while(error >= tol and f.subs(x,pm) != 0 and iter <= niter):
            if(fxi*fpm < 0):
                xf = pm
            else:
                xi = pm

            p0 = pm
            pm = (f.subs(x,xf)*xi-f.subs(x,xi)*xf)/(f.subs(x,xf)-f.subs(x,xi))

            fpm = f.subs(x,pm)
            error = abs(pm - p0)
        
            iter = iter +1

        if(f.subs(x,pm) == 0):
            print(str(pm) + " is root and was found in the iteration " + str(iter))
        else: 
            print(str(round(pm,2)) + " is root with tolerance " + str(tol) + " and was found in the iteration " + str(iter))

f = x**3 - 7.51*x**2 + 18.4239*x - 14.8331
xi = 3                                        
xf = 3.5                                      
tol = 5*10**-5                               
niter = 10                                   
falseRule(f,xi,xf,tol, niter)