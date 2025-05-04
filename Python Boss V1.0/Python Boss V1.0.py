# Python Boss V1.0
# GUI for Python and it's features.

import tkinter as tk
from tkinter import scrolledtext
import subprocess
import threading
import sys

# Global variable to keep track of the Python interactive shell process
python_process = None

# Function to execute Python commands and display output in the log area
def run_command(command):
    if python_process is None:
        try:
            log_text.config(state='normal')
            log_text.insert(tk.END, f"Running command: {command}\n")
            log_text.see(tk.END)
            log_text.config(state='disabled')
            
            result = subprocess.run([sys.executable, '-m', 'pip', 'install', command], capture_output=True, text=True, shell=True)
            
            log_text.config(state='normal')
            log_text.insert(tk.END, result.stdout.strip() + "\n")
            if result.stderr:
                log_text.insert(tk.END, f"Error: {result.stderr.strip()}\n")
            log_text.see(tk.END)
            log_text.config(state='disabled')
        except Exception as e:
            log_text.config(state='normal')
            log_text.insert(tk.END, f"Error: {str(e)}\n")
            log_text.see(tk.END)
            log_text.config(state='disabled')

# Function to display a comprehensive help menu
def display_help_menu():
    help_text = """
Python Library Installation Help Menu:

1. numpy
   - Description: Install numpy, a package for numerical computations.

2. pandas
   - Description: Install pandas, a library for data manipulation and analysis.

3. matplotlib
   - Description: Install matplotlib, a plotting library for creating visualizations.

4. scipy
   - Description: Install scipy, a library for scientific and technical computing.

5. scikit-learn
   - Description: Install scikit-learn, a library for machine learning.

6. requests
   - Description: Install requests, a library for HTTP requests.

7. flask
   - Description: Install flask, a micro web framework for building web applications.

8. django
   - Description: Install django, a high-level web framework for rapid development.

9. pillow
   - Description: Install pillow, a library for image processing.

10. seaborn
   - Description: Install seaborn, a library for statistical data visualization.

Click the respective button to install the library directly using pip.
    """
    log_text.config(state='normal')
    log_text.delete(1.0, tk.END)  # Clear the current log area
    log_text.insert(tk.END, help_text.strip())
    log_text.see(tk.END)
    log_text.config(state='disabled')

# Function to clear the text area
def clear_text_area():
    log_text.config(state='normal')
    log_text.delete(1.0, tk.END)
    log_text.config(state='disabled')

# Function to start the Python terminal
def start_terminal():
    global python_process
    if python_process is None:
        log_text.config(state='normal')
        log_text.delete(1.0, tk.END)
        log_text.insert(tk.END, "Python interactive terminal started. Enter commands below.\n")
        log_text.config(state='disabled')
        
        python_process = subprocess.Popen(
            [sys.executable, '-i'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            shell=True
        )
        threading.Thread(target=read_output, daemon=True).start()

# Function to read output from the Python interactive shell and display it in the text area
def read_output():
    global python_process
    while python_process:
        output = python_process.stdout.readline()
        if output:
            log_text.config(state='normal')
            log_text.insert(tk.END, output)
            log_text.see(tk.END)
            log_text.config(state='disabled')

# Function to send input to the Python terminal
def send_command(event):
    global python_process
    if python_process:
        command = entry.get()
        if command.strip() != "":
            python_process.stdin.write(command + "\n")
            python_process.stdin.flush()
            entry.delete(0, tk.END)

# List of common Python libraries (as buttons for quick installation)
python_libraries = [
    'numpy', 'pandas', 'matplotlib', 'scipy', 'scikit-learn',
    'requests', 'flask', 'django', 'pillow', 'seaborn'
]

# Create the main window
window = tk.Tk()
window.title("Python Boss V1.0")

# Apply dark mode theme
window.configure(bg='#2e2e2e')

# Frame for buttons (on the left side)
button_frame = tk.Frame(window, bg='#2e2e2e')
button_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.Y)

# Dynamically create buttons for each Python library
for library in python_libraries:
    button = tk.Button(button_frame, text=f"Install {library}", command=lambda l=library: run_command(l), bg='#3c3f41', fg='#ffffff', bd=0, relief='flat')
    button.pack(fill=tk.X, pady=5)

# Add a Help button that displays the help menu (styled in red)
help_button = tk.Button(button_frame, text="Help", command=display_help_menu, bg='#ff4040', fg='#ffffff', bd=0, relief='flat')
help_button.pack(fill=tk.X, pady=5)

# Add a Clear button to clear the text area (styled in blue)
clear_button = tk.Button(button_frame, text="Clear", command=clear_text_area, bg='#4040ff', fg='#ffffff', bd=0, relief='flat')
clear_button.pack(fill=tk.X, pady=5)

# Add a Start Terminal button (styled in red)
terminal_button = tk.Button(button_frame, text="Start Terminal", command=start_terminal, bg='#ff4040', fg='#ffffff', bd=0, relief='flat')
terminal_button.pack(fill=tk.X, pady=5)

# Log area for output and terminal (single text area)
log_text = scrolledtext.ScrolledText(window, width=80, height=20, wrap=tk.WORD, bg='#1e1e1e', fg='#00ff00', insertbackground='white', font=("Courier", 10))
log_text.pack(fill=tk.BOTH, padx=10, pady=10, expand=True)
log_text.tag_configure("left", lmargin1=0, lmargin2=0)
log_text.config(state='disabled')

# Entry box for typing commands in the terminal
entry = tk.Entry(window, bg='#1e1e1e', fg='#00ff00', insertbackground='white', font=("Courier", 10))
entry.pack(fill=tk.X, padx=10, pady=5)
entry.bind('<Return>', send_command)

# Start the GUI event loop
window.mainloop()
