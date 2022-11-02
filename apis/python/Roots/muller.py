import sympy as sm 
import numpy as np 
import math
import matplotlib.pyplot as plt

x = sm.symbols('x')

def muller(f,x0,x1,tol,n):
    fx0 = float(f.subs(x,x0))
    fx1 = float(f.subs(x,x1))
    x2 = (x0+x1)/2
    fx2 = float(f.subs(x,x2))

    h0 = x1-x0
    h1 = x2-x1
    delta0 = (fx1 -fx0) / h0
    delta1 = (fx2 -fx1) / h1

    a = (delta1 - delta0) / (h1 - h0)
    b = a * (h1) + delta1
    c = fx2

    xi = x2 + (-2*c) / (b+(b / abs(b))* math.sqrt(b**2-4*a*c))
    fxi = float(f.subs(x,xi))
    error = abs(xi-x2)
    counter = 0
    matrix = [["counter","xi","fxi","error"]]
    matrix.append([counter,xi,fxi,error])

    while (fxi != 0 and error > tol and counter < n):
      x2Aux = x2
      x1Aux = x1
      x2 = xi
      x1 = x2Aux
      x0 = x1Aux
      fx0 = float(f.subs(x,x0))
      fx1 = float(f.subs(x,x1))
      fx2 = float(f.subs(x,x2))

      h0 = x1 - x0
      h1 = x2 - x1
      delta0 = (fx1 -fx0) / h0
      delta1 = (fx2 -fx1) / h1; 

      a = (delta1 - delta0) / (h1 - h0)
      b = a * (h1) + delta1
      c = fx2

      xi = x2 + (-2*c) / (b+(b / abs(b))* math.sqrt(b**2-4*a*c))
      fxi = float(f.subs(x,xi))
      error = abs(xi-x2)
      counter = counter + 1
      matrix.append([counter,xi,fxi,error])
    
    if fxi == 0:
      ans = 'The root has been found and it is: ', xi
    elif error <= tol:
      ans = 'An approximation has been found and is: ', xi
    else:
      ans = 'The method fails with the maximum number of iterations given'
    return ans,matrix


f = sm.ln(sm.sin(x) ** 2+1)-(1/2)
x0 = 1
x1 = 10
tol = 1e-7
niter = 20

ans,matrix = muller(f,x0,x1,tol,niter)
print(ans)
print()
if len(matrix)>1:
  print(f"%11s | %15s | %15s | %15s"%(matrix[0][0],matrix[0][1],matrix[0][2],matrix[0][3]))
  i = 1
  while (i < len(matrix)):
    print(f"%11s | %15E | %15E | %15E"%(matrix[i][0],matrix[i][1],matrix[i][2],matrix[i][3]))
    i += 1