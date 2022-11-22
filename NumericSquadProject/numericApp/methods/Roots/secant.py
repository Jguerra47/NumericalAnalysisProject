import sympy as sm 

x = sm.symbols('x')

def secant(f, x0, x1, tol, nIter):
    f = sm.sympify(f)
    fx0 = float(f.subs(x,x0))
    fx1 = float(f.subs(x, x1))
    matrix = []
    if(fx0 == 0):
        return(f"%E is root"%(x0)),[]
    
    else:
        cont = 1
        error = tol+1
        den = fx1-fx0
        # print(f'%5s | %20E | %20E'%(-1,x0,error))
        matrix.append([0,x0,error])
        while(error >= tol and fx1 != 0 and den != 0 and cont < nIter):
            
            x2 = x1-(fx1*(x1-x0))/den

            error = abs(x2-x1)
            
            x0 = x1
            x1 = x2
            # print(f'%5s | %20E | %20E'%(cont,x0,error))
            matrix.append([cont,x0,error])
            #print(matrix[-1])
            fx0 = float(fx1)
            fx1 = float(f.subs(x,x1))
            
            den = fx1-fx0
            cont = cont + 1
        
        if(fx1 == 0):
            ans = (f"%E is a root"%(x1))
                
        elif(error < tol):
            ans = (f"%E is an approximation to a root with a tolerance of %E" %(x1,tol))
                
        elif(den == 0):
            ans = ("There is a possible multiple root")
            
        else:
            ans = ("Failed in " + str(nIter) +  " iterations")
        return ans,matrix



# f = sm.sympify("log(sin(x)^2 + 1)-(1/2)")
# tol = 1e-7
# x0 = 0.5
# x1 = 1
# nIter = 100
# print(secant(f,x0,x1,tol,nIter))