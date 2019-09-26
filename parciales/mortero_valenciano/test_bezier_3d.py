import numpy as np
import matplotlib.pyplot as plt
import bezier 
from mpl_toolkits import mplot3d

def mortero( gauge, height, density ):
	fig = plt.figure()
	ax = plt.axes(projection='3d')
	zline = np.linspace(1, height, density)
	for z in zline:
		points = np.asfortranarray([
			[gauge*z*-1, z, gauge*z],
			[0, 		 -1*gauge*z, 0]])
		curve = bezier.Curve( points , degree=3 )
		xline = np.linspace(-density, density, density)
		yline = curve.evaluate_multi(xline)[1]
		zline = [z for i in range(density)]
		ax.scatter(xline, yline, zline, zdir='z', s=density)

		print(yline)
	plt.show()

mortero(8, 10, 50)

#