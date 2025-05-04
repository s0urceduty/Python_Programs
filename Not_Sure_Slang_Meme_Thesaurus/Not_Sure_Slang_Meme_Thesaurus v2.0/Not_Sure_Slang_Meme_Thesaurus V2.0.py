#Not_Sure_Slang_Meme_Thesaurus V2.0

#Slang word thesaurus designed for assisting the creation of NOT SURE IF memes.

#Copyright (C) 2023,  Sourceduty - All Rights Reserved.
#THE CONTENTS OF THIS PROJECT ARE PROPRIETARY.

from tkinter import *
import json
from difflib import get_close_matches
import tkinter.messagebox

data = json.load(open("data.json"))

word = None

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

def clear():
    e1.delete("0", END)
    txt.delete("1.0", END)

def close():
    get = tkinter.messagebox.askquestion("Exit", "Do you want to exit?")
    if get == 'yes':
        window.destroy()

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

# Buttons
button_frame = Frame(window, bg='#DFDFDF')
button_frame.pack(pady=10)
b1 = Button(button_frame, bd=4,  font="Calibri 12", text="Search", fg="#000000", bg='#FFFC93', command=dictionary)
b1.grid(row=0, column=0, padx=5)
b2 = Button(button_frame, bd=4, font="Calibri 12", text="Clear", fg="#000000", bg='#A7EEFF', command=clear)
b2.grid(row=0, column=1, padx=5)
b3 = Button(button_frame, bd=4, font="Calibri 12", text="Close", fg="#000000", bg='#FF6B6B', command=close)
b3.grid(row=0, column=2, padx=5)

# Output Area
txt=Text(window, height=15, width=60, wrap=WORD, fg="#000000", bg='#DFDFDF')
txt.pack(pady=20)

window.mainloop()
window.mainloop()
