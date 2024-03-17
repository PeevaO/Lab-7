import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter

LENGTH = 2 * np.pi

print('Создание анимации...')
animation = PillowWriter(60)
fig = plt.figure()
ax = fig.add_subplot()

animation.setup(fig, 'sin(x).gif')

ax.set_title('График функции y = sin(x)')
ax.set_xlabel('x')
ax.set_ylabel('sin(x)')

xs = np.linspace(0, LENGTH, 100)
ys = np.sin(xs)
ax.plot(xs, ys)
dot, = plt.plot([0], [np.sin(0)], 'ro')
animation.grab_frame()

slides = np.linspace(0, LENGTH, 60)
for i in slides:
    dot.set_data(i, np.sin(i))
    animation.grab_frame()

animation.finish()
print('Создание анимации завершено. Получен файл sin(x).gif.')