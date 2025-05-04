# Drag-Drop_Rename
# Drag and Drop to Folder with Random Naming
# Copyright (C) 2024, Sourceduty - All Rights Reserved.

import os
import shutil
import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
import secrets
import string

def generate_random_word(length=10):
    alphabet = string.ascii_lowercase + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def create_and_copy_files(file_list):
    new_folder_path = 'Renamed_Files'
    os.makedirs(new_folder_path, exist_ok=True)
    for file in file_list:
        extension = os.path.splitext(file)[1]
        random_word = generate_random_word()
        new_name = os.path.join(new_folder_path, f"{random_word}{extension}")
        shutil.copy(file, new_name)
    print(f"Files have been copied and renamed in {new_folder_path}")

def drop(event):
    file_list = root.tk.splitlist(event.data)
    create_and_copy_files(file_list)

root = TkinterDnD.Tk()
root.title('Drag and Drop Files Here')
root.geometry('400x400')

label = tk.Label(root, text='Drag files here', pady=20, padx=20)
label.pack(expand=True, fill=tk.BOTH)
label.drop_target_register(DND_FILES)
label.dnd_bind('<<Drop>>', drop)

root.mainloop()
