import sympy as sm 
import numpy as np 
import math
import matplotlib.pyplot as plt

x = sm.symbols('x')

def bisection(xi, xf, f, tol):
    if(f.subs(x,xi)*f.subs(x,xf)==0):
        print("x0 or xf is a root")
    
    elif(f.subs(x,xi)*f.subs(x,xf)>0):
        print("Invalid interval")
    else:
        mid = (xi+xf)/2
        error = math.fabs(mid - xi)
        
        while(error > tol and f.subs(x,mid) != 0):
            if(f.subs(x,xi)*f.subs(x,mid)<0):
                xf = mid
                xi = xi
            else:
                xi = mid
                xf = xf
            
            mid = (xi+xf)/2
            error = math.fabs(mid - xi)
        
        if(f.subs(x,mid)==0):
            print("mid is a root")
            
        else:
            print(str(round(mid,2)) + " is a root with tolerance " + str(tol))

f = sm.exp(3*x-12) + x*sm.cos(3*x)-x**2+4
xi = 2                                       
xf = 3                                       
tol = 0.5*10**-3                    

bisection(xi,xf,f,tol)