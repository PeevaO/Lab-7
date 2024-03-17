import numpy as np
import matplotlib.pyplot as plt
import csv

COLUMN = 5
NUMBER_COLUMNS = 20

with open('data2.csv', 'r') as table:
    table = list(csv.reader(table, delimiter=','))
    table.pop(0)
    data = np.array([])
    for row in table:
        if row[COLUMN - 1] != '':
            data = np.append(data, float(row[COLUMN - 1]))

deviation = np.std(data)
print(f'Среднеквадратичное отклонение {deviation}.')

fig = plt.figure(figsize=(10, 4))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)
fig.subplots_adjust(wspace=0.5)

ax1.hist(data, bins=NUMBER_COLUMNS)
ax1.set_title('Распределение')
ax1.set_xlabel('значение измерения')
ax1.set_ylabel('интервалы измерений')

ax2.hist(data, bins=NUMBER_COLUMNS, density=True)
ax2.set_title('Выровненное распределение')
ax2.set_xlabel('значение измерения')
ax2.set_ylabel('интервалы измерений')
plt.show()