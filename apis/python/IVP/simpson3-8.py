import math

def func(x):
	return math.log(x)

def calculate(leftLimit, rightLimit, n ):
     
    interval_size = (float(rightLimit - leftLimit) / n)
    sumi = func(leftLimit) + func(rightLimit)

    for i in range(1, n ):
        if (i % 3 == 0):
            sumi = sumi + 2 * func(leftLimit + i * interval_size)
        else:
            sumi = sumi + 3 * func(leftLimit + i * interval_size)
     
    return (( 3 * interval_size) / 8 ) * sumi )
 

n = 10
leftLimit = 1
rightLimit = 10
 
print("%.5f"% simpson(leftLimit, rightLimit, n))