import sympy as sm

x = sm.symbols('x')

def mulRT(f, xi, tol, nIter):
    f = sm.sympify(f)
    dx = sm.diff(f,x)
    dx2 = sm.diff(dx,x)

    if(float(f.subs(x,xi)) == 0):
        return (str(xi) + " is a root"),[]
    
    else:
        iter = 0 
        error = tol +1
        matrix = []
        fxn = float(f.subs(x,xi))
        matrix.append([iter,xi,fxn,error])
        # print(matrix[-1])
        while(error >= tol and iter < nIter):
            xn = xi - (float(f.subs(x,xi))*float(dx.subs(x,xi)))/(((float(dx.subs(x,xi)))**2) - float(f.subs(x,xi))*float(dx2.subs(x,xi)))
            error = abs(xn-xi)
            iter = iter + 1
            xi = xn
            fxn = float(f.subs(x,xn))
            matrix.append([iter,xi,fxn,error])
            # print(matrix[-1])

        if(error < tol):
            return (str(xi) + " is root with tolerance " + str(tol)),matrix
        
        else:
            return ("No root found"),matrix


f = sm.sympify("exp(x) - x - 1")
xi = 1
tol = 1e-7
nIter = 100

print(mulRT(f,xi,tol,nIter))