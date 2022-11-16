from math import *
import numpy as np
import scipy

def matrix(x,y):
    A = []
    B = []
    n = len(x)
    m = 4*(n-1)
    A = np.zeros([m,m])
    print(A)
    B = np.zeros([m,1])
    Coef = np.zeros([n-1,4])
    z = 0
    for i in range(1,n):
        A[i][z] = (x[i])**3
        A[i][z+1] = (x[i])**2
        A[i][z+2] = x[i]
        A[i][z+3] = 1
        z = z+4
        B[i][0]=y[i]

    A[0][0] = x[0]**3
    A[0][1] = x[0]**2
    A[0][2] = x[0]**1
    A[0][3] = 1
    B[0][0] = y[0]
    z=0
    for i in range(2,len(x)):
        A[len(x)-2+i][z] = x[i-1]**3
        A[len(x)-2+i][z+1] = x[i-1]**2
        A[len(x)-2+i][z+2] = x[i-1]
        A[len(x)-2+i][z+3] = 1
        A[len(x)-2+i][z+4] = -(x[i-1]**3)
        A[len(x)-2+i][z+5] = -(x[i-1]**2)
        A[len(x)-2+i][z+6] = -x[i-1]
        A[len(x)-2+i][z+7] = -1
        z=z+4 
        B[n-1+i][0]=0
    z=0
    for i in range(2, len(x)):
        A[2*len(x)-4+i][z] = (x[i-1]**2)*3
        A[2*len(x)-4+i][z+1] = x[i-1]*2
        A[2*len(x)-4+i][z+2] = 1
        A[2*len(x)-4+i][z+3] = 0
        A[2*len(x)-4+i][z+4] = -(x[i-1]**2)*3
        A[2*len(x)-4+i][z+5] = -(x[i-1]*2)
        A[2*len(x)-4+i][z+6] = -1
        A[2*len(x)-4+i][z+7] = 0
        z=z+4
        B[2*len(x)-3+i][0]=0
    z=0
    for i in range(2, len(x)):
        A[3*len(x)-6+i][z] = (x[i-1]*6)
        A[3*len(x)-6+i][z+1] = 2
        A[3*len(x)-6+i][z+2] = 0
        A[3*len(x)-6+i][z+3] = 0
        A[3*len(x)-6+i][z+4] = -(x[i-1]*6)
        A[3*len(x)-6+i][z+5] = -2
        A[3*len(x)-6+i][z+6] = 0
        A[3*len(x)-6+i][z+7] = 0
        z=z+4
        B[len(x)+4+i][0]=0
    A[m-2][0]=x[0]*6
    A[m-2][1]=2
    B[m-1][0]=0
    A[m-1][8]=x[len(x)-1]*6
    A[m-1][9]=2
    B[m-2][0]=0
    inverse= np.linalg.inv(A)
    result = np.dot(inverse,B)
    newarray = np.zeros((3,4))
    print(A)
    toit=0
    for i in range(1, len(newarray)+1):
        print("as")
        newarray[i-1][0] = result[toit]
        newarray[i-1][1] = result[toit+1]
        newarray[i-1][2] = result[toit+2]
        newarray[i-1][3] = result[toit+3]
        toit = toit+4
    return newarray

x = [1,2,3,4]
y = [5,6,7,8]

print(matrix(x,y))