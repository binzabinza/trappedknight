import matplotlib.pyplot as plt
import mpl_toolkits
from mpl_toolkits.mplot3d import Axes3D

f = open("results.txt")
line = f.readline().split()

x = []
y = []
z = []

while line:
    line = f.readline().split()
    if len(line) == 0 : break
    x.append(int(line[0]))
    y.append(int(line[1]))
    z.append(int(line[2].strip()))

f.close()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z)
plt.show()


