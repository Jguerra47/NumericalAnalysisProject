from math import *
import numpy as np
import numericApp.methods.Interpolation.totalPivoting as totalPivoting

def spline3Ans(x,y):
    A = []
    B = []
    n = len(x)
    m = 4*(n-1)
    A = np.zeros([m,m])
    B = np.zeros([m,1])
    coef = np.zeros([n-1,4])
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
    for i in range(2,n):
        A[n-2+i][z] = x[i-1]**3
        A[n-2+i][z+1] = x[i-1]**2
        A[n-2+i][z+2] = x[i-1]
        A[n-2+i][z+3] = 1
        A[n-2+i][z+4] = -(x[i-1]**3)
        A[n-2+i][z+5] = -(x[i-1]**2)
        A[n-2+i][z+6] = -x[i-1]
        A[n-2+i][z+7] = -1
        z=z+4 
        B[n-1+i][0]=0
    z=0
    for i in range(2, n):
        A[2*n-4+i][z] = (x[i-1]**2)*3
        A[2*n-4+i][z+1] = x[i-1]*2
        A[2*n-4+i][z+2] = 1
        A[2*n-4+i][z+3] = 0
        A[2*n-4+i][z+4] = -(x[i-1]**2)*3
        A[2*n-4+i][z+5] = -(x[i-1]*2)
        A[2*n-4+i][z+6] = -1
        A[2*n-4+i][z+7] = 0
        z=z+4
        B[2*n-3+i][0]=0
    z=0
    for i in range(2, n):
        A[3*n-6+i][z] = (x[i-1]*6)
        A[3*n-6+i][z+1] = 2
        A[3*n-6+i][z+2] = 0
        A[3*n-6+i][z+3] = 0
        A[3*n-6+i][z+4] = -(x[i-1]*6)
        A[3*n-6+i][z+5] = -2
        A[3*n-6+i][z+6] = 0
        A[3*n-6+i][z+7] = 0
        z=z+4
        B[n+4+i][0]=0
    A[m-2][0]=x[0]*6
    A[m-2][1]=2
    B[m-1][0]=1
    A[m-1][m-4]=x[n-1]*6
    A[m-1][m-3]=2
    B[m-2][0]=1

    #Solution
    A = np.concatenate((A,B),axis=1)
    totalPivoting.a = A.tolist()
    totalPivoting.n = len(A)
    totalPivoting.tags = [i for i in range(0,totalPivoting.n)]
    result = totalPivoting.elimination()


    toit=0
    for i in range(1, len(coef)+1):
        coef[i-1][0] = result[toit]
        coef[i-1][1] = result[toit+1]
        coef[i-1][2] = result[toit+2]
        coef[i-1][3] = result[toit+3]
        toit = toit+4

    segments = []
    polBySeg = []
    for seg in range(1,n,1):
        segments.append(f"{x[seg-1]:g} ≤ x ≤ {x[seg]:g}")
        polBySeg.append(f"{coef[seg-1,0]:4g}x^3 + {coef[seg-1,1]:4g}x^2 + {coef[seg-1,2]:4g}x + {coef[seg-1,3]:4g}")
        
        
    return segments,polBySeg

#x = [1,2,3,4]
#y = [5,6,7,8]
#print(spline3Ans(x,y))