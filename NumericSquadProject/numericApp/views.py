from django.shortcuts import render
from numericApp.methods.Interpolation.vandermonde import vandermondeAns
from numericApp.methods.Interpolation.lagrange import lagrange
from numericApp.methods.Interpolation.divideddiff import newton_interpolation

# Create your views here.

def index(request):
    return render(request, "numericApp/index.html")

def notfound(request):
    return render(request, "numericApp/notfound.html")

# def vander_not(request):
#     return render(request, "numericApp/vandermonde.html")

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