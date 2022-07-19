from matplotlib.backend_bases import MouseButton
import matplotlib.pyplot as plt
import numpy as np
import time
import math



class Plotter:
    def __init__(self) -> None:
        self.angle = 0
        self.idx = 0


fig, ax = plt.subplots(1,2)
plot_data1, = ax[0].plot([], [])
plot_data2, = ax[1].plot([], [])
fig.set_size_inches(14,8)
ax[0].set_ylim(0, 1)
ax[0].set_xlim(0, 1)

ax[1].set_ylim(0, 90)
ax[1].set_xlim(0, 1000)

angle = 0
plt.suptitle('angle 0')

t = np.linspace(0, 1000, 1000)

idx = 0

def updatePlot(angle):
    # plotting f(angle)
    x = np.linspace(0, 1, 100)
    rand = np.random.normal(scale = 0.1,size = x.shape)
    y = math.tan(math.radians(angle)) * x + rand
    plot_data1.set_xdata(x)
    plot_data1.set_ydata(y)

    # plotting angle(t)
    new_y = np.append(plot_data2.get_xdata(), angle)
    new_x = np.append(plot_data2.get_ydata(), t[plotter.idx])

    # in case of size missmatch
    if len(new_x) > len(new_y):
        padding = [new_y[-1]] * [len(new_x) - len(new_y)]
        new_y = np.append(new_y, padding)
    elif len(new_x) < len(new_y):
        padding = [new_x[-1]] * [len(new_y) - len(new_x)]
        new_x = np.append(new_x, padding)

    plot_data2.set_ydata(new_y)
    plot_data2.set_xdata(new_x)
    plotter.idx += 1    

    plt.draw()
    plt.pause(0.01)


def on_move(event):
    # get the x and y pixel coords
    x, y = event.xdata, event.ydata
    if event.inaxes:
        ax = event.inaxes  # the axes instance
        centered_y = (y - ax.get_ylim()[0])
        centered_x = (x - ax.get_xlim()[0]) 
        angle = np.degrees(np.arctan(centered_y / centered_x))
        print(f'data coords {x}, {y}, angle {angle}')
        updatePlot( angle)
        plt.suptitle(f'angle {angle}')


def on_click(event):
    if event.button is MouseButton.LEFT:
        print('disconnecting callback')
        plt.disconnect(binding_id)
        plt.close()
        exit()

binding_id = plt.connect('motion_notify_event', on_move)
plt.connect('button_press_event', on_click)

plotter = Plotter()

while True:
    
    fig.canvas.draw()
    fig.canvas.flush_events()
    time.sleep(0.01)
    plt.show()