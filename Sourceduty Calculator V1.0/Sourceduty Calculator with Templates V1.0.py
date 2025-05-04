# Sourceduty Calculator with Templates V1.0
# Copyright (C) 2024, Sourceduty - All Rights Reserved.

import tkinter as tk
from tkinter import Listbox, Scrollbar, Text, messagebox, OptionMenu, StringVar

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sourceduty Calculator with Templates")
        self.geometry("900x600")
        self.resizable(False, False)
        self.expression = ""
        
        self.create_widgets()
    
    def create_widgets(self):
        # Display for calculation
        self.display = tk.Entry(self, font=("Arial", 32), borderwidth=2, relief="solid", justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipadx=8, ipady=20)

        # Buttons layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
        ]
        
        for (text, row, col) in buttons:
            tk.Button(self, text=text, font=("Arial", 24), width=5, height=2, command=lambda t=text: self.on_button_click(t)).grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
        
        # Additional buttons
        tk.Button(self, text="C", font=("Arial", 24), width=11, height=2, command=self.clear_display).grid(row=5, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
        
        # Grid configuration for responsiveness
        for i in range(6):
            self.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
        
        # Template Manager Integration
        self.template_manager = TemplateManager(self)
        self.template_manager.create_template_widgets()

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

class TemplateManager:
    def __init__(self, parent):
        self.parent = parent
        self.templates = {
            "BMI Calculator": "weight / (height ** 2)",
            "Circle Area": "3.14 * (radius ** 2)",
            "Rectangle Area": "length * width",
            "Square Area": "side ** 2",
            "Cylinder Volume": "3.14 * (radius ** 2) * height",
            "Simple Interest": "(principal * rate * time) / 100",
            "Compound Interest": "principal * ((1 + rate / 100) ** time) - principal",
            "Distance (Speed-Time)": "speed * time",
            "Kinetic Energy": "0.5 * mass * (velocity ** 2)",
            "Potential Energy": "mass * gravity * height",
            "Ohm's Law": "voltage / resistance",
            "Power (P=VI)": "voltage * current",
            "Quadratic Formula": "(-b + (b**2 - 4*a*c)**0.5) / (2*a)",
            "Pythagorean Theorem": "(a**2 + b**2) ** 0.5",
            "Future Value of Investment": "principal * ((1 + rate / 100) ** time)"
        }
        self.selected_template = tk.StringVar(self.parent)
    
    def create_template_widgets(self):
        # Template selection Drop-down menu
        self.template_frame = tk.Frame(self.parent)
        self.template_frame.grid(row=0, column=4, rowspan=6, padx=20, pady=20, sticky="nswe")

        tk.Label(self.template_frame, text="Templates", font=("Arial", 18)).pack(anchor='w')
        
        self.selected_template.set("Select Template")
        template_menu = OptionMenu(self.template_frame, self.selected_template, *self.templates.keys(), command=self.on_template_select)
        template_menu.config(font=("Arial", 18), width=20)
        template_menu.pack(anchor='w', padx=10, pady=10)

        # Notepad and Entry for Templates
        self.notepad = Text(self.template_frame, font=("Arial", 14), height=15, width=35, wrap="word", bg="white", fg="black", borderwidth=2, relief="solid")
        self.notepad.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.entry_bar = tk.Entry(self.template_frame, font=("Arial", 18), borderwidth=2, relief="solid")
        self.entry_bar.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Button(self.template_frame, text="Enter", font=("Arial", 18), command=self.calculate_template).pack(pady=10)

    def on_template_select(self, selected_template):
        if selected_template:
            template_expression = self.templates[selected_template]
            self.display_template(template_expression)
    
    def display_template(self, expression):
        self.notepad.delete(1.0, tk.END)
        self.notepad.insert(tk.END, f"Template: {expression}\n")
        self.entry_bar.delete(0, tk.END)
        self.entry_bar.insert(0, "Enter values with commas (e.g., 70, 1.75)")

    def calculate_template(self):
        selected_template = self.selected_template.get()
        if selected_template and selected_template != "Select Template":
            template_expression = self.templates[selected_template]
            try:
                input_values = list(map(float, self.entry_bar.get().split(',')))
                variable_names = [var for var in template_expression.split() if var.isidentifier()]
                if len(variable_names) == len(input_values):
                    local_vars = dict(zip(variable_names, input_values))
                    result = eval(template_expression, {}, local_vars)
                    messagebox.showinfo("Result", f"Result: {result}")
                else:
                    messagebox.showerror("Error", "The number of input values does not match the template variables.")
            except Exception as e:
                messagebox.showerror("Error", f"Error in calculation: {e}")
        else:
            messagebox.showerror("Error", "Please select a template.")

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
