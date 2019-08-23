# f: funcion
# i: numero de iteraciones
def aitken(f, i):
    x0= f(0)
    x1= f(1)
    x2= f(2)

    ax= x0 - (x1-x0)**2/(x2-2*x1+x0)

    axk=np.array([ax])
    xk=np.array([x0])
    for k in range(1, i):
        x0=x1
        x1=x2
        x2=f(k+2)
        if np.isclose(x2-2*x1+x0, 0.0):
            return ax, axk, xk

        ax= x0 - (x1-x0)**2/(x2-2*x1+x0)
        axk= np.append(axk, ax)
        xk= np.append(xk, x0)
    return ax, axk, xk

aitken(lambda x: x*3+3*x*2, 12)
