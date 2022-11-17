import sympy as sm

x = sm.symbols('x')

def falseRule(f, xi, xf, tol, niter):
    
    error = 1000
    if(float(f.subs(x,xi))*float(f.subs(x,xf)) == 0):
        if(float(f.subs(x,xi)) == 0):
            return(str(round(xi,8)) + " is a root"),[]
        else:
            return(str(round(xf,8)) + " is a root"),[]
    
    elif(float(f.subs(x,xi))*float(f.subs(x,xf)) > 0):
        return("Invalid interval"),[]
    
    else:
        fxi = float(f.subs(x,xi))
        fxf = float(f.subs(x,xf))
        pm = (fxf*xi-fxi*xf)/(fxf-fxi)
        fpm = float(f.subs(x,pm))
        matrix = []
        matrix.append([1,xi,pm,xf,fpm,error])
        # print(matrix[-1])
        iter = 2
        while(error >= tol and float(f.subs(x,pm)) != 0 and iter <= niter):
            if(fxi*fpm < 0):
                xf = pm
            else:
                xi = pm

            p0 = pm
            pm = (float(f.subs(x,xf))*xi-float(f.subs(x,xi))*xf)/(float(f.subs(x,xf))-float(f.subs(x,xi)))

            fpm = float(f.subs(x,pm))
            error = abs(pm - p0)

            matrix.append([iter,xi,pm,xf,fpm,error])
            # print(matrix[-1])
            iter = iter +1

        if(float(f.subs(x,pm)) == 0):
            return(str(round(pm,8)) + " is root and was found in the iteration " + str(iter)),matrix
        else: 
            return(str(round(pm,8)) + " is root with tolerance " + str(tol) + " and was found in the iteration " + str(iter)),matrix

# f = sm.sympify("log(sin(x)^2 + 1)-(1/2)")
# xi = 0     
# xf = 1
# tol = 1e-7
# niter = 100
# print(falseRule(f,xi,xf,tol, niter))