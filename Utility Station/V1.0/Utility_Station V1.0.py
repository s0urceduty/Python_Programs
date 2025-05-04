# Utility_Station V1.0
# Concept desktop interface design for tools and utilities.
# Copyright (C) 2024, Sourceduty - All Rights Reserved.

import tkinter as tk
from tkinter import ttk
from tkinter import Text, Scrollbar
from tkinter import filedialog

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

def clear_notepad():
    notepad_text.delete(1.0, tk.END)

def calculate():
    try:
        expression = calculator_input_text.get(1.0, tk.END)
        result = eval(expression)
        calculator_output_text.delete(1.0, tk.END)
        calculator_output_text.insert(tk.END, f"= {result}")
    except Exception as e:
        calculator_output_text.delete(1.0, tk.END)
        calculator_output_text.insert(tk.END, "Error")

def clear_calculator():
    calculator_input_text.delete(1.0, tk.END)
    calculator_output_text.delete(1.0, tk.END)

def save_notepad():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(notepad_text.get(1.0, tk.END))

def close_window():
    root.destroy()

root = tk.Tk()
root.overrideredirect(True)  # Remove window decorations (border)
root.attributes("-alpha", 0.75)  # Set transparency to 75%
root.configure(bg="grey")  # Set background color to grey
root.title("Transparent Notepad and Calculator")

# Set the desired window size (75% smaller than 1920x1080)
width = int(1920 * 0.75)
height = int(1080 * 0.75)

center_window(root, width, height)

# Create Calculator
calculator_frame = ttk.Frame(root, width=width // 2, height=height, style="Black.TFrame")
calculator_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

calculator_input_text = Text(calculator_frame, height=3, wrap=tk.WORD)
calculator_input_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

calculator_buttons = ttk.Frame(calculator_frame)
calculator_buttons.pack(pady=10)

calculator_output_text = Text(calculator_frame, height=1, wrap=tk.WORD)
calculator_output_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

button_grid = [
    ['7', '8', '9', '+'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '*'],
    ['0', '.', '=', '/']
]

for i in range(4):
    for j in range(4):
        button_text = button_grid[i][j]
        if button_text == '=':
            ttk.Button(calculator_buttons, text=button_text, width=10, command=calculate).grid(row=i, column=j, padx=5, pady=5)
        else:
            ttk.Button(calculator_buttons, text=button_text, width=10, command=lambda text=button_text: calculator_input_text.insert(tk.END, text)).grid(row=i, column=j, padx=5, pady=5)

# Create Notepad
notepad_frame = ttk.Frame(root, width=width // 2, height=height, style="Grey.TFrame")
notepad_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.BOTH, expand=True)

notepad_text = Text(notepad_frame, wrap=tk.WORD)
notepad_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

notepad_buttons = ttk.Frame(notepad_frame)
notepad_buttons.pack(pady=10)

notepad_button_grid = [
    ['Open', 'Save', 'Clear']
]

for i in range(1):
    for j in range(3):
        button_text = notepad_button_grid[i][j]
        ttk.Button(notepad_buttons, text=button_text, width=10, command=lambda text=button_text: handle_notepad_button(text)).pack(side=tk.LEFT, padx=5, pady=5)

# Close Button (minimal 'x' button with spacing)
close_button = ttk.Button(root, text="x", width=2, command=close_window, style="Minimal.TButton")
close_button.place(x=width-35, y=height-35)  # Placed at the bottom right corner with spacing

def handle_notepad_button(button_text):
    if button_text == 'Open':
        # Implement the Open functionality here
        pass
    elif button_text == 'Save':
        save_notepad()  # Save the notepad content
    elif button_text == 'Clear':
        clear_notepad()  # Clear the notepad only

# Configure Styles
style = ttk.Style()
style.configure("Black.TFrame", background="black")
style.configure("Grey.TFrame", background="grey")
style.configure("Black.TLabel", background="black", foreground="grey", font=("Helvetica", 16, "bold"))
style.configure("Grey.TLabel", background="grey", foreground="black", font=("Helvetica", 16, "bold"))
style.configure("Minimal.TButton", relief="flat")  # Set relief to flat for a minimal button appearance

root.mainloop()
