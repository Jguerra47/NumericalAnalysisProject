import sympy as sm

x = sm.symbols('x')

def simpson38(leftLimit, rightLimit, n ,f):
    f = sm.sympify(f)
    interval_size = (float(rightLimit - leftLimit) / n)
    sumi = f.subs(x,leftLimit) + f.subs(x,rightLimit)

    for i in range(1, n ):
        if (i % 3 == 0):
            sumi = sumi + 2 * float(f.subs(x,leftLimit + i * interval_size))
        else:
            sumi = sumi + 3 * float(f.subs(x,leftLimit + i * interval_size))
     
    return (( 3 * interval_size) / 8 ) * sumi 
 

# n = 10
# leftLimit = 1
# rightLimit = 10
 
# print("%.5f"% simpson(leftLimit, rightLimit, n))