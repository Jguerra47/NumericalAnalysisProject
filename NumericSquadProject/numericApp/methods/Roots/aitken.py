import sympy as sm 

x = sm.symbols('x')

def aitken(f,x0,tol,n):
    f = sm.sympify(f)
    fxi = float(f.subs(x,x0))
    if fxi == 0:
        return "A root was found",[]
    else:
        matrix = []
        matrix.append([1,x0,fxi,1])
        x1 = float(f.subs(x,x0))
        error = abs(x1-x0)
        fxi = float(f.subs(x,x1))
        matrix.append([2,x1,fxi,error])
        x2 = float(f.subs(x,x1))
        error = abs(x2-x1)
        fxi - float(f.subs(x,x2))
        matrix.append([3,x2,fxi,error])
        det = (x2-x1)-(x1-x0)
        counter = 4
        xi = 0
        while(fxi != 0 and error > tol and counter < n and det!=0):
            xi = x2 - ( (x2 - x1)**2 )/det
            fxi = float(f.subs(x,xi))
            det = (x2-x1)-(x1-x0)
            error = abs(xi-x2)
            matrix.append([counter,xi,fxi,error])
            x0 = xi
            x1 = float(f.subs(x,x0))
            x2 = float(f.subs(x,x1))
            counter += 1
        if fxi == 0:
            ans = 'The root has been found and it is: ', xi
        elif error <= tol:
            ans = 'An approximation has been found and is: ', xi
        elif det == 0:
            ans = 'Error during method execution'
        else:
            ans = 'The method fails with the maximum number of iterations given'
        return ans,matrix

# f = sm.ln(sm.sin(x) ** 2+1)-(1/2)
# x0 = 1
# tol = 1e-7
# niter = 20

# ans,matrix = aitken(f,x0,tol,niter)
# print(ans)
# print(matrix)
# print(ans)
# print()
# if len(matrix)>1:
#   print(f"%11s | %15s | %15s | %15s"%(matrix[0][0],matrix[0][1],matrix[0][2],matrix[0][3]))
#   i = 1
#   while (i < len(matrix)):
#     print(f"%11s | %15E | %15E | %15E"%(matrix[i][0],matrix[i][1],matrix[i][2],matrix[i][3]))
#     i +=1