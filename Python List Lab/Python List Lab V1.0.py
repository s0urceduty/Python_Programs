# Python List Lab V1.0
# Developed to teach and learn how to create and control lists using Python.
# Copyright (C) 2024, Sourceduty - All Rights Reserved.

import tkinter as tk
from tkinter import messagebox
import random

def add_item():
    item = entry.get()
    if item:
        listbox.insert(tk.END, item)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter an item.")

def remove_selected_item():
    try:
        selected_index = listbox.curselection()[0]
        listbox.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select an item to remove.")

def measure_length():
    length = listbox.size()
    messagebox.showinfo("List Length", f"Number of items in the list: {length}")

def sort_list():
    items = list(listbox.get(0, tk.END))
    items.sort()
    listbox.delete(0, tk.END)
    for item in items:
        listbox.insert(tk.END, item)

def clear_list():
    listbox.delete(0, tk.END)

def reverse_list():
    items = list(listbox.get(0, tk.END))
    items.reverse()
    listbox.delete(0, tk.END)
    for item in items:
        listbox.insert(tk.END, item)

def count_item_occurrences():
    item = entry.get()
    if item:
        occurrences = listbox.get(0, tk.END).count(item)
        messagebox.showinfo("Item Occurrences", f"'{item}' occurs {occurrences} times in the list.")
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter an item to count.")

def find_item_index():
    item = entry.get()
    if item:
        try:
            index = listbox.get(0, tk.END).index(item)
            messagebox.showinfo("Item Index", f"The first occurrence of '{item}' is at index {index}.")
        except ValueError:
            messagebox.showinfo("Item Index", f"'{item}' is not in the list.")
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter an item to find.")

def remove_by_value():
    item = entry.get()
    if item:
        try:
            index = listbox.get(0, tk.END).index(item)
            listbox.delete(index)
        except ValueError:
            messagebox.showwarning("Warning", f"'{item}' is not in the list.")
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter an item to remove.")

def duplicate_item():
    try:
        selected_index = listbox.curselection()[0]
        item = listbox.get(selected_index)
        listbox.insert(tk.END, item)
    except IndexError:
        messagebox.showwarning("Warning", "Please select an item to duplicate.")

def move_item_up():
    try:
        selected_index = listbox.curselection()[0]
        if selected_index > 0:
            item = listbox.get(selected_index)
            listbox.delete(selected_index)
            listbox.insert(selected_index-1, item)
            listbox.selection_set(selected_index-1)
    except IndexError:
        messagebox.showwarning("Warning", "Please select an item to move.")

def move_item_down():
    try:
        selected_index = listbox.curselection()[0]
        if selected_index < listbox.size() - 1:
            item = listbox.get(selected_index)
            listbox.delete(selected_index)
            listbox.insert(selected_index+1, item)
            listbox.selection_set(selected_index+1)
    except IndexError:
        messagebox.showwarning("Warning", "Please select an item to move.")

def shuffle_list():
    items = list(listbox.get(0, tk.END))
    random.shuffle(items)
    listbox.delete(0, tk.END)
    for item in items:
        listbox.insert(tk.END, item)

def extract_even_index_items():
    items = list(listbox.get(0, tk.END))
    even_index_items = [items[i] for i in range(len(items)) if i % 2 == 0]
    messagebox.showinfo("Even Index Items", "\n".join(even_index_items))

def concatenate_items():
    items = list(listbox.get(0, tk.END))
    concatenated = ' '.join(items)
    messagebox.showinfo("Concatenated Items", concatenated)

def load_example():
    examples = [
        ["Apple", "Banana", "Cherry", "Cat", "Dog", "Bird"],
        ["Cat", "Dog", "Bird", "Cat", "Dog", "Bird", "Cat", "Dog", "Bird", "Cat", "Dog", "Bird"],
        ["Apple", "Banana", "Cherry", "Apple", "Banana", "Cherry", "Apple", "Banana", "Cherry", "Apple", "Banana", "Cherry", "Apple", "Banana", "Cherry"]
    ]
    chosen_example = random.choice(examples)
    clear_list()
    for item in chosen_example:
        listbox.insert(tk.END, item)

app = tk.Tk()
app.geometry("800x600")
app.title("Python List Lab")

frame = tk.Frame(app)
frame.pack(side=tk.LEFT, padx=10, pady=10)

buttons = [
    ("Add Item", add_item),
    ("Remove Selected", remove_selected_item),
    ("Measure Length", measure_length),
    ("Sort List", sort_list),
    ("Clear List", clear_list),
    ("Reverse List", reverse_list),
    ("Count Occurrences", count_item_occurrences),
    ("Find Item Index", find_item_index),
    ("Remove by Value", remove_by_value),
    ("Duplicate Item", duplicate_item),
    ("Move Item Up", move_item_up),
    ("Move Item Down", move_item_down),
    ("Shuffle List", shuffle_list),
    ("Extract Even", extract_even_index_items),
    ("Concatenate Items", concatenate_items),
    ("Example", load_example)
]

for (text, function) in buttons:
    button = tk.Button(frame, text=text, command=function)
    button.pack(fill=tk.X)

entry = tk.Entry(app)
entry.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

listbox = tk.Listbox(app, bg='blue', fg='white')  # Set the background color to blue and text color to white
listbox.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

app.mainloop()
