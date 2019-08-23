from scipy import optimize

def f(x):
	return x**2+4*((2-x)/2)**2-4

minimum = optimize.brent(f,brack=(1,2))
print(minimum)