import numpy as np
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
import math
from prettytable import PrettyTable

def prettyPrint(name,matrix):
    n = len(matrix)
    table = PrettyTable()
    table.field_names = [f"{name}{i}" for i in range(n)]
    table.add_rows(matrix)
    print(table)

def newton(n, x, y):
	tabla = np.zeros((n+1,n+1))

	for i in range(n):
		tabla[i][0] = x[i]
		tabla[i][1] = y[i]

	res = polinomioNewton(tabla,n).tolist()
	#print (res)
	for i in range(len(res)):
		res[i].pop(0)
	res.pop()
	return np.array(res).tolist()


def polinomioNewton(tabla,n):
    polinomio = "P(X) = " + str(tabla[0][1])
    coef = []
    coef.append(str(tabla[0][1]))
    for j in range(2,n+1):
        for i in range(j-1,n):
            tabla[i][j] = (tabla[i][j-1] - tabla[i-1][j-1])/(tabla[i][0] - tabla[i-j+1][0])
            
            if(i==j-1):
                coef.append(tabla[i][j])
                polinomio += " + " + str(tabla[i][j])
                for i in range(0,i):
                    polinomio += "(x - " + str(tabla[i][0]) + ")"
    table = PrettyTable()
    table.field_names = [f"x{i}" for i in range(len(coef))]
    table.add_row(coef)
    print("\nPolynomial coefficients:")
    print(table)
    print("\nNewton’s Divided Difference Table")
    printTable(tabla,n)
    F = parse_expr(polinomio.replace("P(X) = ","").replace("(","*("))
    polinomio = polinomio.replace("- -","+").replace("+ -","-").replace("- +","-").replace("(x - 0.0)","x").replace("(x + 0.0)","x")
    print("\nNewton's polynom\n" + polinomio)

    return tabla

def printTable(tabla,n):
    #print(tabla)
    table = PrettyTable()
    row = ["n", "xi"]+[f"{i}º" for i in range(n)]
    table.field_names = row
    for i in range(n):
        a = [i]
        for item in tabla[i]:
            a.append(item)
        table.add_row(a)
    print(table)

newton(4,[-1,0,3,4],[15.5,3,8,1])