# Python Slider Lock v1.0

import tkinter as tk
from tkinter import messagebox

# Default combination (to unlock the lock)
default_combination = (1, 2, 3)

# Function to update the sliders
def update_slider_state():
    # Unlock the second slider when the first slider reaches 1
    if slider1.get() == default_combination[0]:
        slider2.config(state="normal")
    else:
        slider2.config(state="disabled")
        slider2.set(default_combination[1])

    # Unlock the third slider when the second slider reaches 2
    if slider2.get() == default_combination[1]:
        slider3.config(state="normal")
    else:
        slider3.config(state="disabled")
        slider3.set(default_combination[2])

    # Unlock the main lock if the third slider reaches 3
    if slider3.get() == default_combination[2]:
        unlock_button.config(state="normal", bg="green")
    else:
        unlock_button.config(state="disabled", bg="red")

# Function to handle the unlock button click
def unlock_combination():
    if (slider1.get(), slider2.get(), slider3.get()) == default_combination:
        # If all sliders match the default combination, the lock is unlocked
        messagebox.showinfo("Unlocked", "The lock is now unlocked!")
        text_area.config(state="normal")
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, "You have successfully unlocked the combination lock!")
        unlock_button.config(state="disabled", bg="green")  # Disable the unlock button after unlocking
    else:
        # If the combination is incorrect
        messagebox.showerror("Incorrect", "Incorrect combination. Try again.")
        text_area.config(state="disabled")

# Function to reset the sliders
def reset_lock():
    # Reset all sliders to 0
    slider1.set(0)  # First slider starts at 0
    slider2.set(0)  # Second slider starts at 0 (disabled initially)
    slider3.set(0)  # Third slider starts at 0 (disabled initially)
    slider2.config(state="disabled")  # Disable second slider
    slider3.config(state="disabled")  # Disable third slider
    unlock_button.config(state="disabled", bg="red")  # Reset unlock button to disabled and red

    # Reset the text area
    text_area.config(state="normal")
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END, f"Default Combination: {default_combination[0]} - {default_combination[1]} - {default_combination[2]}\n")
    text_area.insert(tk.END, "Please unlock the lock by setting each slider to the correct value.")
    text_area.config(state="disabled")

# Create the main window
root = tk.Tk()
root.title("Combination Lock")

# Apply dark mode styling
root.config(bg="#2e2e2e")  # Set the background color of the window
text_area_bg = "#333333"
button_bg = "#4c4c4c"
button_fg = "#ffffff"
slider_bg = "#444444"
label_fg = "#ffffff"

# Add padding above sliders
root.grid_rowconfigure(0, minsize=20)  # Add some space above the sliders

# Create sliders
slider1 = tk.Scale(root, from_=0, to=25, orient="vertical", label="Slider 1", length=300, bg=slider_bg, fg=label_fg)
slider1.grid(row=1, column=0, padx=20)
slider1.set(0)  # Start the first slider at 0

slider2 = tk.Scale(root, from_=0, to=25, orient="vertical", label="Slider 2", length=300, state="disabled", bg=slider_bg, fg=label_fg)
slider2.grid(row=1, column=1, padx=20)
slider2.set(0)  # Start the second slider at 0 (but it is initially disabled)

slider3 = tk.Scale(root, from_=0, to=25, orient="vertical", label="Slider 3", length=300, state="disabled", bg=slider_bg, fg=label_fg)
slider3.grid(row=1, column=2, padx=20)
slider3.set(0)  # Start the third slider at 0 (but it is initially disabled)

# Create a text area for success message and default combination display
text_area = tk.Text(root, height=5, width=40, wrap=tk.WORD, state="disabled", bg=text_area_bg, fg=label_fg)
text_area.grid(row=2, column=0, columnspan=3, pady=10)

# Display the default combination in the text area when the program starts
text_area.config(state="normal")
text_area.insert(tk.END, f"Default Combination: {default_combination[0]} - {default_combination[1]} - {default_combination[2]}\n")
text_area.insert(tk.END, "Please unlock the lock by setting each slider to the correct value.")
text_area.config(state="disabled")

# Create unlock button (disabled initially, red color)
unlock_button = tk.Button(root, text="Unlock", state="disabled", command=unlock_combination, bg="red", fg=button_fg)
unlock_button.grid(row=3, column=0, padx=10, pady=10)

# Create reset button
reset_button = tk.Button(root, text="Reset", command=reset_lock, bg=button_bg, fg=button_fg)
reset_button.grid(row=3, column=1, padx=10, pady=10)

# Center the buttons side-by-side below the text area
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Update the slider states when any slider is changed
slider1.bind("<Motion>", lambda event: update_slider_state())
slider2.bind("<Motion>", lambda event: update_slider_state())
slider3.bind("<Motion>", lambda event: update_slider_state())

# Start the Tkinter event loop
root.mainloop()
