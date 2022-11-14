
import numpy as np
import sympy as sp

def spline1(xi,fi):
    n = len(xi)
    x = sp.Symbol('x')
    polynom = []
    sec=1
    while not(sec>=n):
        m =(fi[sec]-fi[sec-1])/(xi[sec]-xi[sec-1])
        beg = fi[sec-1]-m*xi[sec-1]
        psec = beg + m*x
        polynom.append(psec)
        sec = sec + 1
    return(polynom)

xi = [-1 , 0, 3, 4]
fi = [15.5, 3, 8, 1]

n = len(xi)
polynom = spline1(xi,fi)

print('polynoms by segments: ')
for sec in range(1,n,1):
    print(' x = ['+str(xi[sec-1])
          +','+str(xi[sec])+']')
    print(str(polynom[sec-1]))