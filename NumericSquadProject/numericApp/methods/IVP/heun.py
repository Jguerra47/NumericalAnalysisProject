#Rewrite function in y'= hf(t,y) form
def func(x, y):
	return (x + y + x * y)
	
def heun(t, y, h, x):
	while t < x:
		y0 = y + h * func(t, y) #Predictor
		y = y + h/2 * func(t, y)+func(t+h, y0) #Corrector
		t = t + h #Jump

	print("Approximate solution at x = ", x, " is ", "%.5f"% y)
	
# t0 = 0
# y0 = 1
# h = 0.025
# x = 0.1

# heun(t0, y0, h, x)