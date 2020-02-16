import numpy as np
import matplotlib.pyplot as plt

x = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
y = [200, 123, 450, 245, 12]
label = ['Jan', 'Feb', 'Mar', 'Apr', 'May']

plt.bar(x, y, tick_label=label, width=0.5, color=['blue', 'yellow'])
plt.xlabel('')
plt.ylabel('Sale')
plt.title('Bar Plot')
plt.show()