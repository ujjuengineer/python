# you can explode the pie chart using explode argument 

import matplotlib.pyplot as plt
import numpy as np

categories = ['a', 'b', 'c', 'd']
values = np.array([300, 250, 275, 225])


colors = ['red', 'blue', 'green', 'pink']

plt.pie(values, labels=categories,
                autopct="%1.1f%%", 
                colors=colors,
                explode=[0,0,0,0.1],
                shadow=True,
                startangle=90) # this will explode the 4th color


# you can add title
plt.title("ujju ka title")

plt.show()
