import sympy as sm

xx = sm.symbols('x')


def simpson13(leftLimit, rightLimit, n,f):
	f = sm.sympify(f)
	h = ( rightLimit - leftLimit )/n	
	x = []
	fx = []
	
	i = 0
	while i<= n:
		x.append(leftLimit + i * h)
		fx.append(float(f.subs(xx,x[i])))
		i += 1

	ans = 0
	i = 0
	while i<= n:
		if i == 0 or i == n:
			ans+= fx[i]
		elif i % 2 != 0:
			ans+= 4 * fx[i]
		else:
			ans+= 2 * fx[i]
		i+= 1
	ans = ans * (h / 3)
	return ans
	

# leftLimit = 4 
# rightLimit = 5.2 
# n = 6 
# print("%.5f"% simpson(leftLimit, rightLimit, n))
