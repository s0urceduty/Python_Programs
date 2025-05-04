#Not_Sure_Slang_Meme_Thesaurus V2.6

#Slang word thesaurus designed for assisting the creation of NOT SURE IF memes.

#Copyright (C) 2023,  Sourceduty - All Rights Reserved.
#THE CONTENTS OF THIS PROJECT ARE PROPRIETARY.

from tkinter import *
import json
from difflib import get_close_matches
import tkinter.messagebox
from PIL import Image, ImageDraw, ImageFont
import os

# Load the data
data = json.load(open("data.json"))

word = None

# Function to generate meme image
def generate_meme(input_text, output_text):
    # Load the image
    img = Image.open("blank_meme.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("impact.ttf", 130)
    
    # Top text
    top_text = "NOT SURE IF " + input_text.upper()
    width, height = draw.textsize(top_text, font=font)
    position = ((img.width - width) / 2, 10)
    draw.text(position, top_text, (255, 255, 255), font=font, stroke_width=3, stroke_fill="black")
    
    # Bottom text
    bottom_text = "OR " + output_text.upper()
    width, height = draw.textsize(bottom_text, font=font)
    position = ((img.width - width) / 2, img.height - height - 10)
    draw.text(position, bottom_text, (255, 255, 255), font=font, stroke_width=3, stroke_fill="black")
    
    # Save the image
    img.save("meme_output.png")
    tkinter.messagebox.showinfo("Success", "Meme image saved as 'meme_output.png' in the script's directory.")

def dictionary():
    global word
    word = e1.get()
    word = word.lower()
    if len(e1.get()) == 0:
        tkinter.messagebox.showinfo("Empty", "Enter word")
    elif e1.get() == 'NOT SURE IF...':
        tkinter.messagebox.showinfo("Empty", "Enter word")
    else:
        output = None
        if word in data:
            output = ', '.join(data[word])
        elif word.title() in data:
            output = ', '.join(data[word.title()])
        elif word.upper() in data:
            output = ', '.join(data[word.upper()])
        elif len(get_close_matches(word, data.keys())) > 0:
            getWord = get_close_matches(word, data.keys())[0]
            ask = tkinter.messagebox.askquestion("Word not found", "Trying to search %s? " % getWord)
            if ask == 'yes':
                output = ', '.join(data[getWord])
            else:
                tkinter.messagebox.showerror("No such word", "There is no such word as %s " % word)
        else:
            tkinter.messagebox.showerror("No such word", "There is no such word as %s " % word)
        if output:
            txt.delete("1.0", END)
            txt.insert(END, output)

def noClick(event):
    if e1.get() == "NOT SURE IF...":
       e1.delete(0, "end")
       e1.insert(0, "")
       e1.config(fg="#000000")

def onClick(event):
    if e1.get() == "":
        e1.insert(0, "NOT SURE IF...")
        e1.config(fg = "grey")

def noClickOutput(event):
    if e2.get() == "OR...":
       e2.delete(0, "end")
       e2.insert(0, "")
       e2.config(fg="#000000")

def onClickOutput(event):
    if e2.get() == "":
        e2.insert(0, "OR...")
        e2.config(fg = "grey")

def clear():
    e1.delete("0", END)
    txt.delete("1.0", END)

def close():
    get = tkinter.messagebox.askquestion("Exit", "Do you want to exit?")
    if get == 'yes':
        window.destroy()

def make_meme():
    input_text = e1.get()
    output_text = e2.get().strip()  # Get value from the new Entry widget
    if input_text and output_text:
        generate_meme(input_text, output_text)
    else:
        tkinter.messagebox.showerror("Error", "Please provide input and get output before generating meme.")

# Create the main window
window = Tk()
window.configure(bg='#DFDFDF')
window.title("Not Sure Slang Meme Thesaurus")

# Header
header = Label(window, text="Not Sure Slang Meme Thesaurus", font=('Arial', 16), bg='#DFDFDF')
header.pack(pady=20)

text=StringVar()
e1 = Entry(window, bd=3, textvariable=text, width=50, fg="#000000", bg='#DFDFDF')
e1.insert(0, "NOT SURE IF...")
e1.bind("<FocusIn>", noClick)
e1.bind("<FocusOut>", onClick)
e1.config(fg = "grey")
e1.pack(pady=10)

# New Entry widget for output_text
output_text_var = StringVar()
e2 = Entry(window, bd=3, textvariable=output_text_var, width=50, fg="#000000", bg='#DFDFDF')
e2.insert(0, "OR...")
e2.bind("<FocusIn>", noClickOutput)
e2.bind("<FocusOut>", onClickOutput)
e2.config(fg = "grey")
e2.pack(pady=10)

# Buttons
button_frame = Frame(window, bg='#DFDFDF')
button_frame.pack(pady=10)
b1 = Button(button_frame, bd=4,  font="Calibri 12", text="Search", fg="#000000", bg='#FFFC93', command=dictionary)
b1.grid(row=0, column=0, padx=5)
b4 = Button(button_frame, bd=4,  font="Calibri 12", text="Make", fg="#000000", bg='#FFD700', command=make_meme)
b4.grid(row=0, column=1, padx=5)
b2 = Button(button_frame, bd=4, font="Calibri 12", text="Clear", fg="#000000", bg='#A7EEFF', command=clear)
b2.grid(row=0, column=2, padx=5)
b3 = Button(button_frame, bd=4, font="Calibri 12", text="Close", fg="#000000", bg='#FF6B6B', command=close)
b3.grid(row=0, column=3, padx=5)

# Output Area
txt=Text(window, height=15, width=60, wrap=WORD, fg="#000000", bg='#DFDFDF')
txt.pack(pady=20)

window.mainloop()
