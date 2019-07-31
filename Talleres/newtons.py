import math
def newtons(f, df, xi, e):
	cont=0
	while(cont<e):
		x=xi-f(xi)/df(xi)
		xi=x
		cont+=1
		print('x: ',x)

newtons(lambda x: math.exp(x), lambda x: math.exp(x), 0, 8)