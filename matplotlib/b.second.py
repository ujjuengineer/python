import matplotlib.pyplot as plt
import numpy as np

# print(matplotlib.__version__)

x = np.array([2024, 2025, 2026, 2027])
y1 = np.array([15, 25, 30, 20])
y2 = np.array([30, 12, 20, 25])

plt.plot(x,y1, marker=".", markersize=20)
plt.plot(x,y2, marker=".", markersize=20)


plt.show()