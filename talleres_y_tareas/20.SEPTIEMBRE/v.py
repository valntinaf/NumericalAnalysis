import matplotlib.path as mpath
import matplotlib.patches as mpatches

import matplotlib.pyplot as plt

Path = mpath.Path

fig, ax = plt.subplots()

pp0 = mpatches.PathPatch(
    Path([(3, 10), (-2, 10), (2, 11), (0, 15)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3, Path.MOVETO]),
    fc="none", transform=ax.transData)

pp1 = mpatches.PathPatch(
    Path([(2, 11), (5, 12), (10, 12), (8, 12)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3, Path.MOVETO]),
    fc="none", transform=ax.transData)

pp2 = mpatches.PathPatch(
    Path([(7, 12), (7, 2), (2, 0), (3, 0)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3, Path.MOVETO]),
    fc="none", transform=ax.transData)

pp3 = mpatches.PathPatch(
    Path([(2, 0), (-3, 2), (7, 8), (0, 8)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3, Path.MOVETO]),
    fc="none", transform=ax.transData)

ax.set(xlim=(0, 14), ylim=(0, 14))
ax.add_patch(pp0)
ax.add_patch(pp1)
ax.add_patch(pp2)
ax.add_patch(pp3)
plt.show()
