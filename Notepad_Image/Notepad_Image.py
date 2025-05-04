# Notepad Image V1.0
# Copyright (C) 2024, Sourceduty

import tkinter as tk
from tkinter.filedialog import asksaveasfilename
from tkinter import messagebox
import pyautogui


class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Notepad Image V1.0")
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

        # Images Menu
        images_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Images", menu=images_menu)
        images_menu.add_command(label="Export Note as Image", command=self.export_note_as_image)

        # Mode Menu
        mode_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Mode", menu=mode_menu)
        mode_menu.add_command(label="Dark Mode", command=self.set_dark_mode)
        mode_menu.add_command(label="Light Mode", command=self.set_light_mode)

        # Options Menu
        options_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Options", menu=options_menu)
        options_menu.add_command(label="Undo", command=self.undo)
        options_menu.add_command(label="Redo", command=self.redo)

        # Help Menu
        help_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.about)

    def export_note_as_image(self):
        try:
            # Update the tkinter GUI to ensure rendering is complete
            self.root.update()
            self.root.update_idletasks()

            # Get the position and dimensions of the window
            x = self.root.winfo_rootx()
            y = self.root.winfo_rooty()
            width = self.root.winfo_width()
            height = self.root.winfo_height()

            # Take a screenshot of the defined region
            screenshot = pyautogui.screenshot(region=(x, y, width, height))

            # Ask the user where to save the image
            save_path = asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if save_path:
                screenshot.save(save_path)
                messagebox.showinfo("Image Saved", f"Your screenshot has been saved: {save_path}")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while saving the image: {str(e)}")

    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.mode = "new"

    def open_file(self):
        file_path = asksaveasfilename(filetypes=[("Text Files", "*.txt")])
        if not file_path:
            return
        with open(file_path, "r") as input_file:
            text = input_file.read()
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, text)
        self.root.title(f"Notepad Image V1.0 - {file_path}")

    def save_file(self):
        if self.mode == "new":
            self.save_as_file()
        else:
            with open(self.current_file, "w") as output_file:
                text = self.text_area.get(1.0, tk.END)
                output_file.write(text)

    def save_as_file(self):
        file_path = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if not file_path:
            return
        with open(file_path, "w") as output_file:
            text = self.text_area.get(1.0, tk.END)
            output_file.write(text)
        self.current_file = file_path
        self.mode = "saved"

    def exit(self):
        self.root.quit()

    def create_widgets(self):
        self.text_area = tk.Text(self.root)
        self.text_area.pack(expand=1, fill='both')

        # Default description
        default_description = (
            "Notepad Image V1.0\n"
            "Copyright (C) 2024, Sourceduty\n\n"
            "This notepad was developed for text editing and image export functionalities.\n\n"
            "Features: \n"
            "- Light and Dark Mode: Switch between light and dark themes.\n"
            "- Export Note as Image: Save your notes as images (PNG format).\n"
            "- Undo/Redo: Support for undoing and redoing changes.\n"
            "- File Operations: Create, open, save, and save files as different formats.\n"
            "- Options and About: Access options and learn more about the application.\n"
            "\n\nRepository: https://github.com/sourceduty/Notepad_Image"
        )
        self.text_area.insert(tk.END, default_description)
        self.set_dark_mode()

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

    def about(self):
        messagebox.showinfo("About", "Notepad Image V1.0\nCopyright (C) 2024, Sourceduty")

    def set_light_mode(self):
        self.text_area.config(bg="white", fg="black", insertbackground="black")
        self.mode = "light"

    def set_dark_mode(self):
        self.text_area.config(bg="black", fg="white", insertbackground="white")
        self.mode = "dark"


# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditor(root)
    root.mainloop()
