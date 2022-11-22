import sympy as sm

x = sm.symbols('x')

def trisection(f,left,right,tol,niter):
    f = sm.sympify(f)
    fRight = float(f.subs(x,right))
    fLeft = float(f.subs(x,left))
    matrix = []
    if (fRight == 0):
        answer = str(right)+" is a root"
        return answer,[]
    elif fLeft == 0:
        answer = str(left)+" is a root"
        return answer,[]
    elif(fLeft*fRight<0):
        xmid1=left+(right-left)/3
        xmid2= right-(right-left)/3
        fXmid1=float(f.subs(x,xmid1))
        fXmid2=float(f.subs(x,xmid2))
        counter=1
        error1=tol+1
        error2=tol+1
        while(error1 > tol  and error2 > tol and fXmid1 != 0 and fXmid2 != 0 and counter < niter):
            matrix.append([counter,left,right,xmid1,xmid2,fXmid1,fXmid2,error1,error2])
            if(fLeft*fXmid1<0):
                right = xmid1
                fRight = fXmid1
            elif(fXmid1*fXmid2<0):
                left = xmid1
                fLeft = fXmid1
                right = xmid2
                fRight = fXmid2
            else:
                left = xmid2
                fLeft = fXmid2
            xAux1 = xmid1
            xAux2 = xmid2
            xmid1 = left+(right-left)/3
            xmid2 = right-(right-left)/3
            fXmid1 = float(f.subs(x,xmid1))
            fXmid2 = float(f.subs(x,xmid2))
            error1 = abs(xmid1-xAux1)
            error2 = abs(xmid2-xAux2)
            counter = counter+1
        matrix.append([counter,left,right,xmid1,xmid2,fXmid1,fXmid2,error1,error2])
        if(fXmid1==0):
            answer = str(xmid1)+" is a root"
        elif(fXmid2==0):
            answer = str(xmid2)+" is a root"
        elif(error1<tol):
            answer = str(xmid1)+" is an approximation with tolerance "+str(tol)
        elif(error2<tol):
            answer = str(xmid2)+" is an approximation with tolerance "+str(tol)
        else:
            answer = "The method fails in "+niter+" iterations"
        return answer,matrix
    else:
        return "bad range",[]

# f = sm.ln(sm.sin(x) ** 2+1)-(1/2)    # Función
# x0 = 1                                     # Punto inicial
# x1 = 10
# tol = 1e-7                               # Cambio en cada intervalo
# niter = 20                                 # Número máximo de iteraciones

# ans,matrix = trisection(f,x0,x1,tol,niter)
# print(ans)
# print(matrix)
# print()
# if len(matrix)>1:
#     print(f"%11s | %15s | %15s | %15s | %15s | %15s | %15s | %15s | %15s"%(matrix[0][0],matrix[0][1],matrix[0][2],matrix[0][3],matrix[0][4],matrix[0][5],matrix[0][6],matrix[0][7],matrix[0][8]))
#     i = 1
#     while (i < len(matrix)):
#         print(f"%11s | %15E | %15E | %15E | %15E | %15E | %15E | %15E | %15E"%(matrix[i][0],matrix[i][1],matrix[i][2],matrix[i][3],matrix[i][4],matrix[i][5],matrix[i][6],matrix[i][7],matrix[i][8]))
#         i += 1