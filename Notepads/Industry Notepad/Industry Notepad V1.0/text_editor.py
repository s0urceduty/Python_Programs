# Industry Notepad V1.0
# Copyright (C) 2024, Sourceduty 

import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox
from templates import TEMPLATES

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Industry Notepad V1.0")
        self.create_menu()
        self.create_widgets()
        self.mode = "light"

    def create_menu(self):
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)

        # File Menu
        file_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As...", command=self.save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit)

        # Industries Menu
        industries_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Industries", menu=industries_menu)
        for industry, templates in TEMPLATES.items():
            industry_menu = tk.Menu(industries_menu, tearoff=0)
            industries_menu.add_cascade(label=industry, menu=industry_menu)
            for template_name in templates:
                industry_menu.add_command(label=template_name, command=lambda name=template_name: self.load_template(name))

        # Mode Menu
        mode_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Mode", menu=mode_menu)
        mode_menu.add_command(label="Dark Mode", command=self.dark_mode)        
        mode_menu.add_command(label="Light Mode", command=self.light_mode)

        # Options Menu
        options_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Control", menu=options_menu)
        options_menu.add_command(label="About", command=self.show_options)

    def create_widgets(self):
        self.text_area = tk.Text(self.root, wrap="word", undo=True)
        self.text_area.pack(expand=1, fill='both')

        # Default description
        default_description = (
            "Industry Notepad V1.0\n"
            "Copyright (C) 2024, Sourceduty\n\n"
            "This notepad was developed for text editing and template management in business industries.\n\n"
            "Features: \n"
            "- Light and Dark Mode: Switch between light and dark themes.\n"
            "- Template Loading: Easily load predefined templates for different industries.\n"
            "- Undo/Redo: Support for undoing and redoing changes.\n"
            "- File Operations: Create, open, save, and save files as different formats.\n"
            "- Options and About: Access options and learn more about the application.\n"
            "\n\nRepository: https://github.com/sourceduty/Industry_Notepad"
        )
        self.text_area.insert(tk.END, default_description)
        self.set_dark_mode()

    def load_template(self, template_name):
        template_content = self.get_template_content(template_name)
        if template_content:
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, template_content)

    def get_template_content(self, template_name):
        for templates in TEMPLATES.values():
            if template_name in templates:
                return templates[template_name]
        return None

    def set_light_mode(self):
        self.text_area.config(bg="white", fg="black", insertbackground="black")
        self.mode = "light"

    def set_dark_mode(self):
        self.text_area.config(bg="black", fg="white", insertbackground="white")
        self.mode = "dark"

    def light_mode(self):
        self.set_light_mode()

    def dark_mode(self):
        self.set_dark_mode()

    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.mode = "new"

    def open_file(self):
        filepath = askopenfilename()
        if not filepath:
            return
        with open(filepath, "r") as file:
            content = file.read()
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, content)
        self.mode = "open"

    def save_file(self):
        if self.mode == "new":
            self.save_as_file()
        else:
            filepath = asksaveasfilename(defaultextension="txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
            if not filepath:
                return
            with open(filepath, "w") as file:
                content = self.text_area.get(1.0, tk.END)
                file.write(content)

    def save_as_file(self):
        filepath = asksaveasfilename(defaultextension="txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if not filepath:
            return
        with open(filepath, "w") as file:
            content = self.text_area.get(1.0, tk.END)
            file.write(content)

    def exit(self):
        self.root.quit()

    def show_options(self):
        messagebox.showinfo("About", "Copyright (C) 2024, Sourceduty ")

    def undo(self):
        try:
            self.text_area.edit_undo()
        except:
            pass

    def redo(self):
        try:
            self.text_area.edit_redo()
        except:
            pass
