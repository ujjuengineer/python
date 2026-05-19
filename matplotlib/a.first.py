import matplotlib.pyplot as plt
import numpy as np

# print(matplotlib.__version__)

x = np.array([2024, 2025, 2026, 2027])
y = np.array([15, 25, 30, 20])

plt.plot(x,y, marker=".", markersize=30, markerfacecolor='red',
         linestyle="solid")
# bydefault linestyle = solid, but you can change it to dotted, dashed, dashdot
# you can also cahnge the line width, and line color, 'linewidth', 'color'

plt.show()