# f: funcion
# df: derivada de la funcion
# xi: valor inicial
# e: error tolerado
from sympy import *
import sympy
#import matplotlib.pyplot as plt
def newtons(f, df, xi, yi, e):
	cont=0
	while(cont<e):
		x=xi-f(xi,yi)/df(xi,yi)
		x=yi-f(xi,yi)/df(xi,yi)
		xi=x
		yi=y
		cont+=1

# f1(e^x)=e^x
f = lambda x, y: x+(x+y)*Math.exp(x+y)-3-x-(x+y)*Math.exp(2*x+y)+4
df = lambda x, y: x+(x+y)*Math.exp(x+y)-3-x-(x+y)*Math.exp(2*x+y)+4
newtons(f, df, 0, 9)