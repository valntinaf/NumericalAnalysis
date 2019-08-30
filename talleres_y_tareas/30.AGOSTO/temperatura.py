from scipy.interpolate import lagrange
import numpy as np
import matplotlib.pyplot as plt 

# Datos de temperatura.
Hora=[6,8,10,12,14,16,18,20]
Grados=[7,9,12,18,21,19,15,10]

# Interpolación por el método de Lagrange
p=lagrange(Hora,Grados)
x1=np.linspace(min(Grados),max(Grados),10)
y1=p(x1)

# Gráfico de los puntos según polinomio de Lagrange
plt.plot(x1,y1,label='interpolación')
# Gráfico de los puntos dados
plt.plot(Hora,Grados,'x', mew=2, label='Datos')

# Datos de plot
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
print(p(13))

# Gráfico de la temperatura a las 13 horas, según polinomio de Lagrange.
plt.plot(13, p(13), 'r.')

# Mostrar gráfico.
plt.show()