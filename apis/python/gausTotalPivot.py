import sympy as sm 
import numpy as np 
import math
import matplotlib.pyplot as plt

x = sm.symbols('x')

def gausTotalPivot(A,b):
    n1,m1= A.shape
    x=[]

    for i in range(n1):
        name='x'+str(i)
        x.append(name)
    x.append('b')
    if (n1!=m1):
        print("La matriz no es cuadrada")
        return 
    else:
        Ab = np.append(A,b, axis = 1)
        Ab=np.array(Ab,dtype='float')
        n,m=Ab.shape
        #matriz multiplicador
        M=np.ones((n,m))
        for k in range(n-1):
            mayor=0
            filaMayor=k
            columnaMayor=k

      #recorremos elementos de la matriz desde
      # k hasta n
        for f in range(k,n):
            for c in range(k,n):
                if(mayor<abs(Ab[f][c])):
                    mayor=abs(Ab[f][c])
                    filaMayor=f
                    columnaMayor=c

        if(mayor==0):
            print("El sistema tiene infinitas soluciones")
            return 
        else:

            if(filaMayor!=k):
                for j in range(n+1):
                    aux=Ab[k,j]
                    Ab[k,j]=Ab[filaMayor,j]
                    Ab[filaMayor,j]=aux

            if(columnaMayor!=k):
                for i in range(n):
                    #cambiamos la columna en Ab
                    aux=Ab[i,k]
                    Ab[i,k]=Ab[i,columnaMayor]     
                    Ab[i,columnaMayor]=aux

                # cambiamos la pos de x
                aux1=x[k]
                x[k]=x[columnaMayor]
                x[columnaMayor]=aux1
            
        for i in range(k+1,n):   
            M[i,k]=Ab[i][k]/Ab[k][k]
            for j in range(k,n+1):
                Ab[i][j]=Ab[i][j]-M[i][k]*Ab[k][j]
          
    return np.round(Ab,decimals=3),x


A = np.array([[-7,2,-3,4],[5,-1,14,-1],[1,9,-7,13],[-12,13,-8,-4]])
b = np.array([[-12],[13],[31],[-32]])

Ab,x=pivoteototal(A,b)
Ab,x