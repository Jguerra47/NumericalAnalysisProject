import sympy as sm 
import math

x = sm.symbols('x')

def bisection(xi, xf, f, tol):
    if(float(f.subs(x,xi))*float(f.subs(x,xf))==0):
        return "xi or xf is a root",[]
    
    elif(float(f.subs(x,xi))*float(f.subs(x,xf))>0):
        return "Invalid interval",[]
    else:
        mid = (xi+xf)/2
        error = math.fabs(mid - xi)
        matrix = []
        count = 1
        while(error > tol and float(f.subs(x,mid)) != 0):
            mid = (xi+xf)/2
            error = math.fabs(mid - xi)
            xMid = float(f.subs(x,mid))
            matrix.append([count,xi,mid,xf,xMid,error])
            count +=  1
            # print(matrix[-1]) 
            if(float(f.subs(x,xi))*float(f.subs(x,mid))<0):
                xf = mid
                xi = xi
            else:
                xi = mid
                xf = xf
            
        
        if(f.subs(x,mid)==0):
            return(str(round(mid,8)) + " is a root"),matrix
            
        else:
            return(str(round(mid,8)) + " is a root with tolerance " + str(tol)),matrix

# f = sm.exp(3*x-12) + x*sm.cos(3*x)-x**2+4
f = sm.sympify("log(sin(x)^2 + 1)-(1/2)")
xi = 0
xf = 1    
tol = 1e-7

print(bisection(xi,xf,f,tol))