import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
import numpy as np

# Function to generate random data
def generate_data():
    return np.random.random()

# Set up the figure and axis
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)

# Initialization function
def init():
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 1)
    line.set_data([], [])
    return line,

# Update function for animation
def update(frame):
    xdata.append(frame)
    ydata.append(generate_data())
    line.set_data(xdata, ydata)
    ax.set_xlim(0, max(10, frame + 1))
    return line,

# Data lists
xdata = []
ydata = []

# Create an animation
ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, 100, 100), init_func=init, blit=True)

# Show plot
plt.show()
