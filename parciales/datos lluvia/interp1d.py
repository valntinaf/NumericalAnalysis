from scipy.interpolate import BarycentricInterpolator, interp1d
import numpy as np
import matplotlib.pyplot as plt 

f1 = lambda x: 2*x+1
f2 = lambda x: x+2
x = [6, 6, 2, 2, 3, 3, 4, 4, 5, 5]
y = [f1(6), f2(6), f1(2), f2(2), f1(3), f2(3), f1(4), f2(4), f1(5), f2(5) ]

f = interp1d(x, y)
print(f(2.5))

xnew = np.arange(2, 6, 0.1)
ynew = f(xnew)

plt.plot(x, y, 'o', xnew, ynew, '-')
# Datos de plot
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()