import sympy as sm

x = sm.symbols('x')

def newton(f,x0 ,tol ,nIter): 
    dx = sm.diff(f,x)
    y0 = float(f.subs(x,x0))
    d0 = float(dx.subs(x,x0))
    cont = 0 
    error = tol+1
    matrix = []
    matrix.append([cont,x0,y0,error])
    # print(matrix[-1])
    while(y0 != 0 and d0 != 0 and error > tol and cont < nIter):
        x1 = x0 -(y0/d0)
        y0 = f.subs(x,x1)
        d0 = dx.subs(x,x1)
        error = abs(x1-x0)
        x0 = x1
        cont = cont + 1
        matrix.append([cont,x0,y0,error])
        # print(matrix[-1])
    
    if(y0 == 0):
        return (str(round(x0,8)) + " is a root "),matrix
    
    elif(error < tol):
        return (str(round(x0,8)) + " is an approximate root with a tolerance of " + str(tol)),matrix
    
    else:
        return ("Failed in " + str(nIter) + " iterations"),matrix
     

f = sm.sympify("log(sin(x)^2 + 1)-(1/2)")
x0 = -2
tol = 1e-7
nIter = 100

print(newton(f,x0,tol,nIter))