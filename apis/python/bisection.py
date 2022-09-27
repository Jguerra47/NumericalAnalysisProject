import sympy as sm 
import numpy as np 
import math
import matplotlib.pyplot as plt

x = sm.symbols('x')

def bisection(xi, xf, f, tol):
    if(f.subs(x,xi)*f.subs(x,xf)==0):
        print("x0 o xf es raíz")
    
    elif(f.subs(x,xi)*f.subs(x,xf)>0):
        print("Intervalo no válido")
    else:
        xmedio = (xi+xf)/2
        error = math.fabs(xmedio - xi)
        
        while(error > tol and f.subs(x,xmedio) != 0):
            if(f.subs(x,xi)*f.subs(x,xmedio)<0):
                xf = xmedio
                xi = xi
            else:
                xi = xmedio
                xf = xf
            
            xmedio = (xi+xf)/2
            error = math.fabs(xmedio - xi)
        
        if(f.subs(x,xmedio)==0):
            print("xmedio es raíz")
            
        else:
            print(str(round(xmedio,2)) + " es una raíz con tolerancia " + str(tolerancia))

# En este método se requiere un intervalo que contenga por lo menos una raíz 

f = sm.exp(3*x-12) + x*sm.cos(3*x)-x**2+4   # Función a la que se le encontrará la raíz
xi = 2                                      # Lado izquierdo del intervalo 
xf = 3                                      # Lado derecho del intervalo 
tolerancia = 0.5*10**-3                     # Máximo error absoluto permitido

bisection(xi,xf,f,tolerancia)