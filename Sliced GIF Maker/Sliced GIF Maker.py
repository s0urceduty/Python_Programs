# Sliced GIF Maker
# Copyright (C) 2024, Sourceduty - All Rights Reserved.
# Create a unique GIF using uploaded image files.

import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sliced GIF Maker")
        self.root.configure(bg='grey')
        
        self.load_button = tk.Button(root, text="Load Image", command=self.load_image, fg='white', bg='grey')
        self.load_button.pack(pady=5)
        
        self.create_gif_button = tk.Button(root, text="Create GIF", command=self.create_gif, state=tk.DISABLED, fg='white', bg='grey')
        self.create_gif_button.pack(pady=5)
        
        self.progress_text = tk.Text(root, height=10, bg='black', fg='yellow')
        self.progress_text.pack(pady=5)
        
        self.image = None
        self.pieces = []
        
    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = Image.open(file_path)
            self.progress_text.insert(tk.END, "Image loaded.\n")
            self.progress_text.see(tk.END)
            self.create_gif_button.config(state=tk.NORMAL)
    
    def process_image(self, image, num_splits=4):
        width, height = image.size
        piece_width = width // num_splits
        piece_height = height // num_splits

        self.pieces = []
        for i in range(num_splits):
            for j in range(num_splits):
                left = j * piece_width
                upper = i * piece_height
                right = left + piece_width if (j + 1) * piece_width <= width else width
                lower = upper + piece_height if (i + 1) * piece_height <= height else height
                box = (left, upper, right, lower)
                piece = image.crop(box)
                self.pieces.append(piece)
    
    def create_gif(self):
        if not self.image:
            return
        
        self.progress_text.insert(tk.END, "Processing image...\n")
        self.progress_text.see(tk.END)
        num_splits = 4  # You can change this value to split into more pieces
        self.process_image(self.image, num_splits=num_splits)
        
        gif_frames = []
        width, height = self.image.size
        piece_width = width // num_splits
        piece_height = height // num_splits
        new_image = Image.new('RGB', (width, height))
        
        for i in range(len(self.pieces)):
            y = i // num_splits
            x = i % num_splits
            left = x * piece_width
            upper = y * piece_height
            new_image.paste(self.pieces[i], (left, upper))
            gif_frames.append(new_image.copy())  # Copy the image to avoid mutating the same image
            self.progress_text.insert(tk.END, f"Processed frame {i + 1}/{len(self.pieces)}.\n")
            self.progress_text.see(tk.END)
        
        # Add the full image as the last frame with a longer duration
        gif_frames.append(self.image)
        
        gif_path = filedialog.asksaveasfilename(defaultextension=".gif", filetypes=[("GIF files", "*.gif")])
        if gif_path:
            gif_frames[0].save(gif_path, save_all=True, append_images=gif_frames[1:], duration=[200] * len(gif_frames[:-1]) + [2000], loop=0)
            self.progress_text.insert(tk.END, f"GIF saved as {gif_path}\n")
            self.progress_text.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessorApp(root)
    root.mainloop()

