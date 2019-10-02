from scipy.interpolate import lagrange
import numpy as np
import matplotlib.pyplot as plt 

f1 = lambda x: 2*x+1
f2 = lambda x: x+2
x = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
y = [f1(1), f2(1), f1(2), f2(2), f1(3), f2(3), f1(4), f2(4), f1(5), f2(5) ]

f = lagrange(x, y)
print(f(2.5))

xnew = np.arange(1, 5, 0.1)
ynew = f(xnew)

plt.plot(x, y, 'o', xnew, ynew, '-')
# Datos de plot
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()