import random
import math
import matplotlib.pyplot as plt

rou = 8
data_for_plot = []
def pso(equation, n_terms, n_particles, error):
	# Vector de velocidades para cada partícula
	velocities = [[round(random.random(),rou) for i in range(n_terms)] for j in range(n_particles+1)]
	# Vector de pesos para cada partícula
	weights = [[round(random.random(),rou) for i in range(n_terms)] for j in range(n_particles+1)]
	# El mejor valor que se ha encontrado en todo el grupo
	best_group_value = 99999.99
	# La solución para el mejor valor
	best_group_terms = [0.0 for i in range(n_terms)]
	# La mejor solución histórica para cada partícula
	best_history_terms_list = [[99999.99 for i in range(n_terms)] for j in range(n_particles)]
	# Las soluciones en las que cada partícula está trabajando, se actualiza en cada iteración
	actual_terms_list = [[round(random.random(),rou) for i in range(n_terms)] for j in range(n_particles)]
	iteration=0
	while(error<abs(equation(best_group_terms))):
		cont = 0
		# Por cada partícula
		for particle in range(n_particles):
			actual_terms = actual_terms_list[particle][:]
			best_terms = best_history_terms_list[particle][:]
			# f_value es el valor en el punto con los valores en actual_terms
			f_value=equation(actual_terms)
			# Si el valor con los nuevos terminos es mejor que el mejor valor, se guardan los términos
			if (abs(f_value) < abs(equation(best_terms))):
				best_history_terms_list[particle] = actual_terms[:]
			# Si el valor con los términos actuales es mejor que el mejor valor grupal.
			if (abs(f_value) < best_group_value):
				# Se actualizan los terminos del mejor valor grupal
				best_group_value=abs(f_value)
				best_group_terms = actual_terms[:]
			cont+=1

		for particle in range(n_particles):
			for term in range(n_terms):
				# Primer término aleatorio 
				r1=random.random()
				r2=random.random()
				r3=random.random()
				r4=random.random()
				r5=random.random()
				r6=random.random()
				r7=random.random()
				pbest=round(best_history_terms_list[particle][term],rou)
				gbest=round(best_group_terms[term],5)
				velocities[particle+1][term]=round((2*r1-0.5)*velocities[particle][term]+(2*r2-0.5)*(pbest-actual_terms[term])+(2*r3-0.5)*(gbest-actual_terms[term]),rou)
				v=round(velocities[particle+1][term],rou)
				weights[particle+1][term]=round((2*r4-0.5)*(gbest-pbest)+(2*r5-0.5)*(gbest-actual_terms[term]),rou)
				w=weights[particle+1][term]
				actual_terms_list[particle][term]=round(pbest+(2*r6-0.5)*v+(2*r7-0.5)*w,rou)
			data_for_plot.append(equation(best_group_terms))
			print(best_group_terms)
		iteration+=1
	print("Solución:")
	print(best_group_terms)
	print("Iteración:")
	print(iteration)
	return equation(best_group_terms)

def f(x):
	try:
		res = math.exp(x[1])+pow(x[0]+1,2)
	except OverflowError:
		res = float('inf')
	return res

fx=pso(f, 2, 12, 1e-4)
print("Valor hallado: ")
print(fx)

plt.plot(data_for_plot)
plt.ylabel('Convergencia')
plt.show()