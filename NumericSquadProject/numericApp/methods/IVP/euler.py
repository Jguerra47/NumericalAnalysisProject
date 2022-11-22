import sympy as sm

xx = sm.symbols('x')
yy = sm.symbols('x')

def euler( x0, y, h, x,f):
	f = sm.sympify(f)
	while x0 < x:
		# y = y + h * func(x0, y)
		y = y + h * float(f.subs(xx,x0).subs(yy,y))
		x0 = x0 + h

	return("Approximate solution at x = "+ str(x)+ " is ", "%.5f"% y)
	

# x0 = 0
# y0 = 1
# h = 0.025
# x = 0.1

# euler(x0, y0, h, x)
