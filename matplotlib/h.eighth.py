# scattered graph : shows the relationship between 2 variable
# helps to identify a correlation (+, -, None)
# example : study hours vs test scores

import matplotlib.pyplot as plt
import numpy as np

x = [0, 1, 1, 2, 3, 4, 5, 6, 7, 7, 8]
y = [55, 60, 65, 62, 68, 70, 75, 78, 82, 85, 87]

plt.scatter(x,y, color = 'red',
                alpha=0.5,
                s = 100)

# alpha : transparency 
# s : size


plt.xlabel("hours studied")
plt.ylabel("grade")

plt.title("test score")

plt.show()