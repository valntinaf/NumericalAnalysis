def newton(f, df, x_0, maxiter=50, xtol=1.0e-6, ftol=1.0e-6):
    x = float(x_0)  # Se convierte a número de coma flotante
    for i in xrange(maxiter):
        dx = -f(x) / df(x)  # ¡Aquí se puede producir una división por cero!
                            # También x puede haber quedado fuera del dominio
        x = x + dx
        if abs(dx / x) &lt; xtol and abs(f(x)) &lt; ftol:
            return x
    raise RuntimeError("No hubo convergencia después de {}
                        iteraciones".format(maxiter))