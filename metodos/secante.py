# f: funcion
# xi: valor inicial
# xj: valor siguiente
# i: numero de iteraciones
import math
def newtons(f, xi, xj, i):
	cont=0
	while(cont<e):
		x=xi-f(xi)/((f(xj)-f(xi))/(xj-xi))
		xi=x
		cont+=1
		print('x: ',x)

# e^x-pi*x
newtons(lambda x: math.exp(x)-math.pi*x , 0, 1, 9)
