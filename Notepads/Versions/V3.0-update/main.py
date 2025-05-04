# Sourceduty Notepad V3.0-Update
# Copyright (C) 2024, Sourceduty 

import tkinter as tk
from text_editor import TextEditor

def main():
    root = tk.Tk()
    app = TextEditor(root)  # Initialize the text editor with file picker
    root.mainloop()

if __name__ == "__main__":
    main()
