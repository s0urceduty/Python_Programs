# Minimal_Calculator V1.0
# Copyright (C) 2024, Sourceduty - All Rights Reserved.

import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear():
    entry.delete(0, tk.END)

def insert_text(text):
    if text == 'E':
        root.destroy()  # Exit the program
    elif text == 'B':
        entry.delete(len(entry.get()) - 1, tk.END)  # Backspace functionality
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Calculator")

# Make the calculator transparent
root.attributes("-alpha", 0.9)

# Remove window borders
root.overrideredirect(True)

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the center position with even spacing around the edge padding
width, height = 300, 400
x = (screen_width - width) // 2
y = (screen_height - height) // 2

# Set the calculator position
root.geometry(f"{width}x{height}+{int(x)}+{int(y)}")

frame = tk.Frame(root, bg="#0074e4")  # Blue background
frame.pack(expand=True, padx=10, pady=10, fill=tk.BOTH)

entry = tk.Entry(frame, font=("Arial", 20), justify="right", bg="#0058b8", fg="white")  # Blue background, white text
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'E', 'B', '%'
]

row = 1
col = 0

last_calculation = ""

for button_text in buttons:
    tk.Button(
        frame,
        text=button_text,
        font=("Arial", 20),
        width=3,
        height=1,
        bg="#0074e4",  # Blue background
        fg="white",    # White text
        command=lambda text=button_text: insert_text(text) if text != '=' else calculate()
    ).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    col += 1
    if col > 3:
        col = 0
        row += 1

# Create a clear button
tk.Button(
    frame,
    text="C",
    font=("Arial", 20),
    width=3,
    height=1,
    bg="#ff4a4a",  # Red background for clear button
    fg="white",    # White text
    command=clear
).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Configure row and column weights for resizing
for i in range(6):
    frame.grid_rowconfigure(i, weight=1)
    frame.grid_columnconfigure(i, weight=1)

root.mainloop()
