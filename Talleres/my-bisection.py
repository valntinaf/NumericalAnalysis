def bisection(f, a, b, e):
	c=(a+b)/2
	while abs(f(c) - 0) > e: 
		if f(a)*f(c) <0:
			b=c
		else:
			a=c
		c=(a+b)/2
	print(c)

bisection( lambda x: pow(x,2)+pow(9,12)*x-3,0,2, 0.001)