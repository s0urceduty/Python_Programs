# Sourceduty Calculator with Simulated Templates V1.1
# Copyright (C) 2024, Sourceduty - All Rights Reserved.

import tkinter as tk
from tkinter import Menu, Text, messagebox
import random
import math  # Import math module for mathematical operations

class SourcedutyCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sourceduty Calculator")
        self.geometry("900x500")
        self.resizable(False, False)
        self.expression = ""
        
        self.create_widgets()
    
    def create_widgets(self):
        # Display for calculation
        self.display = tk.Entry(self, font=("Arial", 28), borderwidth=2, relief="solid", justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipadx=8, ipady=15)

        # Buttons layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
        ]
        
        for (text, row, col) in buttons:
            tk.Button(self, text=text, font=("Arial", 20), width=5, height=2, command=lambda t=text: self.on_button_click(t)).grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
        
        # Additional buttons
        tk.Button(self, text="C", font=("Arial", 20), width=11, height=2, command=self.clear_display).grid(row=5, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
        
        # Simulation button
        tk.Button(self, text="Simulate", font=("Arial", 20), width=11, height=2, command=self.run_simulation).grid(row=5, column=2, columnspan=2, sticky="nsew", padx=5, pady=5)
        
        # Grid configuration for responsiveness
        for i in range(6):
            self.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
        
        # Menu Integration
        self.create_menu()

        # Template Manager Integration
        self.template_manager = TemplateManager(self)
        self.template_manager.create_template_widgets()

    def create_menu(self):
        # Create the main menu
        menu_bar = Menu(self)

        # Basic Templates Menu
        basic_templates_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Templates", menu=basic_templates_menu)
        basic_templates_menu.add_command(label="Addition", command=lambda: self.template_manager.on_template_select("Addition"))
        basic_templates_menu.add_command(label="Subtraction", command=lambda: self.template_manager.on_template_select("Subtraction"))
        basic_templates_menu.add_command(label="Multiplication", command=lambda: self.template_manager.on_template_select("Multiplication"))
        basic_templates_menu.add_command(label="Division", command=lambda: self.template_manager.on_template_select("Division"))
        basic_templates_menu.add_command(label="Square", command=lambda: self.template_manager.on_template_select("Square"))
        basic_templates_menu.add_command(label="Square Root", command=lambda: self.template_manager.on_template_select("Square Root"))
        basic_templates_menu.add_command(label="Exponential", command=lambda: self.template_manager.on_template_select("Exponential"))
        basic_templates_menu.add_command(label="Logarithm", command=lambda: self.template_manager.on_template_select("Logarithm"))

        # Attach the menu to the window
        self.config(menu=menu_bar)

    def on_button_click(self, text):
        if text == "=":
            try:
                self.expression = str(eval(self.expression))
                self.update_display()
            except Exception as e:
                self.display.insert(tk.END, " Error")
                self.expression = ""
        else:
            self.expression += text
            self.update_display()
    
    def clear_display(self):
        self.expression = ""
        self.update_display()
    
    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

    def run_simulation(self):
        selected_template = self.template_manager.selected_template.get()
        if selected_template:
            try:
                # Generate random example numbers based on the selected template type
                example_values = {
                    "Addition": [random.uniform(1, 100), random.uniform(1, 100)],
                    "Subtraction": [random.uniform(1, 100), random.uniform(1, 100)],
                    "Multiplication": [random.uniform(1, 10), random.uniform(1, 10)],
                    "Division": [random.uniform(1, 100), random.uniform(1, 10)],
                    "Square": [random.uniform(1, 20)],
                    "Square Root": [random.uniform(1, 100)],
                    "Exponential": [random.uniform(1, 5)],
                    "Logarithm": [random.uniform(1, 100)],
                }

                # Get example values for the currently selected template
                input_values = example_values.get(selected_template, [])

                # Construct the expression from the template
                template_expression = self.template_manager.templates[selected_template].format(*input_values)

                # Display the selected template and formula
                self.template_manager.notepad.insert(tk.END, f"Template Selected: {selected_template}\n")
                self.template_manager.notepad.insert(tk.END, f"Formula: {self.template_manager.templates[selected_template]}\n")

                # Evaluate the expression and display the result in the text box
                result = eval(template_expression)
                simulation_text = f"Values: {input_values}\nResult: {result}\n"
                self.template_manager.notepad.insert(tk.END, simulation_text)
            except Exception as e:
                # Handle any errors gracefully and display them in the text box
                simulation_text = f"Simulation could not be performed. Error: {e}\n"
                self.template_manager.notepad.insert(tk.END, simulation_text)
        else:
            self.template_manager.notepad.delete(1.0, tk.END)
            self.template_manager.notepad.insert(tk.END, "No template selected for simulation.\n")

class TemplateManager:
    def __init__(self, parent):
        self.parent = parent
        self.templates = {
            "Addition": "{} + {}",
            "Subtraction": "{} - {}",
            "Multiplication": "{} * {}",
            "Division": "{} / {}",
            "Square": "{} ** 2",
            "Square Root": "math.sqrt({})",
            "Exponential": "math.exp({})",
            "Logarithm": "math.log({})",
        }
        self.selected_template = tk.StringVar(self.parent)
    
    def create_template_widgets(self):
        # Template selection Drop-down menu
        self.template_frame = tk.Frame(self.parent)
        self.template_frame.grid(row=0, column=4, rowspan=6, padx=20, pady=20, sticky="nswe")

        # Notepad for Templates (Black background and white text)
        self.notepad = Text(self.template_frame, font=("Arial", 14), height=15, width=35, wrap="word", bg="black", fg="white", borderwidth=2, relief="solid")
        self.notepad.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    def on_template_select(self, selected_template):
        if selected_template:
            self.selected_template.set(selected_template)
            self.notepad.delete(1.0, tk.END)
            self.notepad.insert(tk.END, f"Template Selected: {selected_template}\n")
            self.notepad.insert(tk.END, f"Formula: {self.templates[selected_template]}\n")

if __name__ == "__main__":
    app = SourcedutyCalculator()
    app.mainloop()
