from sympy import *
from sympy.parsing.sympy_parser import parse_expr
import math

def lagrange(valor,x,y):

    pol = ""
    G = Function('G')
    F = Function('F')
    n = len(x) #quantity of points
    result = 0
    for k in range(n):
        productoria = 1
        termino = "("
        for i in range(n):
            if i != k:
                productoria *=  (valor - x[i])/(x[k] - x[i])
                termino += "(x-"+str(x[i])+")"
        termino += ")/("
        for i in range(n):
            if i != k:
                termino += "(" + str(x[k]) + "-" + str(x[i]) + ")"
        termino += ")"
        termino = termino.replace(")(",") * (")
        F = parse_expr(termino)
        print("\n L" + str(k) + "(x) = " + termino.replace("((","(").replace("))",")") + " = " + str(expand(F)))
        toReplace = "L" + str(k) + "(x) = "
        pol += "(" + str(expand(F)) + ")*" + str(y[k])
        if k != n-1:
            pol += " + "
        result += productoria*y[k]
    G = str(expand(pol))
    print ("\nLagrange´s polynom")
    ans = [f"{y[i]}*L{i} +" for i in range(len(y))] 
    ans[-1] = ans[-1][:-1]
    print(" ".join(ans))

lagrange(4,[-1,0,3,4],[15.5,3,8,1])