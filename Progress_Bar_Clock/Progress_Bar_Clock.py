# Progress_Bar_Clock

# 🕒 Progress bar clock face.

# Copyright (C) 2023, Sourceduty - All Rights Reserved.
# THE CONTENTS OF THIS PROJECT ARE PROPRIETARY.

import tkinter as tk
from time import strftime, time
from math import radians, cos, sin

def update_time():
    current_time = time() % (24 * 60 * 60)
    string = strftime('%H:%M:%S %p')

    label.config(text=string)
    update_progress_bar(current_time)

    root.after(1000, update_time)

def update_progress_bar(current_time):
    percentage = (current_time / (24 * 60 * 60)) * 360
    draw_progress_bar(percentage)

def draw_progress_bar(percentage):
    canvas.delete("progress")
    x = canvas.winfo_reqwidth() / 2
    y = canvas.winfo_reqheight() / 2
    r = min(x, y) - 10
    start_angle = 90
    extent = percentage
    arc = canvas.create_arc(x - r, y - r, x + r, y + r, start=start_angle, extent=extent, style=tk.PIESLICE, fill="red", outline="red", tags="progress")
    canvas.create_oval(x - r - 5, y - r - 5, x + r + 5, y + r + 5, outline="black", width=2)
    label.place(x=x - label.winfo_reqwidth() / 2, y=y - label.winfo_reqheight() / 2)

root = tk.Tk()
root.title("Clock in a Circular Progress Bar")

canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.pack()

label = tk.Label(root, font=('calibri', 10, 'bold'), background='red', foreground='black')

update_time()

root.mainloop()

