#Not_Sure_Slang_Meme_Thesaurus

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
        if word in data:
            txt.delete("1.0", END)
            txt.insert(END, data[word])
        elif word.title() in data:
            txt.delete("1.0", END)
            txt.insert(END, data[word.title()])  
        elif word.upper() in data:
            txt.delete("1.0", END)
            txt.insert(END, data[word.upper()])   
        elif len(get_close_matches(word, data.keys())) > 0:
            getWord = get_close_matches(word, data.keys())[0]
            ask = tkinter.messagebox.askquestion("Word not found", "Trying to search %s? " % getWord)
            if ask == 'yes':
                txt.delete("1.0", END)
                txt.insert(END, data[getWord])
            else:
                tkinter.messagebox.showerror("No such word", "There is no such word as %s " % word)
        else:
            tkinter.messagebox.showerror("No such word", "There is no such word as %s " % word)
            
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
    
window = Tk()

window.configure(bg='#DFDFDF')

window.title("Not Sure Slang Meme Thesaurus")

text=StringVar()
e1 = Entry(window, bd=3, textvariable=text, width=38, fg="#000000", bg='#DFDFDF')
e1.insert(0, "NOT SURE IF...")
e1.bind("<FocusIn>", noClick)
e1.bind("<FocusOut>", onClick)
e1.config(fg = "grey")
e1.grid(row=0, column=0, columnspan=2)

b1 = Button(window, bd=4,  font="Calibri 10", text="Output", width=16, fg="#000000", bg='#FFFC93', command=dictionary)
b1.grid(row=0, column=2)

b2 = Button(window, bd=4, font="Calibri 10", text="Clear", width=15, fg="#000000", bg='#A7EEFF', command=clear)
b2.grid(row=1, column=1)

b3 = Button(window, bd=4, font="Calibri 10", text="Close", width=15, fg="#000000", bg='#A7EEFF', command=close)
b3.grid(row=1, column=0)

txt=Text(window, height=11, width=45, wrap=WORD, fg="#000000", bg='#DFDFDF')
txt.grid(row=2, column=0, rowspan=6, columnspan=3)

sb1=Scrollbar(window)
sb1.grid(row=2, column=3, rowspan=6)

txt.configure(yscrollcommand=sb1.set)
sb1.configure(command=txt.yview)

txt.bind('<<TextSelect>>')

window.mainloop()