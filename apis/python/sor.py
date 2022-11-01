from math import fabs
from prettytable import PrettyTable
table = PrettyTable()

def sor(A, b, tol, w):

	n = len(A)
	Xk = [0.0]*n
	sumation = 0.0
	for i in range(n):
		if A[i][i] == 0:
			exit('Los elementos A[i][i] deben ser diferentes de 0')

	Xk1 = [b[i]/float(A[i][i]) for i in range(n)]
	minus = lambda x, y: [x[i]-y[i] for i in range(n)]

	for j in range(n):
	 	dominancia = 0.0
	 	for i in range(n):
	 		if j != i:
	 			dominancia += fabs(A[i][j])
	 	if A[i][i] < dominancia:
	 		exit('La matriz no converge')
	itera = 0
	err = None

	while(norm(minus(Xk1,Xk)) / float(norm(Xk1))) > tol:
		rowAux = [itera] + ["%.5f"%value for value in Xk] + [err] 
		table.add_row(rowAux)
		Xk[:] = Xk1[:]
		for i in range(n):
			sumation1 = sum(A[i][j]*Xk1[j] for j in range(i))
			sumation2 = sum(A[i][j]*Xk1[j] for j in range(i+1, n))
			err=(norm(minus(Xk1,Xk)) / float(norm(Xk1)))
			Xk1[i] = (float(w)/A[i][i])*(b[i] - sumation1 - sumation2) + (1-w)*Xk[i]
		itera += 1

	return Xk1

def normxd(x):
    return max([fabs(x) for x in x]) #Norm inf

def norm(L):
	""" Calcula la norma infinita de un vector:
		||x|| = max {|xi|}, i = 0, 1, ... n.
	"""

	maximum = fabs(L[0])
	for i in range(1, len(L)):
		maximum = max(maximum, fabs(L[i]))
	return maximum	


A = [[4,-1,0,3],[1,15.5,3,8],[0,-1.3,-4,1.1],[14,5,-2,30]]
b=[1,1,1,1]
tol=1e-7
w=0.7
sor(A,b,tol,w)
n = len(A)
table.field_names = ["Iteracion"] + [f"x{i}" for i in range(n)]  + ["Error"]
print(table)