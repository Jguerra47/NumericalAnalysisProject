import math
import numpy as np
from sympy import substitution          
a = [
        [-7,2,-3,4,-12],
        [5,-1,14,-1,13],
        [1,9,-7,13,31],
        [-12,13,-8,-4,-32]
        ]

n = len(a)
tags = [i for i in range(0,n)]


def changeRow(maxRow,k):
    for i in range(0,len(a)+1):
        aux = a[k][i]
        a[k][i] = a[maxRow][i]
        a[maxRow][i]= aux
    
def changeColumn(maxCol,k):
    aux = tags[k]
    tags[k] = tags[maxCol]
    tags[maxCol] = aux
    for j in range(0,len(a)):
        aux = a[j][k]
        a[j][k] = a[j][maxCol]
        a[j][maxCol] = aux
        



def totalPivoting(k):
    maxi = 0
    maxRow = k
    maxCol = k
    for r in range(k,n):
        for s in range (k,n):
            if (math.fabs(a[r][s]) > maxi):
                maxi = math.fabs(a[r][s])
                maxRow = r
                maxCol = s
        
    if(maxi == 0):
        print("division 0")
        return
    else:
        if(maxRow != k):
            changeRow(maxRow,k)
        if(maxCol != k):
            changeColumn(maxCol,k)
            
def elimination():
    for k  in range(0,n-1):
        totalPivoting(k)
        for i  in range (k + 1, n):    
            multiplier = a[i][k]/a[k][k]
            for j in range (k,n + 1):
                a[i][j] = a[i][j]-(multiplier*a[k][j])
        

    return substitution()


def sorting(x):
    return [i for _,i in sorted(zip(tags,x))]
        


def substitution():
    n = len(a) -1
    x = [i for i in range(n+1)]
    x[len(x)-1] = a[n][n+1]/a[n][n]
    
    
    for i in range(0,n+1):
        sumi = 0
        auxi = n - i 
        sumi = 0
        for p in range(auxi+1,n+1):
            sumi = sumi + a[auxi][p]*x[p]
        x[auxi]=(a[auxi][n+1]-sumi)/a[auxi][auxi]

    tags.reverse()
    x.reverse()
    x = sorting(x)
    for i in range(0,len(x)):
        if(math.fabs(x[i]) < 10**-15):
            x[i] = 0    
    return x
            


