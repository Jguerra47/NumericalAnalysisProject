from sympy import *
import sympy as sm 
from sympy.parsing.sympy_parser import parse_expr
import math

def lagrange(x,y):
    valor = len(x)
    n = len(x) #quantity of points
    ansL = []
    for k in range(n):
        productoria = 1
        termino = "("
        for i in range(n):
            if i != k:
                productoria *=  (valor - x[i])/(x[k] - x[i])
                termino += "(x-"+str(x[i])+")"
        termino += ") / ("
        for i in range(n):
            if i != k:
                termino += "(" + str(x[k]) + "-" + str(x[i]) + ")"
        termino += ")"
        termino = termino.replace(")(",") * (")
        ansL.append(termino)
        ansL[-1] = str(sm.sympify(ansL[-1])).replace("**","^")
        
    # print ("\nLagrange´s polynom")
    ans = [f"{y[i]}*L{i} +" for i in range(len(y))] 
    ans[-1] = ans[-1][:-1]
    polynom = (" ".join(ans))
    fullPolynom = polynom
    for i in range(len(y)):
        fullPolynom = fullPolynom.replace(f"L{i}",ansL[i])
    fullPolynom = str(sm.sympify(fullPolynom)).replace("**","^")
    polynom = str(sm.sympify(polynom)).replace("**","^")
    #AnsL is each one of lagrange's polynom and polynom is the use of them with its respective coefficients
    return ansL,polynom,fullPolynom

# print(lagrange([-1,0,3,4],[15.5,3,8,1]))