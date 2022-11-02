import sympy as sm 
import numpy as np 
import math
from Sustitution.sustitutions import *

x = sm.symbols('x')

def LUGauss(A,b):
    n,m = A.shape
    L=np.zeros((n,n))
    U=np.zeros((n,n))
    U[0]=A[0]
    for k in range(n-1):
        L[k,k]=1
        for i in range(k+1,n):
            m=A[i,k]/A[k,k]
            L[i,k]=m
            for j in range(k,n):
                A[i,j]=A[i,j]-m*A[k,j]
                U[i,j]=A[i,j]
        print("Stage ", k+1)
        print("L: ",L)
        print("U: ", U)
    L[n-1,n-1]=1
    z=sustProg(L,b,n)
    x=sustRegr(U,z,n)
    return L,U,x

def LUGaus(A,b):
    L,U,x = LUGauss(A,b)
    ans = []
    for i in range(x.size):
        ans.append("x"+str(i)+" = "+str(x[i])+"   ")
    return ans

A = np.array([[4,-1,0,3],[1,15.5,3,8],[0,-1.3,-4,1.1],[14,5,-2,30]],dtype='float')
b = np.array([[1],[1],[1],[1]], dtype ='float')
print(LUGaus(A,b))