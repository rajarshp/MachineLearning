import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 2.0)

y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
y2 = np.cos(2 * np.pi * x2)

plt.subplot(2, 1, 1)    # create a chart with 2 rows 1 column and first position is occupied by subplot 1
plt.title('Subplot 1')
plt.xlabel('X1')
plt.ylabel('Y1')
plt.plot(x1, y1, '--')

plt.subplot(2, 1, 2)     # create a chart with 2 rows 1 column and first position is occupied by subplot 2
plt.title('Subplot 2')
plt.xlabel('X2')
plt.ylabel('Y2')
plt.plot(x2, y2, '.-')

plt.show()

