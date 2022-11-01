import numpy as np

def vandermonde(x, y):
    n = len(x)
    A =  np.zeros((n, n))
    
    #Primera columna de unos
    cont = 0
    while(cont < n):
        A[cont][0] = 1
        cont += 1

    #Segunda columna con valores de x
    cont = 0
    while(cont < n):
        A[cont][1] = x[cont]
        cont += 1
    
    #Llenar las n-2 columnas restantes
    cont = 0
    while(cont < n): 
        cont2 = 2
        while(cont2 < n):
            A[cont][cont2] = A[cont][1]**(cont2)
            cont2 += 1
        cont += 1
    
    #Inversa de la matriz resultante
    AI = np.linalg.inv(A)

    #Producto matricial
    R = np.dot(AI, y)
    print(R)
    return R
x = [-1, 0, 3, 4]
y = [15.5, 3, 8, 1]

ans = vandermonde(x, y)
ansF = [f"{'+' if i >= 0 else '-'} ({abs(i):.5f}x^{e})" for i,e in zip(ans,range(len(ans)))]
ansF[0] = ansF[0][1:-4]+')'
print(" ".join(ansF))



