# Utility_Station V1.3
# Concept desktop interface design for tools and utilities.
# Copyright (C) 2024, Sourceduty - All Rights Reserved.

import tkinter as tk
from tkinter import ttk
from tkinter import Text, Scrollbar
from tkinter import filedialog

# Function to center a window on the screen
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

# Function to clear the notepad text
def clear_notepad():
    notepad_text.delete(1.0, tk.END)

# Function to calculate the result in the calculator
def calculate():
    try:
        expression = calculator_input_text.get(1.0, tk.END)
        result = eval(expression)
        calculator_output_text.delete(1.0, tk.END)
        calculator_output_text.insert(tk.END, f"= {result}")
    except Exception as e:
        calculator_output_text.delete(1.0, tk.END)
        calculator_output_text.insert(tk.END, "Error")

# Function to clear the calculator input and output
def clear_calculator():
    calculator_input_text.delete(1.0, tk.END)
    calculator_output_text.delete(1.0, tk.END)

# Function to save the notepad content to a file
def save_notepad():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(notepad_text.get(1.0, tk.END))

# Function to close the main window
def close_window():
    root.destroy()

# Create the main window
root = tk.Tk()
root.overrideredirect(True)
root.attributes("-alpha", 0.75)
root.configure(bg="black")
root.title("Transparent Notepad and Calculator")

width = int(1920 * 0.75)
height = int(1080 * 0.75)

center_window(root, width, height)

# Create Calculator Frame
calculator_frame = ttk.Frame(root, width=width // 2, height=height, style="Black.TFrame")
calculator_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

calculator_input_text = Text(calculator_frame, height=3, wrap=tk.WORD)
calculator_input_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=(10, 0))

# Create Calculator Buttons
calculator_buttons = ttk.Frame(calculator_frame)
calculator_buttons.pack(pady=10)

calculator_output_text = Text(calculator_frame, height=1, wrap=tk.WORD)
calculator_output_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))

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
            ttk.Button(calculator_buttons, text=button_text, width=15, command=calculate, style="ModernButton.TButton").grid(row=i, column=j, padx=0, pady=0)
        else:
            ttk.Button(calculator_buttons, text=button_text, width=15, command=lambda text=button_text: calculator_input_text.insert(tk.END, text), style="ModernButton.TButton").grid(row=i, column=j, padx=0, pady=0)

# Create Notepad Frame
notepad_frame = ttk.Frame(root, width=width // 2, height=height, style="Black.TFrame")
notepad_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.BOTH, expand=True)

keyboard_frame = ttk.Frame(notepad_frame)
keyboard_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

keyboard_shortcuts =  """
Windows 10 and Windows 11 Shortcuts

General:
- Win+L: Lock your PC
- Alt+Tab: Switch between open apps
- Win+D: Show or hide the desktop
- Win+P: Choose a presentation display mode
- Win+X: Open the power user menu

Taskbar:
- Win+number (1-9): Open apps pinned to the taskbar
- Win+T: Cycle through apps on the taskbar
- Win+B: Set focus in the notification area
- Shift+click on a taskbar app: Open a new instance

Virtual Desktops (Windows 10 and 11):
- Win+Ctrl+D: Create a new virtual desktop
- Win+Ctrl+Right/Left: Switch between virtual desktops
- Win+Ctrl+F4: Close the current virtual desktop

Snap:
- Win+Left/Right Arrow: Snap current window to the left/right
- Win+Up Arrow: Maximize the current window
- Win+Down Arrow: Restore or minimize the current window

Cortana/Search:
- Win+C: Activate Cortana
- Win+S: Open Cortana's search bar
- Win+Q: Open app-specific search
- Win+W: Open Windows Ink Workspace

Task View:
- Win+Tab: Open Task View
- Win+Ctrl+D: Create a new virtual desktop
- Win+Ctrl+F4: Close the current virtual desktop

System:
- Win+I: Open Settings
- Win+P: Choose a presentation display mode
- Win+L: Lock your PC
- Win+X: Open the power user menu
- Win+K: Open the Connect quick action

File Explorer:
- Win+E: Open File Explorer
- Alt+D: Select the address bar
- Ctrl+N: Open a new File Explorer window
- Ctrl+W: Close the current File Explorer window

Command Prompt and PowerShell:
- Ctrl+C: Copy selected text
- Ctrl+V: Paste text from the clipboard
- Ctrl+A: Select all text
- Ctrl+Shift+Arrow: Select text by words
- Shift+Arrow: Extend selection by one character

"""

notepad_keyboard_shortcuts = Text(keyboard_frame, wrap=tk.WORD, height=20, foreground="black")
notepad_keyboard_shortcuts.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

notepad_keyboard_shortcuts.insert(tk.END, keyboard_shortcuts)

scrollbar = Scrollbar(keyboard_frame, command=notepad_keyboard_shortcuts.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
notepad_keyboard_shortcuts.config(yscrollcommand=scrollbar.set)

notepad_text = Text(notepad_frame, wrap=tk.WORD, height=1)
notepad_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

notepad_buttons = ttk.Frame(notepad_frame)
notepad_buttons.pack(pady=10)

notepad_button_grid = [
    ['Save', 'Clear']
]

for i in range(1):
    for j in range(2):
        button_text = notepad_button_grid[i][j]
        ttk.Button(notepad_buttons, text=button_text, width=10, command=lambda text=button_text: handle_notepad_button(text), style="ModernButton.TButton").pack(side=tk.LEFT)

# Create Close Button
close_button = ttk.Button(root, text="x", width=2, command=close_window, style="ModernButton.TButton")
close_button.place(x=width-35, y=height-35)

# Handle Notepad Buttons
def handle_notepad_button(button_text):
    if button_text == 'Save':
        save_notepad()
    elif button_text == 'Clear':
        clear_notepad()
        clear_calculator()

# Define Styles
style = ttk.Style()
style.configure("Black.TFrame", background="black")
style.configure("Grey.TFrame", background="grey")
style.configure("Black.TLabel", background="black", foreground="grey", font=("Helvetica", 16, "bold"))
style.configure("Grey.TLabel", background="grey", foreground="black", font=("Helvetica", 16, "bold"))
style.configure("ModernButton.TButton", relief="flat", foreground="black", borderwidth=0, padx=5, pady=5, highlightbackground="black", highlightcolor="black")
style.configure("Borderless.TButton", relief="flat", foreground="black", padx=5, pady=5)
style.configure("ModernButton.TButton", relief="flat", background="black", foreground="black", font=("Helvetica", 12, "bold"), padx=5, pady=5)

# Start the Tkinter main loop
root.mainloop()
