import matplotlib.pyplot as plt
import numpy as np
import bezier

nodes1 = np.asfortranarray([
[1.0, 1.0, 3.0, ],
[1.0, 3.0, 3.0, ],
])

curve1 = bezier.Curve.from_nodes(nodes1, degree=2)
ax = curve1.plot(num_pts=256)
plt.show()
