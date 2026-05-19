# you can add custom color to the pie chart


import matplotlib.pyplot as plt
import numpy as np

categories = ['a', 'b', 'c', 'd']
values = np.array([300, 250, 275, 225])


colors = ['red', 'blue', 'green', 'pink']

plt.pie(values, labels=categories,
                autopct="%1.1f%%", colors=colors)


# you can add title
plt.title("ujju ka title")

plt.show()
