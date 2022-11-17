import sympy as sm

x = sm.symbols('x')

def incrementalSearch(f,xi,delta,niter):
    if(f.subs(x,xi)==0):
        return (str(xi) + " is a root")
        
    else:
        xf = xi + delta
        ite = 0
        while((float(f.subs(x,xi))*float(f.subs(x,xf)))>0 and ite < niter):
            xi = xf 
            xf = xf + delta
            ite += 1
            
        if((f.subs(x,xi)*f.subs(x,xf))==0):
            return (str(xf) + " is a root")
        
        elif((f.subs(x,xi)*f.subs(x,xf))<0):
            return ("Between " + str(xi) + " and " + str(xf) + " there is a root")
        
        else:
            return ("No root found")


# f = sm.exp(3*x-12) + x*sm.cos(3*x)-x**2+4
# xi = -10
# delta = 1
# niter = 10

# print(incrementalSearch(f,xi,delta,niter))