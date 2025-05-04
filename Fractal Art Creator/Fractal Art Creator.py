# Fractal Art Generator
# Copyright (C) 2024, Sourceduty - All Rights Reserved.

import tkinter as tk
from tkinter import filedialog, ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

class FractalArtApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fractal Art Creator")
        self.root.geometry("800x400")
        self.root.resizable(False, False) 

        self.create_widgets()
        self.figure_canvas = None
        self.fig = None
        self.ax = None

    def create_widgets(self):
        self.canvas_frame = tk.Frame(self.root, width=800, height=250)
        self.canvas_frame.pack(fill=tk.BOTH, expand=1)

        self.control_frame_bottom = tk.Frame(self.root)
        self.control_frame_bottom.pack(fill=tk.X, side=tk.BOTTOM, pady=10)

        self.iterations_label = tk.Label(self.control_frame_bottom, text="Sections:")
        self.iterations_label.grid(row=0, column=0, padx=5)
        self.iterations_entry = tk.Entry(self.control_frame_bottom)
        self.iterations_entry.grid(row=0, column=1, padx=5)
        self.iterations_entry.insert(0, "3")

        self.color_label = tk.Label(self.control_frame_bottom, text="Color:")
        self.color_label.grid(row=0, column=2, padx=5)
        
        self.color_options = ["hsv", "inferno", "plasma", "viridis", "cividis", "jet", "rainbow"]
        self.color_combobox = ttk.Combobox(self.control_frame_bottom, values=self.color_options)
        self.color_combobox.grid(row=0, column=3, padx=5)
        self.color_combobox.set("hsv")

        self.real_label = tk.Label(self.control_frame_bottom, text="X Axis:")
        self.real_label.grid(row=1, column=0, padx=5)
        self.real_entry = tk.Entry(self.control_frame_bottom)
        self.real_entry.grid(row=1, column=1, padx=5)
        self.real_entry.insert(0, "0.0")

        self.imag_label = tk.Label(self.control_frame_bottom, text="Y Axis:")
        self.imag_label.grid(row=1, column=2, padx=5)
        self.imag_entry = tk.Entry(self.control_frame_bottom)
        self.imag_entry.grid(row=1, column=3, padx=5)
        self.imag_entry.insert(0, "0.0")

        self.zoom_label = tk.Label(self.control_frame_bottom, text="Zoom:")
        self.zoom_label.grid(row=1, column=4, padx=5)
        self.zoom_entry = tk.Entry(self.control_frame_bottom)
        self.zoom_entry.grid(row=1, column=5, padx=5)
        self.zoom_entry.insert(0, "1.0")

        self.create_button = tk.Button(self.control_frame_bottom, text="Create Art", command=self.create_art)
        self.create_button.grid(row=2, column=0, columnspan=2, pady=5)

        self.save_button = tk.Button(self.control_frame_bottom, text="Save Art", command=self.save_art)
        self.save_button.grid(row=2, column=2, columnspan=2, pady=5)

        self.lines_button = tk.Button(self.control_frame_bottom, text="Add Random Lines", command=self.add_random_lines)
        self.lines_button.grid(row=2, column=4, columnspan=2, pady=5)

    def create_art(self):
        iterations = int(self.iterations_entry.get())
        colormap = self.color_combobox.get()
        real = float(self.real_entry.get())
        imag = float(self.imag_entry.get())
        zoom = float(self.zoom_entry.get())
        self.plot_fractal(iterations, colormap, real, imag, zoom)

    def plot_fractal(self, iterations, colormap, real, imag, zoom):
        if self.figure_canvas:
            self.figure_canvas.get_tk_widget().destroy()

        self.fig, self.ax = plt.subplots(figsize=(8, 3), dpi=100)  
        x = np.linspace(-2 / zoom + real, 2 / zoom + real, 800)
        y = np.linspace(-1.125 / zoom + imag, 1.125 / zoom + imag, 300)
        X, Y = np.meshgrid(x, y)
        Z = X + 1j * Y
        C = np.zeros(Z.shape, dtype=complex)
        threshold = 1000

        for i in range(iterations):
            Z = Z**2 + C
            mask = np.abs(Z) > threshold
            Z[mask] = threshold  

        self.ax.imshow(np.angle(Z), extent=(x.min(), x.max(), y.min(), y.max()), cmap=colormap)
        self.ax.axis('off')

        self.figure_canvas = FigureCanvasTkAgg(self.fig, master=self.canvas_frame)
        self.figure_canvas.draw()
        self.figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def add_random_lines(self):
        if self.fig and self.ax:
            for _ in range(10):  # Add 10 random lines
                x_start, x_end = np.random.uniform(-2, 2), np.random.uniform(-2, 2)
                y_start, y_end = np.random.uniform(-1.125, 1.125), np.random.uniform(-1.125, 1.125)
                self.ax.plot([x_start, x_end], [y_start, y_end], color=np.random.rand(3,))
            self.figure_canvas.draw()

    def save_art(self):
        iterations = int(self.iterations_entry.get())
        colormap = self.color_combobox.get()
        real = float(self.real_entry.get())
        imag = float(self.imag_entry.get())
        zoom = float(self.zoom_entry.get())

        if self.figure_canvas:
            file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                     filetypes=[("PNG files", "*.png"),
                                                                ("All files", "*.*")])
            if file_path:
                fig, ax = plt.subplots(figsize=(38.4, 21.6), dpi=100)
                x = np.linspace(-2 / zoom + real, 2 / zoom + real, 3840)
                y = np.linspace(-1.125 / zoom + imag, 1.125 / zoom + imag, 2160)
                X, Y = np.meshgrid(x, y)
                Z = X + 1j * Y
                C = np.zeros(Z.shape, dtype=complex)
                threshold = 1000

                for i in range(iterations):
                    Z = Z**2 + C
                    mask = np.abs(Z) > threshold
                    Z[mask] = threshold  

                ax.imshow(np.angle(Z), extent=(x.min(), x.max(), y.min(), y.max()), cmap=colormap)
                ax.axis('off')

                if self.ax:
                    for line in self.ax.lines:
                        ax.plot(line.get_xdata(), line.get_ydata(), color=line.get_color())

                fig.savefig(file_path, bbox_inches='tight', pad_inches=0)

if __name__ == "__main__":
    root = tk.Tk()
    app = FractalArtApp(root)
    root.mainloop()