#Solucionar sistemas de ecuaciones lineales con python
import numpy as np

A = np.array([[1,0,0,0], [1,4,0,0], [1,6,6*2,0],[1,10,10*6,10*6*4]])
b = np.array([9,18,21,15])
res = np.linalg.solve(A, b)

print(res)
a0=res[0]
a1=res[1]
a2=res[2]
a3=res[3]
x0=8
x1=12
x2=14
x3=18

pol=lambda x: a0+a1*(x-x0)+a2*(x-x0)*(x-x1)+a3*(x-x0)*(x-x1)*(x-x2)

print(pol(10))
print(pol(16))
