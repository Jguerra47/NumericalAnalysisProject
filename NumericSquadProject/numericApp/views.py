from django.shortcuts import render
from numericApp.methods.Interpolation.vandermonde import vandermondeAns
from numericApp.methods.Interpolation.lagrange import lagrange
from numericApp.methods.Interpolation.divideddiff import newton_interpolation
from numericApp.methods.Interpolation.spline1 import spline1Ans
from numericApp.methods.Interpolation.spline2 import spline2Ans
from numericApp.methods.Interpolation.spline3 import spline3Ans
from numericApp.methods.Roots.secant import secant
from numericApp.methods.LinearEquations.crout import croutAns
from numericApp.methods.LinearEquations.jacobi import jacobi_Ans
from numericApp.methods.Roots.incrementalSearch import incrementalSearch
# Create your views here.
from math import sqrt

def index(request):
    return render(request, "numericApp/index.html")

def notfound(request):
    return render(request, "numericApp/notfound.html")

def vandermonde_ep(request):
    if request.method == 'POST':
        X = []
        Y = []
        size = (len(request.POST) - 1)//2
        for i in range(size):
            X.append(float(request.POST["X"+str(i)]))
            Y.append(float(request.POST["Y"+str(i)]))

        matrix, coefficients, f = vandermondeAns(X, Y)
        return render(request, "numericApp/vandermonde.html", {
            "state": 1, #Carga correcta
            "coefficients":coefficients,
            "matrix":matrix,
            "f":f,
            "X":X,
            "Y":Y,
            "size":size
            })
    else:
        return render(request, "numericApp/vandermonde.html")

def lagrange_ep(request):
    if request.method == 'POST':
        X = []
        Y = []
        size = (len(request.POST) - 1)//2
        for i in range(size):
            X.append(float(request.POST["X"+str(i)]))
            Y.append(float(request.POST["Y"+str(i)]))

        lagrange_polynoms, polynom = lagrange(X, Y)
        return render(request, "numericApp/lagrange.html", {
            "state": 1, #Carga correcta
            "lPolynoms": lagrange_polynoms,
            "polynom": polynom,
            "X":X,
            "Y":Y,
            "size":size
            })
    else:
        return render(request, "numericApp/lagrange.html")

def newton_interpolation_ep(request):
    if request.method == 'POST':
        X = []
        Y = []
        size = (len(request.POST) - 1)//2
        for i in range(size):
            X.append(float(request.POST["X"+str(i)]))
            Y.append(float(request.POST["Y"+str(i)]))

        DDTable, polynom, coef = newton_interpolation(X, Y)
        return render(request, "numericApp/newton-interpolation.html", {
            "state": 1, #Carga correcta
            "DDTable": DDTable,
            "polynom": polynom,
            "X":X,
            "Y":Y,
            "size":size
            })
    else:
        return render(request, "numericApp/newton-interpolation.html")

def splines_ep(request):
    if request.method == 'POST':
        X = []
        Y = []
        size = (len(request.POST) - 1)//2
        for i in range(size):
            X.append(float(request.POST["X"+str(i)]))
            Y.append(float(request.POST["Y"+str(i)]))
        
        segments1,polBySeg1 = spline1Ans(X,Y)
        segments2,polBySeg2 = spline2Ans(X,Y)
        segments3,polBySeg3 = spline3Ans(X,Y)
        return render(request, "numericApp/splines.html", {
            "state": 1, #Carga correcta
            "segments1": zip(segments1,polBySeg1),
            "segments2": zip(segments2,polBySeg2),
            "segments3": zip(segments3,polBySeg3),
            "X":X,
            "Y":Y,
            "size":size
            })
    else:
        return render(request, "numericApp/splines.html")

#ROOTS METHODS
def incremental_search_ep(request):
    if request.method == 'POST':
        ans = incrementalSearch(request.POST['equation'],
        float(request.POST['x0']),
        float(request.POST['delta']),
        int(request.POST['iterations']))

        return render(request, "numericApp/incremental-search.html", {
            "state":1,
            "ans":ans,
            "equation":request.POST['equation'],
            "x0":request.POST['x0'],
            "delta":request.POST['delta'],
            "iterations":request.POST['iterations']
            })
    else:
        return render(request, "numericApp/incremental-search.html")

def secant_ep(request):
    if request.method == 'POST':
        ans, procedure = secant(request.POST['equation'],
        float(request.POST['x0']),
        float(request.POST['x1']),
        float(request.POST['tolerance']),
        int(request.POST['iterations']))

        return render(request, "numericApp/secant.html", {
            "state":1,
            "ans":ans,
            "procedure":procedure,
            "equation":request.POST['equation'],
            "x0":request.POST['x0'],
            "x1":request.POST['x1'],
            "tolerance":request.POST['tolerance'],
            "iterations":request.POST['iterations']
            })
    else:
        return render(request, "numericApp/secant.html")

#LINEAR EQUATIONS
def crout_ep(request):
    if request.method == 'POST':
        A = []
        b = []

        size= int(sqrt(len(request.POST)))
        for i in range(size):
            b.append([float(request.POST["B"+str(i)])])

        for i in range(size):
            q = []
            for j in range(size):
                q.append(float(request.POST["A"+str(i)+str(j)]))
            A.append(q)
        
        stages, x = croutAns(A, b)

        return render(request, "numericApp/crout.html", {
            "state":1,
            "A":A,
            "b":b,
            "size":size,
            "stages":stages,
            "x":x
            })
    else:
        return render(request, "numericApp/crout.html")


def jacobi_ep(request):
    if request.method == 'POST':
        A = []
        b = [] 
        x0 = []

        size = int(sqrt(len(request.POST)))-1
        for i in range(size):
            b.append([float(request.POST["B"+str(i)])])
            x0.append([float(request.POST["x0"+str(i)])])

        for i in range(size):
            q = []
            for j in range(size):
                q.append(float(request.POST["A"+str(i)+str(j)]))
            A.append(q)
        
        x,Tmatrix,iterations,spectralRadious = jacobi_Ans(A,b,float(request.POST['tolerance']),x0,int(request.POST['niter']))
        

        return render(request, "numericApp/jacobi.html", {
            "state":1,
            "A":A,
            "b":b,
            "x0":x0,
            "size":size,
            "tolerance":request.POST['tolerance'],
            "niter":request.POST['niter'],
            "Tmatrix":Tmatrix,
            "iterations":iterations,
            "spectralRadious":spectralRadious,
            "x":x
            })
    else:
        return render(request, "numericApp/jacobi.html")