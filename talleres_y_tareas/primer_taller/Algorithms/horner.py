import stdio
import stdarray
import sys
import math

def evaluate(x, a):
    result = 0
    for i in range(len(a)-1, -1, -1):
        result = a[i] + (x * result)
    return result

n = int(sys.argv[1])

a = stdarray.create1D(n, 0.0)
a[0] = 1.0
for i in range(1, n):
    a[i] = a[i-1] / float(i)

while not stdio.isEmpty():
    x = stdio.readFloat()
    stdio.writeln(evaluate(x, a))
    stdio.writeln(math.exp(x))
    stdio.writeln()
