# pie chart : circular chart divided into slices to show percentage of the total. 
# good for visualising distribution among categories

import matplotlib.pyplot as plt
import numpy as np

categories = ['a', 'b', 'c', 'd']
values = np.array([300, 250, 275, 225])

plt.pie(values, labels=categories,
                autopct="%1f")

# autopct will add percentage distributiioin on the chart




plt.show()