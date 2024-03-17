import numpy as np
import matplotlib.pyplot as plt
from math import pi

MIN = -3 * pi
MAX = 3 * pi
NUMBERS = 50

xs = np.linspace(MIN, MAX, NUMBERS)
ys = xs * np.cos(xs)
zs = np.sin(xs)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_title('y=xcos(x), z=sin(x)')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.plot(xs, ys, zs, marker='x', c='red')
plt.show()