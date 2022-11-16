from django.shortcuts import render
from numericApp.methods.Interpolation.vandermonde import vandermondeAns

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