import bezier
import numpy as np
import matplotlib.pyplot as plt

nodes = np.asfortranarray([
     [-2.0, 0.0, 2.0],
     [0.0, 4.0  , 0.0],
 ])
curve = bezier.Curve(nodes, degree=2)
ax = curve.plot(num_pts=256)
plt.show()