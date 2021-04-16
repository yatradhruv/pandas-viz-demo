import matplotlib.pyplot as plt
import numpy as np

mylabels = ["Python," "Javascript", "Java", "C++"]
arr = np.array[20, 50, 12, 18]

plt.pie(arr, labels = mylabels, autopct='%1, f%%', startangle = 90)
plt.show
