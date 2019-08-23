from scipy import optimize

def f(x):
	return x**3

minimum = optimize.brent(f,brack=(1,2))
print(minimum)
A={(lambda x: x**2),(lambda x:Math.exp(x)),(lambda x:3*x)}
