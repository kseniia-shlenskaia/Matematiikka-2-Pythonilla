from matplotlib import pyplot as plt, patches
import numpy as np

fig = plt.figure()
ax = fig.subplots()

circle = patches.Circle((0, 0), radius=1, fill=False)
ax.add_patch(circle)

ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.axis('equal')

plt.xticks([-1, 0, 1])
plt.yticks([-1, 0, 1])

angles_deg = [30, 45, 60, 90, 120, 150, 180, 270]
angles_rad = np.radians(angles_deg)

x = np.cos(angles_rad)
y = np.sin(angles_rad)

plt.scatter(x, y, color='black', marker='X')

for i in range(len(angles_deg)):
    ax.annotate(
        f"{angles_deg[i]}°",
        xy=(x[i], y[i]),
        xytext=(10, 10),
        textcoords='offset points',
        fontsize=10,
        arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0")
    )

plt.grid(True)
plt.show()
