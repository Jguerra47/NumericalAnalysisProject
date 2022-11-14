import sympy as sm 
import numpy as np 
import math
import matplotlib.pyplot as plt

x = sm.symbols('x')

def secant(f, x0, x1, tol, nIter):
    
    fx0 = f.subs(x,x0)
    fx1 = f.subs(x, x1)
    
    if(fx0 == 0):
        print(str(x0) + " is root")
    
    else:
        cont = 0
        error = tol+1
        den = fx1-fx0
        print(f'%5s | %20E | %20E'%(cont,x0,error))
        while(error >= tol and fx1 != 0 and den != 0 and cont < nIter):
            x2 = x1-(fx1*(x1-x0))/den

            error = abs(x2-x1)
            
            x0 = x1
            x1 = x2
            print(f'%5s | %20E | %20E'%(cont,x0,error))
            fx0 = fx1 
            fx1 = f.subs(x,x1)
            
            den = fx1-fx0
            cont = cont + 1
        
        if(fx1 == 0):
            print(str(x1) +  " is a root")
                
        elif(error < tol):
            print(str(x1) +  " is an approximation to a root with a tolerance of " + str(tol))
                
        elif(den == 0):
            print("There is a possible multiple root")
            
        else:
            print("Failed in " + str(nIter) +  " iterations")



f = sm.sympify("x**3")
tol = 0.005
x0 = -2
x1 = 1
nIter = 120
secant(f,x0,x1,tol,nIter)