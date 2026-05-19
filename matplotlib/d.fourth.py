# bar chart : compare categoried of data by representing each category with a bar

import matplotlib.pyplot as plt
import numpy as np

# print(matplotlib.__version__)

categories = np.array(['a', 'b', 'c', 'd', 'e', 'f'])
values = np.array([4,3,2,5,3,1])


plt.bar(categories, values)


# for horizontal bar chart, you can use 
# plt.barh(categories, values)

plt.show()