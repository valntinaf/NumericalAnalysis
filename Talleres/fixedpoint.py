import math
# x = valor inicial
# gx función despejada
# En el intervalo [a,b]
def fixedpoint(x, gx, n):
	cont=0
	while(cont < n):
		x=gx(x)
		print(x)
		cont+=1


fixedpoint(0, lambda x: math.exp(-x), 20)