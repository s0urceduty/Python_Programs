import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import json
import os

class ColorNotepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Color Notepad")
        self.root.geometry("700x500")

        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Consolas", 12))
        self.text_area.pack(fill=tk.BOTH, expand=True)

        self._setup_tags()
        self._setup_menu()
        self._setup_toolbar()

    def _setup_tags(self):
        for color in ['red', 'green', 'blue']:
            self.text_area.tag_config(color, foreground=color)

    def _setup_menu(self):
        menu_bar = tk.Menu(self.root)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Save (.txt + .json)", command=self.save_note)
        file_menu.add_command(label="Open .txt with color", command=self.load_note)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)
        self.root.config(menu=menu_bar)

    def _setup_toolbar(self):
        frame = tk.Frame(self.root)
        frame.pack(fill=tk.X)
        tk.Button(frame, text="Red", fg="red", command=lambda: self.apply_color("red")).pack(side=tk.LEFT)
        tk.Button(frame, text="Green", fg="green", command=lambda: self.apply_color("green")).pack(side=tk.LEFT)
        tk.Button(frame, text="Blue", fg="blue", command=lambda: self.apply_color("blue")).pack(side=tk.LEFT)

    def apply_color(self, color):
        try:
            start = self.text_area.index(tk.SEL_FIRST)
            end = self.text_area.index(tk.SEL_LAST)
            self.text_area.tag_add(color, start, end)
        except tk.TclError:
            messagebox.showwarning("No selection", "Please select text to apply color.")

    def save_note(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text Files", "*.txt")],
                                                 title="Save Note")
        if not file_path:
            return

        # Save text
        text_content = self.text_area.get("1.0", tk.END)
        with open(file_path, "w", encoding="utf-8") as txt_file:
            txt_file.write(text_content)

        # Save colors
        color_data = []
        for tag in ['red', 'green', 'blue']:
            ranges = self.text_area.tag_ranges(tag)
            for i in range(0, len(ranges), 2):
                start = ranges[i].string
                end = ranges[i+1].string
                color_data.append({
                    "tag": tag,
                    "start": start,
                    "end": end
                })

        json_path = os.path.splitext(file_path)[0] + ".json"
        with open(json_path, "w", encoding="utf-8") as json_file:
            json.dump(color_data, json_file, indent=2)

        messagebox.showinfo("Saved", f"Saved:\n{file_path}\nand\n{json_path}")

    def load_note(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if not file_path:
            return

        # Load text
        try:
            with open(file_path, "r", encoding="utf-8") as txt_file:
                content = txt_file.read()
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert("1.0", content)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load text:\n{e}")
            return

        # Load color metadata
        json_path = os.path.splitext(file_path)[0] + ".json"
        if os.path.exists(json_path):
            try:
                with open(json_path, "r", encoding="utf-8") as json_file:
                    color_data = json.load(json_file)
                for item in color_data:
                    self.text_area.tag_add(item["tag"], item["start"], item["end"])
            except Exception as e:
                messagebox.showwarning("Warning", f"Could not load color metadata:\n{e}")
        else:
            messagebox.showinfo("Info", "No color metadata (.json) found. Loaded plain text only.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ColorNotepad(root)
    root.mainloop()
