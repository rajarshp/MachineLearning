import random
import matplotlib.pyplot as plt

ages = random.sample(range(1, 100), 20)
print(ages)
bins = 10

ranges = (0, 100)

plt.hist(ages, bins, ranges, color=['orange'], rwidth=0.6, histtype='bar')
plt.xlabel('Ages')
plt.title("Histogram Plot")
plt.show()
