# Sourceduty Notepad V4.5
# Copyright (C) 2024, Sourceduty

# pip install markdown python-docx pymupdf pandas
# pip install googletrans==4.0.0-rc1

import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import simpledialog, messagebox
from tkinter import scrolledtext
import time
import os
import markdown
from docx import Document
import csv
import fitz
import pandas as pd
import json
import html
import difflib
import random
import string

TEMPLATES = {
    "Business": {
        "Meeting Notes": "Meeting Notes\nDate: \nAttendees: \nAgenda:\n- \n- \n\nDiscussion:\n- \n- \n\nAction Items:\n- \n- \n\nNext Meeting: ",
        "Project Plan": "Project Plan\nProject Name: \nStart Date: \nEnd Date: \nProject Manager: \n\nGoals:\n- \n- \n\nMilestones:\n- \n- \n\nResources:\n- \n- \n\nRisks:\n- \n- \n\nDeliverables:\n- \n- ",
        "Schedule": "Schedule\nDate: \n\nTasks:\n1. \n2. \n3. \n\nNotes:\n- \n- \n",
        "Routine": "Daily Routine\nDate: \n\nMorning:\n- \n- \n\nAfternoon:\n- \n- \n\nEvening:\n- \n- \n\nNotes:\n- \n- \n",
        "Copyright": "# Copyright (C) 20--, YourName\n\n[Add your content here]\n",
        "Process": "Process Template\nTitle: \n\nObjective:\n\nSteps:\n1. \n2. \n3. \n\nOutcome:\n\nNotes:\n- \n- \n",
        "Business Process": "Business Process\nTitle: \n\nObjective: \n\nSteps:\n1. Step 1 Description\n2. Step 2 Description\n3. Step 3 Description\n\nResources: \n- Resource 1\n- Resource 2\n\nOutcome: \n\n"
    },
    "Education": {
        "Lecture Notes": "Lecture Notes\nDate: \nInstructor: \nCourse: \n\nKey Points:\n- \n- \n\nSummary:\n\nQuestions:\n- \n- ",
        "Essay Outline": "Essay Outline\nTitle: \nThesis Statement: \n\nIntroduction:\n\nBody Paragraphs:\n1. \n2. \n3. \n\nConclusion: ",
        "Schedule": "Schedule\nDate: \n\nTasks:\n1. \n2. \n3. \n\nNotes:\n- \n- \n",
        "Routine": "Daily Routine\nDate: \n\nMorning:\n- \n- \n\nAfternoon:\n- \n- \n\nEvening:\n- \n- \n\nNotes:\n- \n- \n",
        "Copyright": "# Copyright (C) 20--, YourName\n\n[Add your content here]\n",
        "Process": "Process Template\nTitle: \n\nObjective:\n\nSteps:\n1. \n2. \n3. \n\nOutcome:\n\nNotes:\n- \n- \n"
    },
    "Creative Writing": {
        "Story Outline": "Story Outline\nTitle: \nGenre: \n\nCharacters:\n1. \n2. \n3. \n\nPlot Overview:\n\nChapter Breakdown:\n1. \n2. \n3. ",
        "Poem Template": "Poem Template\nTitle: \n\n[Write your poem here]\n\n\nReflection:\n\n",
        "Schedule": "Schedule\nDate: \n\nTasks:\n1. \n2. \n3. \n\nNotes:\n- \n- \n",
        "Routine": "Daily Routine\nDate: \n\nMorning:\n- \n- \n\nAfternoon:\n- \n- \n\nEvening:\n- \n- \n\nNotes:\n- \n- \n",
        "Copyright": "# Copyright (C) 20--, YourName\n\n[Add your content here]\n",
        "Process": "Process Template\nTitle: \n\nObjective:\n\nSteps:\n1. \n2. \n3. \n\nOutcome:\n\nNotes:\n- \n- \n"
    },
    "Custom Templates": {}
}

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Sourceduty Notepad V4.5")
        self.start_time = time.time()
        self.create_menu()
        self.create_widgets()
        self.set_default_description()
        self.update_footer()

    def create_menu(self):
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)

        file_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Open and Merge", command=self.open_and_merge)
        file_menu.add_command(label="Compare Files", command=self.compare_files)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As...", command=self.save_as_file)
        file_menu.add_command(label="Export", command=self.export_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit)

        templates_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Templates", menu=templates_menu)
        for industry, templates in TEMPLATES.items():
            industry_menu = tk.Menu(templates_menu, tearoff=0)
            templates_menu.add_cascade(label=industry, menu=industry_menu)
            for template_name in templates:
                industry_menu.add_command(label=template_name, command=lambda name=template_name, industry=industry: self.load_template(industry, name))
            if industry == "Custom Templates":
                industry_menu.add_separator()
                industry_menu.add_command(label="Delete Template", command=self.delete_custom_template)

        custom_template_menu = tk.Menu(templates_menu, tearoff=0)
        templates_menu.add_cascade(label="Add Custom Template", menu=custom_template_menu)
        custom_template_menu.add_command(label="Add Template", command=self.add_custom_template)

        mode_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Mode", menu=mode_menu)
        mode_menu.add_command(label="Dark Mode", command=self.dark_mode)        
        mode_menu.add_command(label="Light Mode", command=self.light_mode)

        control_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Control", menu=control_menu)
        control_menu.add_command(label="About", command=self.show_options)
        control_menu.add_command(label="Text Statistics", command=self.show_statistics)
        control_menu.add_command(label="Generate Password", command=self.generate_password)
        control_menu.add_command(label="Sort/Filter and Export List", command=self.export_list)
        control_menu.add_command(label="Translate to English", command=self.translate_to_english)

    def create_widgets(self):
        self.text = tk.Text(self.root, wrap="word")
        self.text.pack(expand=1, fill="both")

        self.footer_frame = tk.Frame(self.root, bg="black")
        self.footer_frame.pack(side="bottom", fill="x")

        self.dynamic_footer = tk.Label(self.footer_frame, text="", anchor="w", bg="black", fg="white")
        self.dynamic_footer.pack(side="left", padx=10)

        self.timestamp_button = tk.Button(self.footer_frame, text="Insert Timestamp", command=self.insert_timestamp, bg="black", fg="white")
        self.timestamp_button.pack(side="right", padx=0)

        self.toolbar = tk.Frame(self.root, bg="black")
        self.toolbar.pack(side="top", fill="x")

    def set_default_description(self):
        default_description = (
            "Sourceduty Notepad V4.5\n"
            "Copyright (C) 2024, Sourceduty\n\n"
            "Welcome to Sourceduty Notepad V4.5, your versatile text editor designed for various industry needs.\n\n"
            "Features:\n\n"
            "- Templates: Easily access and use pre-defined templates for various industries, including Business, Education, and Creative Writing.\n"
            "- Text Editing: Edit and format text with various options.\n"
            "- Text Statistics: Analyze word count, character count, and paragraph count.\n"
            "- Password Generator: Generate secure passwords with customizable length.\n"
            "- List Exporter: Sort and filter lists before exporting them to a text file.\n"
            "- Translation: Translate text to English (mock feature, replace with actual translation logic).\n"
            "- Insert Timestamp: Quickly insert a timestamp into your text.\n"
            "- File Operations: Open, save, and merge files of various formats including text, Word documents, CSV, PDF, HTML, and JSON.\n"
            "- File Comparison: Compare two text files and view differences.\n"
            "- Custom Templates: Add, manage, and delete custom templates for your specific needs.\n"
            "- Modes: Switch between Dark Mode and Light Mode for comfortable reading and editing.\n"
            "- About: View application information.\n\n"
            "\n\nRepository: https://github.com/sourceduty/Notepad"
        )
        self.text.insert(tk.END, default_description)

    def update_footer(self):
        elapsed_time = time.time() - self.start_time
        minutes = int(elapsed_time / 60)
        seconds = int(elapsed_time % 60)
        self.dynamic_footer.config(text=f"Time Elapsed: {minutes}m {seconds}s")

    def new_file(self):
        self.text.delete(1.0, tk.END)
        self.update_footer()

    def open_file(self):
        file_path = askopenfilename(filetypes=[("Text Files", "*.txt"), ("Word Documents", "*.docx"), ("CSV Files", "*.csv"), ("PDF Files", "*.pdf"), ("HTML Files", "*.html"), ("JSON Files", "*.json")])
        if file_path:
            self.text.delete(1.0, tk.END)
            with open(file_path, "r") as file:
                self.text.insert(tk.END, file.read())
            self.update_footer()

    def open_and_merge(self):
        file_paths = askopenfilename(multiple=True, filetypes=[("Text Files", "*.txt"), ("Word Documents", "*.docx"), ("CSV Files", "*.csv"), ("PDF Files", "*.pdf"), ("HTML Files", "*.html"), ("JSON Files", "*.json")])
        if file_paths:
            self.text.delete(1.0, tk.END)
            for file_path in file_paths:
                with open(file_path, "r") as file:
                    self.text.insert(tk.END, file.read() + "\n\n")
            self.update_footer()

    def compare_files(self):
        file_paths = askopenfilename(multiple=True, filetypes=[("Text Files", "*.txt")])
        if len(file_paths) == 2:
            with open(file_paths[0], "r") as file1, open(file_paths[1], "r") as file2:
                text1 = file1.readlines()
                text2 = file2.readlines()
                diff = difflib.unified_diff(text1, text2, fromfile="File1", tofile="File2")
                self.text.delete(1.0, tk.END)
                self.text.insert(tk.END, ''.join(diff))
        else:
            messagebox.showwarning("File Comparison", "Please select exactly two files for comparison.")

    def save_file(self):
        file_path = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("Word Documents", "*.docx"), ("CSV Files", "*.csv"), ("PDF Files", "*.pdf"), ("HTML Files", "*.html"), ("JSON Files", "*.json")])
        if file_path:
            content = self.text.get(1.0, tk.END)
            if file_path.endswith(".txt"):
                with open(file_path, "w") as file:
                    file.write(content)
            elif file_path.endswith(".docx"):
                doc = Document()
                doc.add_paragraph(content)
                doc.save(file_path)
            elif file_path.endswith(".csv"):
                with open(file_path, "w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow([content])
            elif file_path.endswith(".pdf"):
                pdf = fitz.open()
                pdf.add_page()
                pdf[0].insert_text((72, 72), content)
                pdf.save(file_path)
            elif file_path.endswith(".html"):
                with open(file_path, "w") as file:
                    file.write(f"<html><body>{html.escape(content)}</body></html>")
            elif file_path.endswith(".json"):
                with open(file_path, "w") as file:
                    json.dump(content, file)
            self.update_footer()

    def save_as_file(self):
        self.save_file()

    def export_file(self):
        file_path = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("Word Documents", "*.docx"), ("CSV Files", "*.csv"), ("PDF Files", "*.pdf"), ("HTML Files", "*.html"), ("JSON Files", "*.json")])
        if file_path:
            self.save_file()

    def load_template(self, industry, template_name):
        if industry in TEMPLATES and template_name in TEMPLATES[industry]:
            template_content = TEMPLATES[industry][template_name]
            self.text.delete(1.0, tk.END)
            self.text.insert(tk.END, template_content)

    def add_custom_template(self):
        industry = simpledialog.askstring("Industry", "Enter the industry (e.g., Business, Education, Creative Writing):")
        if industry not in TEMPLATES:
            TEMPLATES[industry] = {}
        template_name = simpledialog.askstring("Template Name", "Enter the template name:")
        if template_name:
            template_content = simpledialog.askstring("Template Content", "Enter the template content:")
            if template_content:
                TEMPLATES[industry][template_name] = template_content

    def delete_custom_template(self):
        industry = simpledialog.askstring("Industry", "Enter the industry of the template to delete:")
        if industry in TEMPLATES and industry != "Custom Templates":
            template_name = simpledialog.askstring("Template Name", "Enter the template name to delete:")
            if template_name in TEMPLATES[industry]:
                del TEMPLATES[industry][template_name]
                messagebox.showinfo("Template Deleted", f"Template '{template_name}' has been deleted.")
            else:
                messagebox.showwarning("Template Not Found", "Template not found.")
        else:
            messagebox.showwarning("Invalid Industry", "Please enter a valid industry.")

    def dark_mode(self):
        self.root.config(bg="black")
        self.text.config(bg="black", fg="white")
        self.footer_frame.config(bg="black")
        self.dynamic_footer.config(bg="black", fg="white")
        self.toolbar.config(bg="black")

    def light_mode(self):
        self.root.config(bg="white")
        self.text.config(bg="white", fg="black")
        self.footer_frame.config(bg="black")
        self.dynamic_footer.config(bg="black", fg="white")
        self.toolbar.config(bg="black")

    def show_options(self):
        messagebox.showinfo("About", "Copyright (C) 2024, Sourceduty")

    def show_statistics(self):
        content = self.text.get(1.0, tk.END)
        word_count = len(content.split())
        char_count = len(content)
        paragraph_count = content.count('\n\n') + 1
        messagebox.showinfo("Text Statistics", f"Word Count: {word_count}\nCharacter Count: {char_count}\nParagraph Count: {paragraph_count}")

    def generate_password(self):
        length = simpledialog.askinteger("Password Length", "Enter the length of the password:")
        if length:
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for i in range(length))
            messagebox.showinfo("Generated Password", f"Password: {password}")

    def export_list(self):
        content = self.text.get(1.0, tk.END)
        lines = content.splitlines()
        sorted_lines = sorted(lines)
        with open("sorted_list.txt", "w") as file:
            file.write("\n".join(sorted_lines))
        messagebox.showinfo("Export", "List sorted and exported to 'sorted_list.txt'")

    def translate_to_english(self):
        content = self.text.get(1.0, tk.END)
        translated_content = self.mock_translate_to_english(content)
        self.text.delete(1.0, tk.END)
        self.text.insert(tk.END, translated_content)
        
    def mock_translate_to_english(self, content):
        return content

    def insert_timestamp(self):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        self.text.insert(tk.INSERT, f"\nTimestamp: {timestamp}")

    def exit(self):
        self.root.quit()

root = tk.Tk()
app = TextEditor(root)
root.mainloop()
