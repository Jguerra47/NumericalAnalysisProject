import sympy as sm

x = sm.symbols('x')

def fixedPoint(f, xi, tol, g, maxIter):
    if(f.subs(x,xi) == 0):
        return(str(xi) + " is a root")

    else:
        ite = 0
        error = tol + 1

        while(error >= tol and ite < maxIter):
            xn = g.subs(x,xi)

            error = abs(xn - xi)

            ite += 1

            xi = xn

        if error < tol:
            return(str(round(xi,4)) + " is root with tolerance " + str(tol) + " in " + str(ite) + " iteration")
        else:
            return("No root was found")

# f =  sm.exp(-x) - x
# g =  sm.exp(-x)
# xi = 0.5
# tol = 0.005
# niter = 100

# print(fixedPoint(f, xi,tol ,g, niter))