# Earth Age Clock V1.0
# Copyright (C) 2024, Sourceduty - All Rights Reserved.

import tkinter as tk
from datetime import datetime

def calculate_earth_year():
    earth_start_year = 4540000000
    now = datetime.now()
    earth_year = now.year + (now - datetime(now.year, 1, 1)).days / 365.25 + earth_start_year
    return earth_year

def update_clock():
    earth_year = int(calculate_earth_year())
    current_time = datetime.now().strftime("%m-%d %H:%M:%S")
    combined_display.set(f"{earth_year}-{current_time}")
    root.after(1000, update_clock)

root = tk.Tk()
root.title("Earth Age Clock")
root.configure(bg="#121212")
font_color = "#FFFFFF"

combined_display = tk.StringVar()

display_label = tk.Label(
    root,
    textvariable=combined_display,
    font=("Helvetica", 16),
    fg=font_color,
    bg="#121212",
    justify="center"
)
display_label.pack(pady=(30, 15), padx=25)

description_label = tk.Label(
    root,
    text=(
        "This clock combines the Earth's age in years "
        "with the current time in the MM-DD HH:MM:SS format."
    ),
    font=("Helvetica", 12),
    fg=font_color,
    bg="#121212",
    wraplength=400,
    justify="center"
)
description_label.pack(pady=(15, 30), padx=25)

update_clock()
root.mainloop()
