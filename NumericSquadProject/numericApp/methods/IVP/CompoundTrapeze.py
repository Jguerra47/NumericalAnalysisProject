import sympy as sm 


x = sm.symbols('x')

def CompoundTrapeze(a,b,f,n):
    f = sm.sympify(f)
    deltaX = (b-a)/n
    A = 0
    # ans = []
    for i in range(n):
        xi =  a + i * deltaX
        fxi = float(f.subs(x,xi))
        if i > 0 and i < n:
            fxi = 2*fxi
        # ans.append([i+1,xi,fxi])
        A = A + fxi
    A = A * (deltaX/2)
    return A

# f = sm.ln(sm.sin(x) ** 2+1)-(1/2)
# a = 1
# b = 10
# n = 20
# print(str(CompoundTrapeze(a,b,f,b))+" is the result of the integral")