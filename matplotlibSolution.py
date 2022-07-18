from re import X
from matplotlib.backend_bases import MouseButton
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 1.0, 0.01)
s = np.sin(2 * np.pi * t)
fig, ax = plt.subplots()
ax.plot(t, s)

angle = 0

def on_move(event):
    # get the x and y pixel coords
    x, y = event.xdata, event.ydata
    if event.inaxes:
        ax = event.inaxes  # the axes instance
        centered_y = (y - ax.get_ylim()[0])
        centered_x = (x - ax.get_xlim()[0]) 
        angle = np.degrees(np.arctan(centered_y / centered_x))
        print(f'data coords {x}, {y}, angle {angle}')


def on_click(event):
    if event.button is MouseButton.LEFT:
        print('disconnecting callback')
        plt.disconnect(binding_id)


binding_id = plt.connect('motion_notify_event', on_move)
plt.connect('button_press_event', on_click)

plt.show()