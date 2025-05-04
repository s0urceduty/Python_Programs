# ZIP Folder Topology Tool V1.0
# Copyright (C) 2024, Sourceduty - All Rights Reserved.

import os
import zipfile
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText

def create_topology(zip_path):
    topology = []
    zip_title = os.path.basename(zip_path)
    topology.append(zip_title + '/')
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        prev_dir = ''
        for file_info in zip_ref.infolist():
            file_path = file_info.filename
            if file_info.is_dir():
                continue

            dir_name, file_name = os.path.split(file_path)
            if dir_name != prev_dir:
                if dir_name:
                    folder_name = '  ' * dir_name.count(os.sep) + dir_name + '/'
                    topology.append(folder_name)
                prev_dir = dir_name

            topology.append('  ' * (dir_name.count(os.sep) + 1) + '|-- ' + file_name)
    
    return '\n'.join(topology)

def open_zip_file():
    zip_path = filedialog.askopenfilename(filetypes=[("Zip files", "*.zip")])
    if zip_path:
        topology = create_topology(zip_path)
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, topology)
    else:
        messagebox.showwarning("Warning", "No file selected")

def save_as_text_file():
    topology = text_area.get(1.0, tk.END)
    if topology.strip():
        save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if save_path:
            with open(save_path, 'w') as file:
                file.write(topology)
            messagebox.showinfo("Success", f"File saved as {save_path}")
    else:
        messagebox.showwarning("Warning", "No topology to save")

def clear_text_area():
    text_area.delete(1.0, tk.END)

root = tk.Tk()
root.title("Zip Topology Viewer")

root.configure(bg='black')

text_area = ScrolledText(root, wrap=tk.WORD, fg='yellow', bg='black', insertbackground='yellow')
text_area.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=10, pady=10)

open_button = tk.Button(root, text="Open Zip File", command=open_zip_file, fg='yellow', bg='black')
open_button.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

save_button = tk.Button(root, text="Save as Text File", command=save_as_text_file, fg='yellow', bg='black')
save_button.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

clear_button = tk.Button(root, text="Clear", command=clear_text_area, fg='yellow', bg='black')
clear_button.grid(row=1, column=2, sticky="ew", padx=5, pady=5)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_rowconfigure(0, weight=1)

root.mainloop()
