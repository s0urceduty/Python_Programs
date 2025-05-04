import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation, PillowWriter

# Set up the figure and 3D axis
fig = plt.figure(figsize=(19.2, 10.8), dpi=100)
ax = fig.add_subplot(111, projection='3d')

# Parameters for the fractal lines
num_points = 1000
t = np.linspace(0, 4 * np.pi, num_points)

# Base parametric 3D curve for the fractal
x = np.sin(t) * np.cos(t)
y = np.sin(t)
z = np.cos(t)

# Rotation and morphing parameters
angle_step = 360 / (10 * 30)  # 10 seconds at 30 FPS
morph_factor = np.linspace(1, 2, num_points)

# Create the plot
line, = ax.plot(x, y, z, lw=2)

def update(frame):
    # Apply rotation by changing the view angle
    ax.view_init(30, frame * angle_step)
    
    # Morphing the fractal by scaling the z-axis dynamically
    morph_z = z * morph_factor[frame % num_points]
    line.set_data(x, y)
    line.set_3d_properties(morph_z)
    return line,

# Set the animation
anim = FuncAnimation(fig, update, frames=300, interval=33, blit=False)

# Save the animation as a GIF
anim.save('3d_fractal_animation.gif', writer=PillowWriter(fps=30))
