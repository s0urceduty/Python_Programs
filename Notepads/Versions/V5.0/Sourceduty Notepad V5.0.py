# Sourceduty Notepad V5.0
# Copyright (C) 2024, Sourceduty

# pip install tkinter python-docx PyMuPDF googletrans==4.0.0-rc1

import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
import csv
import os
import json
from docx import Document
import fitz
import difflib
import time
import random
import string
from googletrans import Translator

LANGUAGES = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Chinese": "zh-cn",
    "Japanese": "ja",
    "Russian": "ru",
    "Italian": "it"
}

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
        self.root.title("Sourceduty Notepad V5.0")
        self.language = 'en'
        self.current_file = None
        self.micronotes = []
        self.start_time = time.time()

        self.text = tk.Text(root, wrap="word", bg="black", fg="white", insertbackground="white")
        self.text.pack(expand=1, fill="both")

        self.footer_frame = tk.Frame(root, bg="black")
        self.footer_frame.pack(side="bottom", fill="x")

        self.dynamic_footer = tk.Label(self.footer_frame, text="Time Elapsed: 0m 0s", bg="black", fg="white")
        self.dynamic_footer.pack(side="left")

        self.timestamp_button = tk.Button(self.footer_frame, text="Insert Timestamp", command=self.insert_timestamp, bg="black", fg="white")
        self.timestamp_button.pack(side="right")

        self.micronotes_button = tk.Button(self.footer_frame, text="Micronotes", command=self.show_micronotes_menu, bg="black", fg="white")
        self.micronotes_button.pack(side="right")

        self.create_menu()
        self.translator = Translator()
        self.insert_default_description()

    def create_menu(self):
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Open and Merge", command=self.open_and_merge)
        self.file_menu.add_command(label="Compare Files", command=self.compare_files)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_as_file)
        self.file_menu.add_command(label="Export", command=self.export_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)

        self.template_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Templates", menu=self.template_menu)
        for industry, templates in TEMPLATES.items():
            industry_menu = tk.Menu(self.template_menu, tearoff=0)
            self.template_menu.add_cascade(label=industry, menu=industry_menu)
            for template_name in templates:
                industry_menu.add_command(label=template_name, command=lambda name=template_name, ind=industry: self.load_template(ind, name))
        self.template_menu.add_separator()
        self.template_menu.add_command(label="Add Custom Template", command=self.add_custom_template)

        self.mode_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Mode", menu=self.mode_menu)
        self.mode_menu.add_command(label="Dark Mode", command=self.dark_mode)
        self.mode_menu.add_command(label="Light Mode", command=self.light_mode)

        self.tools_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Control", menu=self.tools_menu)
        self.tools_menu.add_command(label="Password", command=self.generate_password)
        self.tools_menu.add_command(label="Export List", command=self.export_list)
        self.tools_menu.add_command(label="Statistics", command=self.show_statistics)
        self.tools_menu.add_command(label="Translate Text", command=self.translate_document)
        self.tools_menu.add_command(label="Import Restore", command=self.import_restore)
        self.tools_menu.add_command(label="Text Layout", command=self.adjust_layout)
        self.tools_menu.add_command(label="About", command=self.show_options)

    def new_file(self):
        self.text.delete(1.0, tk.END)
        self.current_file = None

    def open_file(self):
        file = askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if not file:
            return
        with open(file, "r", encoding="utf-8") as f:
            self.text.delete(1.0, tk.END)
            self.text.insert(tk.END, f.read())
        self.current_file = file

    def save_file(self):
        if self.current_file:
            with open(self.current_file, "w", encoding="utf-8") as f:
                f.write(self.text.get(1.0, tk.END))
        else:
            self.save_as_file()

    def compare_files(self):
        file1 = askopenfilename(title="Select First File", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        file2 = askopenfilename(title="Select Second File", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if not file1 or not file2:
            return
        with open(file1, "r", encoding="utf-8") as f1, open(file2, "r", encoding="utf-8") as f2:
            content1 = f1.readlines()
            content2 = f2.readlines()
        diff = difflib.unified_diff(content1, content2, lineterm="")
        diff_text = "\n".join(list(diff))
        self.text.delete(1.0, tk.END)
        self.text.insert(tk.END, diff_text)

    def export_file(self):
        file = asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if not file:
            return
        with open(file, "w", encoding="utf-8") as f:
            f.write(self.text.get(1.0, tk.END))

    def show_micronotes_menu(self):
        def add_micronote():
            manage_window = tk.Toplevel(self.root)
            manage_window.title("Micronotes")
            manage_window.geometry("400x300")

            notes_text = tk.Text(manage_window, wrap="word")
            notes_text.pack(expand=1, fill="both")
            notes_text.insert(tk.END, "\n".join(self.micronotes))
            
            def save_note():
                note = notes_text.get(1.0, tk.END).strip()
                if note and len(note.split()) <= 500:
                    self.micronotes.append(note)
                    manage_window.destroy()
                elif len(note.split()) > 500:
                    messagebox.showerror("Error", "Micronote exceeds 500 words limit.")

            save_button = tk.Button(manage_window, text="Save Note", command=save_note)
            save_button.pack(side="bottom", pady=10)

        def manage_notes():
            manage_window = tk.Toplevel(self.root)
            manage_window.title("Manage Notes")
            manage_window.geometry("400x300")

            notes_text = tk.Text(manage_window, wrap="word")
            notes_text.pack(expand=1, fill="both")
            for note in self.micronotes:
                notes_text.insert(tk.END, note + "\n\n")

            def delete_note():
                selected_text = notes_text.get(tk.SEL_FIRST, tk.SEL_LAST)
                if selected_text.strip() in self.micronotes:
                    self.micronotes.remove(selected_text.strip())
                    notes_text.delete(tk.SEL_FIRST, tk.SEL_LAST)
                    self.update_footer()

            delete_button = tk.Button(manage_window, text="Delete Selected Note", command=delete_note)
            delete_button.pack(side="bottom", pady=10)

            notes_text.config(bg="black", fg="white", insertbackground="white")
            notes_text.bind("<Control-a>", lambda e: notes_text.tag_add("sel", "1.0", "end"))

        menu = tk.Menu(self.root, tearoff=0)
        menu.add_command(label="Add Micronote", command=add_micronote)
        menu.add_command(label="Manage Notes", command=manage_notes)
        menu.post(self.root.winfo_pointerx(), self.root.winfo_pointery())

    def load_template_dialog(self):
        industry = simpledialog.askstring("Template Industry", "Enter industry (e.g., Business, Creative Writing):")
        if not industry:
            return

        template_name = simpledialog.askstring("Template Name", "Enter template name:")
        if not template_name:
            return

        self.load_template(industry, template_name)

    def insert_default_description(self):
        default_description = (
            "Sourceduty Notepad V5.0\n"
            "Copyright (C) 2024, Sourceduty\n\n"
            "Welcome to Sourceduty Notepad V5.0, your versatile text editor designed for various industry needs.\n\n"
            "Features:\n\n"
            "- Modes: Switch between Dark Mode and Light Mode for comfortable reading and editing.\n"
            "- File Operations: Open, save, and merge files of various formats including text, Word documents, CSV, PDF, HTML, and JSON.\n"
            "- Open and Merge: Combine multiple files into one text document.\n"
            "- Text Editing: Edit and format text with various options.\n"
            "- Compare Files: View differences between two text files.\n"
            "- File Comparison: Compare two text files and view differences.\n"
            "- Text Statistics: Analyze word count, character count, and paragraph count.\n"
            "- Save As: Save your document in various file formats.\n"
            "- Insert Timestamp: Quickly insert a timestamp into your text.\n"
            "- Load Template: Use predefined templates for different industries.\n"
            "- Add Custom Template: Create and add your own custom templates to fit your specific needs.\n"
            "- Text Analysis: Analyze your text with features like word count, character count, and line count.\n"
            "- Password Generation: Generate secure passwords with customizable length and complexity.\n"
            "- Export List: Save a list of items from your document as a text file with unique items.\n"
            "- Translation: Translate your document into different languages.\n"
            "- Import Restore: Fix the structure, format, and punctuation of imported files.\n"
            "- Micronotes: Store up to 500 words in micronotes with a new footer button and push-up menu.\n"
            "\n\nRepository: https://github.com/sourceduty/Notepad"
        )
        
        self.text.insert(tk.END, default_description)
        self.text.config(bg="black", fg="white")  
        self.text.delete(1.0, tk.END)  
        self.text.insert(tk.END, default_description)

    def open_and_merge(self):
        files = filedialog.askopenfilenames(filetypes=[("All Files", "*.*")])
        if not files:
            return

        combined_text = ""
        for file in files:
            with open(file, "r", encoding="utf-8") as f:
                combined_text += f.read() + "\n\n"

        self.text.delete(1.0, tk.END)
        self.text.insert(tk.END, combined_text)

    def save_as_file(self):
        file = asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if not file:
            return

        with open(file, "w", encoding="utf-8") as f:
            f.write(self.text.get(1.0, tk.END))

    def load_template(self, industry, template_name):
        if industry in TEMPLATES and template_name in TEMPLATES[industry]:
            template_content = TEMPLATES[industry][template_name]
            self.text.delete(1.0, tk.END)
            self.text.insert(tk.END, template_content)
        else:
            messagebox.showerror("Error", "Template not found.")

    def add_custom_template(self):
        name = simpledialog.askstring("Template Name", "Enter custom template name:")
        if not name:
            return

        content = simpledialog.askstring("Template Content", "Enter the content of the custom template:")
        if not content:
            return

        TEMPLATES["Custom Templates"][name] = content
        messagebox.showinfo("Template Added", "Custom template added successfully!")

    def dark_mode(self):
        self.text.config(bg="black", fg="white")
        self.dynamic_footer.config(bg="black", fg="white")
        self.timestamp_button.config(bg="black")
        self.micronotes_button.config(bg="black")

    def light_mode(self):
        self.text.config(bg="white", fg="black")
        self.dynamic_footer.config(bg="black", fg="white")
        self.timestamp_button.config(bg="black")
        self.micronotes_button.config(bg="black")

    def show_statistics(self):
        text_content = self.text.get(1.0, tk.END)
        word_count = len(text_content.split())
        char_count = len(text_content)
        line_count = text_content.count("\n")
        messagebox.showinfo("Statistics", f"Words: {word_count}\nCharacters: {char_count}\nLines: {line_count}")

    def show_options(self):
        messagebox.showinfo("About", "Copyright (C) 2024, Sourceduty")

    def generate_password(self):
        length = simpledialog.askinteger("Password Length", "Enter password length:", minvalue=8, maxvalue=128)
        if not length:
            return

        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(chars) for _ in range(length))
        self.text.delete(1.0, tk.END)
        self.text.insert(tk.END, f"Generated Password: {password}")

    def export_list(self):
        content = self.text.get(1.0, tk.END).splitlines()
        unique_items = list(set(content))
        file = asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if not file:
            return

        with open(file, "w", encoding="utf-8") as f:
            for item in unique_items:
                f.write(item + "\n")

    def translate_document(self):
        text_content = self.text.get(1.0, tk.END)
        translated_text = self.translator.translate(text_content, dest=self.language).text
        self.text.delete(1.0, tk.END)
        self.text.insert(tk.END, translated_text)

    def import_restore(self):
        messagebox.showinfo("Import Restore", "Restoration of imported file structure, format, and punctuation is not yet implemented.")

    def adjust_layout(self):
        messagebox.showinfo("Layout Adjustment", "Layout adjustment feature is not yet implemented.")

    def insert_timestamp(self):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        self.text.insert(tk.END, f"{timestamp}")

    def update_footer(self):
        elapsed_time = time.time() - self.start_time
        minutes, seconds = divmod(int(elapsed_time), 60)
        self.dynamic_footer.config(text=f"Time Elapsed: {minutes}m {seconds}s")

if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditor(root)
    root.mainloop()
