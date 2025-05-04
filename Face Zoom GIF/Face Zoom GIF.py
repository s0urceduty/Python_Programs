# Face Zoom GIF
# Copyright (C) 2024 [Sourceduty] - All Rights Reserved.

import tkinter as tk
from tkinter import filedialog
from PIL import Image
import cv2
import numpy as np
import imageio
import os

class ImageProcessor:
    def __init__(self, root):
        self.root = root
        self.root.title("Sliced GIF Maker")
        self.root.geometry("650x350")
        self.root.configure(bg="gray")

        self.frame = tk.Frame(root, bg="gray")
        self.frame.pack(pady=10)

        self.load_button = tk.Button(self.frame, text="Load Image", command=self.load_image)
        self.load_button.grid(row=0, column=0, padx=5)

        self.process_button = tk.Button(self.frame, text="Create GIF", command=self.process_image)
        self.process_button.grid(row=0, column=1, padx=5)

        self.progress_label = tk.Label(root, text="", fg="yellow", bg="black")
        self.progress_label.pack(fill="both", expand=True, pady=10)

        self.image = None
        self.image_path = None

        # Create GIFs directory if it doesn't exist
        if not os.path.exists("GIFs"):
            os.makedirs("GIFs")

    def load_image(self):
        self.image_path = filedialog.askopenfilename()
        self.image = Image.open(self.image_path)
        self.progress_label.config(text="Image loaded. Ready to create GIF.")

    def process_image(self):
        if self.image_path:
            # Detect face and create GIF
            gif_path = self.zoom_in_on_face(self.image_path)
            self.progress_label.config(text=f"GIF saved at {gif_path}")

    def zoom_in_on_face(self, image_path):
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        img = cv2.imread(image_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        if len(faces) == 0:
            self.progress_label.config(text="No faces found")
            return

        x, y, w, h = faces[0]
        face_center = (x + w // 2, y + h // 2)
        original_size = img.shape[1], img.shape[0]

        frames = []
        steps = 5
        for i in range(steps):
            zoom_factor = 1 - (i / steps)
            new_width = int(original_size[0] * zoom_factor)
            new_height = int(original_size[1] * zoom_factor)

            top_left_x = max(0, face_center[0] - new_width // 2)
            top_left_y = max(0, face_center[1] - new_height // 2)
            bottom_right_x = min(original_size[0], face_center[0] + new_width // 2)
            bottom_right_y = min(original_size[1], face_center[1] + new_height // 2)

            cropped = img[top_left_y:bottom_right_y, top_left_x:bottom_right_x]
            resized = cv2.resize(cropped, original_size, interpolation=cv2.INTER_LINEAR)
            frames.append(Image.fromarray(cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)))
            self.progress_label.config(text=f"Processing step {i + 1}/{steps}")
            self.root.update()

        gif_path = os.path.join("GIFs", "zoomed_face.gif")
        frames[0].save(gif_path, save_all=True, append_images=frames[1:], loop=0, duration=100)
        return gif_path

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessor(root)
    root.mainloop()

