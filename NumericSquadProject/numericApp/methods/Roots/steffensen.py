def steffensen(f,p0,tol,niter):
    count = 0
    error = tol + 1
    matrix = [["iterations","p","error"]]
    matrix.append([count,p0,error])
    while (count < niter and error > tol):
        p1 = float(f.subs(x,p0))
        p2 = float(f.subs(x,p1))
        p = p0-(p1-p0)**2/(p2-2*p1+p0)
        error = abs(p-p0)
        p0 = p; 
        count = count+1
        matrix.append([count,p0,error])
    if(f.subs(x,p0) == 0):
        ans = str(p0)+" is a root"
    elif error < tol:
        ans = str(p0)+" is an approximation with tolerance "+str(tol)
    else:
        ans = 'failed to converge in 1000 iterati ons.'
    return ans,matrix

f = sm.ln(sm.sin(x) ** 2+1)-(1/2)    # Función
p0 = -10                                     # Punto inicial
tol = 1                                    # Cambio en cada intervalo
niter = 10                                   # Número máximo de iteraciones

ans,matrix = steffensen(f,p0,tol,niter)
print(ans)
print()
if len(matrix)>1:
    print(f"%11s | %15s | %15s"%(matrix[0][0],matrix[0][1],matrix[0][2]))
    i = 1
    while (i < len(matrix)):
        print(f"%11s | %15E | %15E"%(matrix[i][0],matrix[i][1],matrix[i][2]))
        i +=1