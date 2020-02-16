import matplotlib.pyplot as plt
import numpy as np

# sample plot x,y
x = range(0, 5)
y = [2, 7, 1, 5, 6]

plt.figure(figsize=(8, 5))
plt.axes().set_facecolor('purple')

# plot x,y
plt.plot(x, y)
plt.xlabel('x-axis')  # label x axis
plt.ylabel('y-axis')  # label y axis
plt.title('First Sample chart')  # chart title
# plt.show()  # display the chart on screen

# cosine plot using numpy

t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.cos(2 * np.pi * t)

plt.plot(t, s, '*')     # last param will chage the plot color
plt.grid()  # display grids in the plot
plt.axes().set_facecolor('black')
plt.xlabel('Time(t)')  # label x axis
plt.ylabel('Velocity(S)')  # label y axis
plt.title('cosine plot')  # chart title
plt.show()  # display the chart on screen
