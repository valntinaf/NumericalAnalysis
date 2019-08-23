import numpy as np
def biseccion(f, a, b, tol=1.0e-6):
    if a &gt; b:
        raise ValueError("Intervalo mal definido")
    if f(a) * f(b) &gt;= 0.0:
        raise ValueError("La función debe cambiar de signo en el intervalo")
    if tol &lt;= 0:
        raise ValueError("La cota de error debe ser un número positivo")
    x = (a + b) / 2.0
    while True:
        if b - a &lt; tol:
            return x
        # Utilizamos la función signo para evitar errores de precisión
        elif np.sign(f(a)) * np.sign(f(x)) &gt; 0:
            a = x
        else:
            b = x
        x = (a + b) / 2.0