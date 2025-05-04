# Industry Notepad V1.0
# Copyright (C) 2024, Sourceduty 

import tkinter as tk
from text_editor import TextEditor

if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditor(root)
    root.mainloop()
