import sympy as sm 
import numpy as np 
import math
import matplotlib.pyplot as plt

x = sm.symbols('x')

def fixedPoint(f, xi, tol, g, maxIter):
    if(f.subs(x,xi) == 0):
        print(str(xi) + " es una raíz")

    else:
        ite = 0
        error = tol + 1

        while(error >= tol and ite < maxIter):
            xn = g.subs(x,xi)

            error = abs(xn - xi)

            ite += 1

            xi = xn

        if error < tol:
            print(str(round(xi,4)) + " es raiz con tolerancia " + str(tol) + " en " + str(ite) + " iteraciones")
        else:
            print("No se halló raíz")

f =  sm.exp(-x) - x         # Función original
g =  sm.exp(-x)             # Función punto fijo
xi = 0.5                    # Punto inicial de búsqueda
tol = 0.005                 # Máximo error absoluto permitido
niter = 100                 # Número máximo de iteraciones en el algoritmo 

fixedPoint(f, xi,tol ,g, niter)