import sympy as sm 
import numpy as np 
import math
import matplotlib.pyplot as plt

x = sm.symbols('x')

def incrementalSearch(f,xi,delta,niter):
    if(f.subs(x,xi)==0):
        print(str(xi) + " es una raíz")
        
    else:
        xf = xi + delta
        ite = 0
        while((f.subs(x,xi)*f.subs(x,xf))>0 and ite < niter):
            xi = xf 
            xf = xf + delta
            ite += 1
            
        if((f.subs(x,xi)*f.subs(x,xf))==0):
            print(str(xf) + " es una raíz")
        
        elif((f.subs(x,xi)*f.subs(x,xf))<0):
            print("Entre " + str(xi) + " y " + str(xf) + " hay una raíz")
        
        else:
            print("No se encontró raíz")


f = sm.exp(3*x-12) + x*sm.cos(3*x)-x**2+4    # Función
xi = -10                                     # Punto inicial
delta = 1                                    # Cambio en cada intervalo
niter = 10                                   # Número máximo de iteraciones

incrementalSearch(f,xi,delta,niter)