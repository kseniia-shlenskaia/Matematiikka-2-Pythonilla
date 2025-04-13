import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-3 * np.pi, 3 * np.pi, 1000)
C = np.cos(X)
S = np.sin(X)

fig, ax = plt.subplots(figsize=(19.2, 4.8))

ax.plot(X, C, color='red', linestyle='--', label='cos(x)')
ax.plot(X, S, color='blue', linestyle='-.', label='sin(x)')

ax.legend()

xticks = np.linspace(-3 * np.pi, 3 * np.pi, 13)
xtick_labels = [
    r"$-3\pi$", r"$-5\pi/2$", r"$-2\pi$", r"$-3\pi/2$", r"$-\pi$", r"$-\pi/2$",
    r"$0$", r"$\pi/2$", r"$\pi$", r"$3\pi/2$", r"$2\pi$", r"$5\pi/2$", r"$3\pi$"
]

ax.set_xticks(xticks)
ax.set_xticklabels(xtick_labels)

ax.grid(True)
plt.show()