import sympy as sm 
import math

x = sm.symbols('x')

def bisection(xi, xf, f, tol):
    if(f.subs(x,xi)*f.subs(x,xf)==0):
        return("x0 or xf is a root")
    
    elif(f.subs(x,xi)*f.subs(x,xf)>0):
        return("Invalid interval")
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
            return("mid is a root")
            
        else:
            return(str(round(mid,2)) + " is a root with tolerance " + str(tol))

# f = sm.exp(3*x-12) + x*sm.cos(3*x)-x**2+4
# xi = 2                                       
# xf = 3                                       
# tol = 0.5*10**-3                    

# print(bisection(xi,xf,f,tol))