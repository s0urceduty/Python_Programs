"""
Autoformat Notepad V1.0

Copyright (C) 2024, Sourceduty - All Rights Reserved.

"""

import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox, Menu, Label
from pygments import lex
from pygments.lexers import PythonLexer, HtmlLexer, JavascriptLexer, CLexer, JavaLexer, JsonLexer
from pygments.token import Token

def get_lexer_by_content(content):
    if 'import' in content or 'def' in content or 'class' in content:
        return PythonLexer(), '.py'
    elif '<html>' in content or '</html>' in content:
        return HtmlLexer(), '.html'
    elif 'function' in content or 'const' in content or 'let' in content:
        return JavascriptLexer(), '.js'
    elif '#include' in content or 'int main' in content:
        return CLexer(), '.c'
    elif 'public class' in content:
        return JavaLexer(), '.java'
    elif '{"' in content or '":' in content:
        return JsonLexer(), '.json'
    else:
        return None, '.txt'

class AutoformatNotepadV1:
    def __init__(self, root):
        self.root = root
        self.root.title("Autoformat Notepad V1.0")
        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, undo=True)
        self.text_area.pack(fill=tk.BOTH, expand=True)
        self.text_area.bind('<KeyRelease>', self.update_highlight_and_status)
        self.status_bar = Label(self.root, text="File format: .txt", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        self.menu_bar = Menu(self.root)
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Exit", command=self.exit_app)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.edit_menu = Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(label="Undo", command=self.text_area.edit_undo)
        self.edit_menu.add_command(label="Redo", command=self.text_area.edit_redo)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.view_menu = Menu(self.menu_bar, tearoff=0)
        self.view_menu.add_command(label="Dark Mode", command=lambda: self.apply_theme('dark'))
        self.view_menu.add_command(label="Light Mode", command=lambda: self.apply_theme('light'))
        self.menu_bar.add_cascade(label="View", menu=self.view_menu)
        self.root.config(menu=self.menu_bar)

    def new_file(self):
        self.text_area.delete("1.0", tk.END)
        self.status_bar.config(text="File format: .txt")

    def open_file(self):
        file = filedialog.askopenfilename()
        if file:
            with open(file, 'r') as f:
                data = f.read()
                self.text_area.delete("1.0", tk.END)
                self.text_area.insert("1.0", data)
            _, ext = get_lexer_by_content(data)
            self.status_bar.config(text=f"File format: {ext}")

    def save_file(self):
        content = self.text_area.get("1.0", tk.END)
        lexer, default_extension = get_lexer_by_content(content)
        file = filedialog.asksaveasfilename(defaultextension=default_extension, filetypes=[("All files", "*.*"), ("Text files", "*.txt"), ("Python files", "*.py"), ("HTML files", "*.html"), ("JavaScript files", "*.js"), ("C files", "*.c"), ("Java files", "*.java"), ("JSON files", "*.json")])
        if file:
            with open(file, 'w') as f:
                f.write(content)
            self.status_bar.config(text=f"File format: {default_extension}")

    def exit_app(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()

    def update_highlight_and_status(self, event=None):
        start = "1.0"
        end = "end"
        self.text_area.mark_set("range_start", start)
        data = self.text_area.get(start, end)
        lexer, file_extension = get_lexer_by_content(data)
        if lexer:
            self.highlight_syntax(data, lexer)
        self.status_bar.config(text=f"File format: {file_extension}")

    def highlight_syntax(self, data, lexer):
        for token, content in lex(data, lexer):
            self.text_area.mark_set("range_start", "range_start + %dc" % len(content))
            self.text_area.tag_add(str(token), "range_start - %dc" % len(content), "range_start")
        self.apply_tag_styles()

    def apply_tag_styles(self):
        self.text_area.tag_configure(str(Token.Keyword), foreground="#FF007F")
        self.text_area.tag_configure(str(Token.Name), foreground="#0000FF")
        self.text_area.tag_configure(str(Token.Literal.String), foreground="#BA2121")
        self.text_area.tag_configure(str(Token.Literal.Number), foreground="#7D00A6")
        self.text_area.tag_configure(str(Token.Operator), foreground="#000000")
        self.text_area.tag_configure(str(Token.Comment), foreground="#3F7F5F", font="TkFixedFont 9 italic")

    def apply_theme(self, theme):
        if theme == 'dark':
            self.text_area.config(bg="#2D2D2D", fg="#CCCCCC")
            self.status_bar.config(bg="#2D2D2D", fg="#CCCCCC")
        elif theme == 'light':
            self.text_area.config(bg="#FFFFFF", fg="#000000")
            self.status_bar.config(bg="#FFFFFF", fg="#000000")

def main():
    root = tk.Tk()
    notepad = AutoformatNotepadV1(root)
    root.mainloop()

if __name__ == "__main__":
    main()
