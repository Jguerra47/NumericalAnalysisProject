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
        x = []
        y = []
        for i in range(int(request.POST["size"])):
            x.append(float(request.POST["x"+str(i)]))
            y.append(float(request.POST["y"+str(i)]))

        matrix, coefficients, f = vandermondeAns(x, y)
        return render(request, "numericApp/vandermonde.html", {
            "state": 1, #Carga correcta
            "coefficients":coefficients,
            "matrix":matrix,
            "f":f
            })
    else:
        return render(request, "numericApp/vandermonde.html")