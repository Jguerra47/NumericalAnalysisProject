import sympy as sm

xx = sm.symbols('x')
yy = sm.symbols('x')
	
def heun(t, y, h, x,f):
	f = sm.sympify(f)
	while t < x:
		# y0 = y + h * func(t, y) #Predictor
		y0 = y + h * float(f.subs(xx,t).subs(yy,y))
		# y = y + h/2 * func(t, y)+func(t+h, y0) #Corrector
		y = y + h/2 * float(f.subs(xx,t).subs(yy,y))+float(f.subs(xx,t+h).subs(yy,y0))
		t = t + h #Jump

	return("Approximate solution at x = "+ str(x)+ " is "+ "%.10f"% y)
	
# t0 = 0
# y0 = 1
# h = 0.025
# x = 0.1

# heun(t0, y0, h, x)