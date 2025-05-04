# Notepad Image V1.0
# Copyright (C) 2024, Sourceduty 

from PIL import ImageGrab
import tkinter as tk
from tkinter.filedialog import asksaveasfilename
from tkinter import messagebox

def export_note_as_image(self):
    try:
        # Update the window to ensure it's fully rendered
        self.root.update_idletasks()

        # Get the coordinates of the tkinter window
        x = self.root.winfo_rootx()
        y = self.root.winfo_rooty()
        width = self.root.winfo_width()
        height = self.root.winfo_height()

        # Take a screenshot of the tkinter window
        screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))

        # Ask the user where to save the image
        save_path = asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        
        if save_path:
            # Save the screenshot
            screenshot.save(save_path)
            messagebox.showinfo("Image Saved", f"Your screenshot has been saved as an image: {save_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while saving the image: {str(e)}")
