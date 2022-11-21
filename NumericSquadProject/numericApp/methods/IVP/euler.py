
# dy / dx =(x + y + xy)
def func( x, y ):
	return (x + y + x * y)
	
def euler( x0, y, h, x):

	while x0 < x:
		y = y + h * func(x0, y)
		x0 = x0 + h

	print("Approximate solution at x = ", x, " is ", "%.5f"% y)
	

# x0 = 0
# y0 = 1
# h = 0.025
# x = 0.1

# euler(x0, y0, h, x)
