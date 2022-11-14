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
        print("The matrix is not square")
        return 
    else:
        Ab = np.append(A,b, axis = 1)
        Ab=np.array(Ab,dtype='float')
        n,m=Ab.shape

        M=np.ones((n,m))
        for k in range(n-1):
            mayor=0
            majorRow=k
            majorColumn=k

        for f in range(k,n):
            for c in range(k,n):
                if(mayor<abs(Ab[f][c])):
                    mayor=abs(Ab[f][c])
                    majorRow=f
                    majorColumn=c

        if(mayor==0):
            print("The system has infinite solutions")
            return 
        else:

            if(majorRow!=k):
                for j in range(n+1):
                    aux=Ab[k,j]
                    Ab[k,j]=Ab[majorRow,j]
                    Ab[majorRow,j]=aux

            if(majorColumn!=k):
                for i in range(n):
                    aux=Ab[i,k]
                    Ab[i,k]=Ab[i,majorColumn]     
                    Ab[i,majorColumn]=aux

                aux1=x[k]
                x[k]=x[majorColumn]
                x[majorColumn]=aux1
            
        for i in range(k+1,n):   
            M[i,k]=Ab[i][k]/Ab[k][k]
            for j in range(k,n+1):
                Ab[i][j]=Ab[i][j]-M[i][k]*Ab[k][j]
          
    return np.round(Ab,decimals=3),x


A = np.array([[-7,2,-3,4],[5,-1,14,-1],[1,9,-7,13],[-12,13,-8,-4]])
b = np.array([[-12],[13],[31],[-32]])

Ab,x=pivoteototal(A,b)
Ab,x