from django.shortcuts import render
from numericApp.methods.Interpolation.vandermonde import vandermonde

# Create your views here.

def index(request):
    return render(request, "numericApp/index.html")

def notfound(request):
    return render(request, "numericApp/notfound.html")

def vander_not(request):
    return render(request, "numericApp/vandermonde.html")

def vandermonde_ep(request):
    x = [-1, 0, 3, 4]
    y = [15.5, 3, 8, 1]

    coefficients, matrix = vandermonde(x, y)
    return render(request, "numericApp/vandermonde.html", {
        "coefficients":str(coefficients),
        "matrix":str(matrix)
        })