import math
import numpy as np

def f(x):
    f=math.pow(x,3) + 2*math.pow(x,2) - 3*x - 1
    return f

def regulaFalsi(a,b,TOL,N):
    i=1
    FA=f(a)
    while(i <= N):
        p = (a*f(b)-b*f(a))/(f(b) - f(a))
        FP = f(p)
        if(FP == 0 or np.abs(f(p)) < TOL):
            break
        else:
             print("%-20.8g %-20.8g %-20.8g %-20.8g %-20.8g\n" % (i, a, b, p, f(p)))

        i=i + 1
        if(FA*FP > 0):
            a=p
        else:
            b=p
    return
