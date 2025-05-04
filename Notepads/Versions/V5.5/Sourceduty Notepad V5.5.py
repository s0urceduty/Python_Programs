# Sourceduty Notepad V5.5
# Copyright (C) 2024, Sourceduty

# pip install tkinter python-docx PyMuPDF pandas ebooklib beautifulsoup4

import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter.filedialog import asksaveasfilename, askopenfilename
import difflib
import fitz
import time
import random
import string
import csv
import json
import pandas as pd
from ebooklib import epub
from bs4 import BeautifulSoup
from docx import Document
import re

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
        self.root.title("Sourceduty Notepad V5.5")
        self.language = 'en'
        self.current_file = None
        self.micronotes = []
        self.start_time = time.time()
        self.keywords = []

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
        self.insert_default_description()
        self.update_footer()  # Start updating the footer

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
        self.file_menu.add_command(label="Import", command=self.import_file)
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
        self.tools_menu.add_command(label="Import Restore", command=self.import_restore)
        self.tools_menu.add_command(label="Text Layout", command=self.show_adjust_layout_menu)
        self.tools_menu.add_command(label="About", command=self.show_options)
        self.tools_menu.add_command(label="Search", command=self.search_word)
        self.tools_menu.add_command(label="Tagging and Categorization", command=self.tag_and_categorize)
        self.tools_menu.add_command(label="Keyword Highlighting", command=self.set_keywords)

    def show_adjust_layout_menu(self):
        adjust_layout_menu = tk.Menu(self.root, tearoff=0)
        
        adjust_layout_menu.add_command(label="Set Background Color", command=self.set_background_color)
        adjust_layout_menu.add_command(label="Set Foreground Color", command=self.set_foreground_color)
        adjust_layout_menu.add_command(label="Set Font Size", command=self.set_font_size)
        
        adjust_layout_menu.tk_popup(self.root.winfo_pointerx(), self.root.winfo_pointery())

    def set_background_color(self):
        color = simpledialog.askstring("Background Color", "Enter the background color (e.g., 'white'):")
        if color:
            self.text.config(bg=color)
            self.footer_frame.config(bg=color)
            self.dynamic_footer.config(bg=color)
            self.timestamp_button.config(bg=color)
            self.micronotes_button.config(bg=color)

    def set_foreground_color(self):
        color = simpledialog.askstring("Foreground Color", "Enter the foreground color (e.g., 'black'):")
        if color:
            self.text.config(fg=color)
            self.dynamic_footer.config(fg=color)
            self.timestamp_button.config(fg=color)
            self.micronotes_button.config(fg=color)

    def set_font_size(self):
        size = simpledialog.askinteger("Font Size", "Enter the font size (e.g., '12'):")
        if size:
            self.text.config(font=("Helvetica", size))

    def save_file(self):
        if self.current_file:
            with open(self.current_file, "w", encoding="utf-8") as f:
                f.write(self.text.get(1.0, tk.END))
        else:
            self.save_as_file()

    def save_as_file(self):
        file = asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if not file:
            return
        with open(file, "w", encoding="utf-8") as f:
            f.write(self.text.get(1.0, tk.END))
        self.current_file = file

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

    def open_and_merge(self):
        files = askopenfilename(multiple=True, filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if not files:
            return
        merged_text = ""
        for file in files:
            with open(file, "r", encoding="utf-8") as f:
                merged_text += f.read() + "\n"
        self.text.delete(1.0, tk.END)
        self.text.insert(tk.END, merged_text)

    def compare_files(self):
        file1 = askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if not file1:
            return
        file2 = askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if not file2:
            return
        with open(file1, "r", encoding="utf-8") as f1, open(file2, "r", encoding="utf-8") as f2:
            text1 = f1.readlines()
            text2 = f2.readlines()
        diff = difflib.unified_diff(text1, text2)
        diff_text = ''.join(diff)
        self.text.delete(1.0, tk.END)
        self.text.insert(tk.END, diff_text)

    def export_file(self):
        file = asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf"), ("Text files", "*.txt"), 
                                                                   ("CSV files", "*.csv"), ("HTML files", "*.html"),
                                                                   ("JSON files", "*.json"), ("EPUB files", "*.epub"),
                                                                   ("Python files", "*.py"), ("All files", "*.*")])
        if not file:
            return
        if file.endswith(".pdf"):
            with fitz.open() as doc:
                page = doc.new_page()
                page.insert_text((72, 72), self.text.get(1.0, tk.END), fontsize=12)
                doc.save(file)
        elif file.endswith(".txt"):
            with open(file, "w", encoding="utf-8") as f:
                f.write(self.text.get(1.0, tk.END))
        elif file.endswith(".csv"):
            with open(file, "w", encoding="utf-8", newline='') as f:
                writer = csv.writer(f)
                for line in self.text.get(1.0, tk.END).splitlines():
                    writer.writerow([line])
        elif file.endswith(".html"):
            with open(file, "w", encoding="utf-8") as f:
                html_content = f"<html><body><pre>{self.text.get(1.0, tk.END)}</pre></body></html>"
                f.write(html_content)
        elif file.endswith(".json"):
            text_content = self.text.get(1.0, tk.END)
            json_data = {"content": text_content}
            with open(file, "w", encoding="utf-8") as f:
                json.dump(json_data, f, ensure_ascii=False, indent=4)
        elif file.endswith(".epub"):
            book = epub.EpubBook()
            book.set_title("Sourceduty Notepad Export")
            book.add_author("Sourceduty")
            chapter = epub.EpubHtml(title="Content", file_name="chapter1.xhtml", lang="en")
            chapter.content = f"<h1>Exported Content</h1><p>{self.text.get(1.0, tk.END)}</p>"
            book.add_item(chapter)
            book.spine = ['nav', chapter]
            epub.write_epub(file, book)
        elif file.endswith(".py"):
            with open(file, "w", encoding="utf-8") as f:
                f.write(self.text.get(1.0, tk.END))

    def import_file(self):
        file = askopenfilename(filetypes=[("Text files", "*.txt"), ("CSV files", "*.csv"), ("JSON files", "*.json"), 
                                          ("EPUB files", "*.epub"), ("Python files", "*.py"), ("All files", "*.*")])
        if not file:
            return
        if file.endswith(".txt") or file.endswith(".py"):
            with open(file, "r", encoding="utf-8") as f:
                self.text.delete(1.0, tk.END)
                self.text.insert(tk.END, f.read())
        elif file.endswith(".csv"):
            with open(file, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                self.text.delete(1.0, tk.END)
                for row in reader:
                    self.text.insert(tk.END, ', '.join(row) + '\n')
        elif file.endswith(".json"):
            with open(file, "r", encoding="utf-8") as f:
                json_data = json.load(f)
                self.text.delete(1.0, tk.END)
                self.text.insert(tk.END, json_data.get("content", ""))
        elif file.endswith(".epub"):
            book = epub.read_epub(file)
            content = ""
            for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
                soup = BeautifulSoup(item.get_body_content(), "html.parser")
                content += soup.get_text() + "\n"
            self.text.delete(1.0, tk.END)
            self.text.insert(tk.END, content)

    def insert_timestamp(self):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        self.text.insert(tk.INSERT, f"{timestamp}")

    def show_micronotes_menu(self):
        menu = tk.Menu(self.root, tearoff=0)
        for note in self.micronotes:
            menu.add_command(label=note, command=lambda n=note: self.insert_micronote(n))
        menu.add_command(label="Add Micronote", command=self.add_micronote)
        menu.tk_popup(self.root.winfo_pointerx(), self.root.winfo_pointery())

    def add_micronote(self):
        note = simpledialog.askstring("Micronote", "Enter the text for the micronote:")
        if note:
            self.micronotes.append(note)

    def insert_micronote(self, note):
        self.text.insert(tk.INSERT, f"\nMicronote: {note}\n")

    def show_options(self):
        messagebox.showinfo("About", "Copyright (C) 2024, Sourceduty")

    def generate_password(self):
        length = simpledialog.askinteger("Password Length", "Enter the length of the password:")
        if length:
            chars = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(chars) for _ in range(length))
            messagebox.showinfo("Generated Password", f"Your password is: {password}")

    def export_list(self):
        file = asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if not file:
            return
        unique_items = set(self.text.get(1.0, tk.END).split())
        with open(file, "w", encoding="utf-8") as f:
            for item in unique_items:
                f.write(f"{item}\n")

    def show_statistics(self):
        text_content = self.text.get(1.0, tk.END)
        word_count = len(text_content.split())
        char_count = len(text_content)
        line_count = text_content.count('\n')
        messagebox.showinfo("Statistics", f"Words: {word_count}\nCharacters: {char_count}\nLines: {line_count}")

    def import_restore(self):
        file = askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if not file:
            return
        with open(file, "r", encoding="utf-8") as f:
            imported_text = f.read()
        self.text.delete(1.0, tk.END)
        self.text.insert(tk.END, imported_text)
        messagebox.showinfo("Import Restore", "Restoration of imported file structure, format, and punctuation is not yet implemented.")

    def insert_default_description(self):
        default_description = (
            "Sourceduty Notepad V5.5\n"
            "Copyright (C) 2024, Sourceduty\n\n"
            "Welcome to Sourceduty Notepad V5.5, your versatile text editor designed for various industry needs.\n\n"
            "Features:\n\n"
            "- Modes: Switch between Dark Mode and Light Mode for comfortable reading and editing.\n"
            "- File Operations: Open, save, and merge files of various formats including text, CSV, PDF, HTML, JSON, EPUB, and Python scripts.\n"
            "- Open and Merge: Combine multiple text files into one document.\n"
            "- Text Editing: Edit and format text with customizable font size, background, and foreground colors.\n"
            "- Compare Files: View differences between two text files side by side.\n"
            "- File Export: Save your document in various formats such as TXT, CSV, PDF, HTML, JSON, EPUB, and Python (.py).\n"
            "- File Import: Import and restore files from TXT, CSV, JSON, EPUB, and Python formats.\n"
            "- Text Statistics: Analyze your document with features like word count, character count, and line count.\n"
            "- Insert Timestamp: Quickly insert the current timestamp into your text.\n"
            "- Load Template: Use predefined templates for business, education, and creative writing needs.\n"
            "- Add Custom Template: Create and add your own custom templates to fit specific requirements.\n"
            "- Password Generation: Generate secure passwords with customizable length and complexity.\n"
            "- Export List: Save a list of unique items from your document as a text file.\n"
            "- Micronotes: Store and insert up to 500 words in micronotes with a convenient footer button.\n"
            "- Search: Search for specific words or strings within the document.\n"
            "- Tagging and Categorization: Automatically categorize and tag notes based on content for easier searching and organization.\n"
            "- Keyword Highlighting: Automatically highlight key terms or phrases based on user-defined keywords.\n"
            "\n\nRepository: https://github.com/sourceduty/Notepad"
        )
        self.text.config(bg="black", fg="white")  
        self.text.delete(1.0, tk.END)  
        self.text.insert(tk.END, default_description)

    def update_footer(self):
        elapsed_time = time.time() - self.start_time
        minutes, seconds = divmod(int(elapsed_time), 60)
        self.dynamic_footer.config(text=f"Time Elapsed: {minutes}m {seconds}s")
        self.root.after(1000, self.update_footer)  # Schedule the update to run again after 1 second

    def dark_mode(self):
        self.text.config(bg="black", fg="white")
        self.footer_frame.config(bg="black")
        self.dynamic_footer.config(bg="black", fg="white")
        self.timestamp_button.config(bg="black", fg="white")
        self.micronotes_button.config(bg="black", fg="white")

    def light_mode(self):
        self.text.config(bg="white", fg="black")
        self.footer_frame.config(bg="white")
        self.dynamic_footer.config(bg="white", fg="black")
        self.timestamp_button.config(bg="white", fg="black")
        self.micronotes_button.config(bg="white", fg="black")

    def load_template(self, industry, template_name):
        if industry in TEMPLATES and template_name in TEMPLATES[industry]:
            self.text.delete(1.0, tk.END)
            self.text.insert(tk.END, TEMPLATES[industry][template_name])
        else:
            messagebox.showwarning("Load Template", "Template not found.")

    def add_custom_template(self):
        template_name = simpledialog.askstring("Add Custom Template", "Enter a name for the new template:")
        if template_name:
            template_content = simpledialog.askstring("Add Custom Template", "Enter the content for the template:")
            if template_content:
                TEMPLATES["Custom"] = TEMPLATES.get("Custom", {})
                TEMPLATES["Custom"][template_name] = template_content
                messagebox.showinfo("Add Custom Template", "Template added successfully.")

    def search_word(self):
        word = simpledialog.askstring("Search", "Enter the word or phrase to search:")
        if word:
            content = self.text.get(1.0, tk.END)
            occurrences = [m.start() for m in re.finditer(word, content)]
            messagebox.showinfo("Search Results", f"Found {len(occurrences)} occurrences of '{word}'.")

    def tag_and_categorize(self):
        content = self.text.get(1.0, tk.END)
        categories = {
            "Business": ["meeting", "project", "schedule"],
            "Education": ["lecture", "essay", "homework"],
            "Creative Writing": ["story", "poem", "novel"]
        }
        tags = set()
        for category, keywords in categories.items():
            for keyword in keywords:
                if keyword in content.lower():
                    tags.add(category)
        messagebox.showinfo("Tagging and Categorization", f"Categories: {', '.join(tags)}")

    def set_keywords(self):
        keyword_str = simpledialog.askstring("Keywords", "Enter keywords to highlight (comma-separated):")
        if keyword_str:
            self.keywords = [kw.strip() for kw in keyword_str.split(",")]
            self.highlight_keywords()

    def highlight_keywords(self):
        content = self.text.get(1.0, tk.END)
        for keyword in self.keywords:
            start_idx = 1.0
            while True:
                start_idx = self.text.search(keyword, start_idx, stopindex=tk.END)
                if not start_idx:
                    break
                end_idx = f"{start_idx}+{len(keyword)}c"
                self.text.tag_add(keyword, start_idx, end_idx)
                self.text.tag_config(keyword, background="yellow")
                start_idx = end_idx

def main():
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()

if __name__ == "__main__":
    main()
