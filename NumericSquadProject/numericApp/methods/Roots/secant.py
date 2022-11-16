import sympy as sm 

x = sm.symbols('x')

def secant(f, x0, x1, tol, nIter):
    
    fx0 = f.subs(x,x0)
    fx1 = f.subs(x, x1)
    matrix = []
    if(fx0 == 0):
        print(f"%E is root"%(x0))
    
    else:
        cont = 0
        error = tol+1
        den = fx1-fx0
        # print(f'%5s | %20E | %20E'%(-1,x0,error))
        matrix.append([-1,x0,error])
        while(error >= tol and fx1 != 0 and den != 0 and cont < nIter):
            x2 = x1-(fx1*(x1-x0))/den

            error = abs(x2-x1)
            
            x0 = x1
            x1 = x2
            # print(f'%5s | %20E | %20E'%(cont,x0,error))
            matrix.append([cont,x0,error])
            fx0 = fx1 
            fx1 = f.subs(x,x1)
            
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



# f = sm.sympify("x**3")
# tol = 0.005
# x0 = -2
# x1 = 1
# nIter = 120
# print(secant(f,x0,x1,tol,nIter))