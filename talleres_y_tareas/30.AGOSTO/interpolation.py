from scipy.interpolate import lagrange
import numpy as np
import matplotlib.pyplot as plt 

# Puntos dados
x=[14.6, 14.7, 14.6, 14.8, 15.2, 15.6, 15.7, 17.0, 17.6, 17.5, 17.3, 16.8, 15.4, 14.8, 14.4, 14.5, 15.0, 15.1, 15.0, 14.9, 14.6, 14.3, 14.0, 13.9, 13.8, 13.5, 13.1, 13.0, 13.3, 13.2, 13.1, 12.9, 12.4, 11.9, 11.7, 11.6, 11.3, 10.9, 10.7, 10.6, 10.6, 10.1, 9.7, 9.4, 9.3, 9.6, 9.9, 10.1, 10.2, 10.3, 9.10, 8.6, 7.5, 7.0, 6.7, 6.6, 7.70, 8.00, 8.10, 8.40,              9.00, 9.30, 10, 10.2, 10.3, 10.0, 9.50]                                                                                                      
y=[14.7, 14.0, 13.4, 12.3, 11.0, 10.5, 10.2, 8.20, 7.10, 6.70, 6.60, 6.80, 8.30, 8.80, 9.30, 8.80, 6.30, 5.50, 5.00, 4.70, 4.60, 4.50, 4.90, 5.40, 5.80, 6.90, 8.20, 7.60, 5.80, 4.50, 4.30, 3.90, 4.20, 5.70, 7.00, 7.90, 8.20, 7.30, 6.70, 5.50, 5.10, 4.60, 4.7, 5.0, 5.5, 7.2, 7.8, 8.60, 9.40, 10.0, 10.7, 9.9, 9.0, 9.1, 9.3, 9.7, 11.7, 12.3, 12.5, 13.0,              13.9, 14.9, 16, 16.4, 16.8, 10.7, 11.0]    

# Retorna un polinomio encontrado por lagrange
p=lagrange(x[32:36],y[32:36])

# Arreglos de puntos según el polinomio de Lagrange entre los puntos 32 y 35
x1=np.linspace(x[32],x[35],10) 
y1=p(x1)

# Grafica los todos los puntos dados.
plt.plot(x1,y1,label='interpolación')
# Grafica los puntos en el polinomio.
plt.plot(x,y,'x', mew=2, label='Datos')

# Datos de plot
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()

#Mostrar gráfica
plt.show()