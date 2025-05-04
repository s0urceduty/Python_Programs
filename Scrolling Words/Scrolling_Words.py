import tkinter as tk

# Text to be displayed
content = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit.

Donec tempor purus vitae dui iaculis, iaculis faucibus massa tincidunt. Integer ac molestie erat, ut tempus nibh.

Etiam non pulvinar lectus, sit amet lacinia urna.

Donec nec enim varius, feugiat dolor ut, tristique ligula. 

Morbi at nunc mollis mauris tristique consequat a rhoncus lectus.

Maecenas maximus nisi lacinia metus aliquam, feugiat hendrerit diam cursus.

Maecenas posuere lorem nulla, at imperdiet tellus laoreet eu.

Vivamus id pretium urna.

Pellentesque accumsan consectetur ante.

Suspendisse gravida odio nec turpis semper, at tincidunt massa accumsan.

Aenean mattis sapien nisi, ac consequat elit gravida ut. 

Pellentesque commodo, justo ut aliquam vestibulum, lectus tortor imperdiet dolor, a blandit sapien nisi vitae metus.
"""

class ScrollingText:
    def __init__(self, root):
        self.root = root
        self.y_position = root.winfo_screenheight()

        # Configure dark mode
        self.root.configure(bg="black")

        # Create canvas for scrolling content
        self.canvas = tk.Canvas(root, width=800, height=600, bg="black", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # Add content to the canvas
        self.text_id = self.canvas.create_text(
            50, self.y_position,  # Left-aligned margin (X=50)
            text=content,
            font=("Courier", 12), 
            fill="white", 
            anchor="nw",  # Align text to the top-left corner
            justify="left"  # Left-aligned text within the bounding box
        )

        # Begin animation
        self.animate()

    def animate(self):
        # Scroll content upward
        self.y_position -= 2  # Adjust scrolling speed here
        self.canvas.coords(self.text_id, 100, self.y_position)

        # Reset position for continuous scrolling
        if self.y_position < -self.canvas.bbox(self.text_id)[3]:
            self.y_position = self.root.winfo_screenheight()

        # Schedule the next frame
        self.root.after(50, self.animate)

# Initialize the application window
root = tk.Tk()
root.geometry("800x600")
root.title("Scrolling Text")

# Start the scrolling text application
app = ScrollingText(root)

# Run the main event loop
root.mainloop()
