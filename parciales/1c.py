import matplotlib.pyplot as plt

def primeros_cuadrados(n):
	suma=0
	data=[]
	for i in range(n):
		suma+=pow(i,2)
		data.append(suma)
	plt.plot(data)
  	plt.ylabel('Convergencia')
  	plt.show()

primeros_cuadrados(5)
