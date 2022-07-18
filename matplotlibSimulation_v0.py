import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('seaborn-pastel')


def trajectory(x, alpha, v):
    return x * np.tan(alpha) - (g * np.power(x, 2))/(2 * np.power(v, 2) * np.power(np.cos(alpha), 2))


def envelope(x, v):
    return np.power(v, 2) / (2 * g) - g * np.power(x, 2) / (2 * np.power(v, 2))


def init():
    for line in lines:
        line.set_data([], [])

    return lines


def animate(i):
    x = points_x[i, :i]
    y = points_y[i, :i]
    lines[0].set_data(x, y)
    xq = np.linspace(0, xlim, 1000) # dodati ako zelis da se iscrta envelopa
    yq = envelope(xq, v0)
    lines[1].set_data(xq, yq)
    return lines


n = 300
alpha = np.zeros(n)
# ovde ubaciti zavisnost ugla od vremena
for i in range(n):
    alpha[i] = (2.7 / 8) * np.pi + (np.pi / 8) * np.sin(np.pi * 0.03 * i)
v0 = 12
g = 9.81
points_x = np.zeros((n, n))
points_y = np.zeros((n, n))

for i in range(n):
    for j in range(i):
        t = (i - j) * 0.01
        v0x = v0 * np.cos(alpha[j])
        v0y = v0 * np.sin(alpha[j])
        points_x[i, j] = v0x * t
        points_y[i, j] = v0y * t - g * np.power(t, 2) / 2


fig = plt.figure()
fig.patch.set_facecolor('#d5dbe7')
xlim = 12
ylim = 8
ax = plt.axes(xlim=(0, xlim), ylim=(0, ylim)) # dimenzije grafika
ax.set_facecolor("#d5dbe7")
N = 2
colors = ['#1f2326', '#1a494f']
linestyles = ['-', '--']
lines = [plt.plot([], [], color=colors[i], linestyle=linestyles[i])[0] for i in range(N)]

anim = FuncAnimation(fig, animate, init_func=init,
                               frames=n, interval=20, blit=True)
anim.save("water_hose.gif", writer='Pillow')