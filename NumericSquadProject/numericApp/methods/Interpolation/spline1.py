
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


def spline1Ans(xi,fi):
    n = len(xi)
    polynom = spline1(xi,fi)

    segments = []
    polBySeg = []
    for sec in range(1,n,1):
        segments.append(' x = ['+str(xi[sec-1])
            +','+str(xi[sec])+']')
        polBySeg.append(str(polynom[sec-1]))

    #Find the polynom (polBySeg_i) that applies to the segment (segments_i)    
    return segments,polBySeg

xi = [-1 , 0, 3, 4]
fi = [15.5, 3, 8, 1]
print(spline1Ans(xi,fi))