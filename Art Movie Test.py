import tkinter as tk
from tkinter import ttk

# ASCII Art Frames for the Alien
frames = [
    "     .-''''''-.\n    .'          '.\n   /   O      O   \\\n  :           `    :\n  |                |  \n  :    .------.    :\n   \\  '        '  /\n    '.          .'\n      '-......-'",
    "    .-''''''-.\n   .'          '.\n  /   O      O   \\\n :           `    :\n |                |   \n :    .------.    :\n  \\  '        '  /\n   '.          .'\n     '-......-'",
    "   .-''''''-.\n  .'          '.\n /   O      O   \\\n:           `    :\n|                |    \n:    .------.    :\n \\  '        '  /\n  '.          .'\n    '-......-'"
]

class ASCIIAnimation:
    def __init__(self, root):
        self.root = root
        self.animating = False
        self.frame_index = 0
        self.x_pos = root.winfo_screenwidth()

        # ASCII Art Label
        self.art_label = tk.Label(root, text="", font=("Courier", 14), justify="left")
        self.art_label.pack(pady=20)

        # Play Button
        self.play_button = ttk.Button(root, text="Play", command=self.animate)
        self.play_button.pack(side=tk.LEFT, padx=20)

        # Pause Button
        self.pause_button = ttk.Button(root, text="Pause", command=self.stop)
        self.pause_button.pack(side=tk.LEFT)

        # Speed Slider Label
        self.speed_label = tk.Label(root, text="Speed")
        self.speed_label.pack(side=tk.LEFT)

        # Speed Slider
        self.speed_slider = ttk.Scale(root, from_=1, to_=10, orient=tk.HORIZONTAL)
        self.speed_slider.set(5)
        self.speed_slider.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=20)

    def animate(self):
        if not self.animating:
            self.animating = True
            self.animation_loop()

    def stop(self):
        self.animating = False
        self.frame_index = 0
        self.x_pos = self.root.winfo_screenwidth()

    def animation_loop(self):
        if self.animating:
            if self.x_pos < -200:  # Arbitrary value past the left side to reset
                self.x_pos = self.root.winfo_screenwidth()
                self.frame_index = 0
            
            frame = frames[self.frame_index % len(frames)]
            self.art_label.config(text=frame)
            self.art_label.place(x=self.x_pos, y=100)  # Adjust y for vertical positioning

            self.frame_index += 1
            if self.frame_index >= len(frames):
                self.frame_index = 0

            speed = int(self.speed_slider.get())
            self.x_pos -= (speed * 10)  # Adjust speed factor as needed

            self.root.after(100, self.animation_loop)

# Application Window
root = tk.Tk()
root.geometry("800x600")
root.title("ASCII Art Movie")

app = ASCIIAnimation(root)

root.mainloop()

