# 3D Model STL File Database Manager V1.0
# Copyright (C) 2024, Sourceduty - All Rights Reserved.

import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import os
import sqlite3
import trimesh
import csv
from datetime import datetime

# Initialize the main application window
root = tk.Tk()
root.title("STL File Database Manager")
root.geometry("800x600")
root.configure(bg='#2e2e2e')

# In-memory storage of STL records
stl_records = []

# Database Initialization
def init_db():
    conn = sqlite3.connect('stl_files.db')
    cursor = conn.cursor()
    # Create the table if it does not exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS stl_files (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        file_name TEXT NOT NULL,
                        file_path TEXT NOT NULL,
                        file_size INTEGER,
                        vertex_count INTEGER,
                        volume REAL,
                        model_dimension TEXT,
                        modification_date TEXT,
                        note TEXT,
                        date_added TEXT)''')
    # Alter table to add missing columns if they do not exist
    try:
        cursor.execute('ALTER TABLE stl_files ADD COLUMN vertex_count INTEGER')
    except sqlite3.OperationalError:
        pass  # Column already exists

    try:
        cursor.execute('ALTER TABLE stl_files ADD COLUMN volume REAL')
    except sqlite3.OperationalError:
        pass  # Column already exists

    try:
        cursor.execute('ALTER TABLE stl_files ADD COLUMN modification_date TEXT')
    except sqlite3.OperationalError:
        pass  # Column already exists

    try:
        cursor.execute('ALTER TABLE stl_files ADD COLUMN note TEXT')
    except sqlite3.OperationalError:
        pass  # Column already exists

    conn.commit()
    conn.close()

init_db()

# Database Operations
def add_to_db(file_name, file_path, file_size, vertex_count, volume, model_dimension, modification_date, note):
    conn = sqlite3.connect('stl_files.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO stl_files (file_name, file_path, file_size, vertex_count, volume, model_dimension, modification_date, note, date_added)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, datetime('now'))''',
                   (file_name, file_path, file_size, vertex_count, volume, model_dimension, modification_date, note))
    conn.commit()
    conn.close()

def fetch_from_db():
    conn = sqlite3.connect('stl_files.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, file_name, file_path, file_size, vertex_count, volume, model_dimension, modification_date, note FROM stl_files')
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_from_db(file_ids):
    conn = sqlite3.connect('stl_files.db')
    cursor = conn.cursor()
    cursor.executemany('DELETE FROM stl_files WHERE id=?', [(file_id,) for file_id in file_ids])
    conn.commit()
    conn.close()

def export_to_csv():
    rows = fetch_from_db()
    if rows:
        file_path = filedialog.asksaveasfilename(defaultextension=".csv",
                                                 filetypes=[("CSV files", "*.csv")])
        if file_path:
            with open(file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['ID', 'File Name', 'File Path', 'File Size', 'Vertex Count', 'Volume', 'Model Dimension', 'Modification Date', 'Note', 'Date Added'])
                writer.writerows(rows)
            messagebox.showinfo("Export", "Database successfully exported to CSV")
    else:
        messagebox.showwarning("Export", "No data to export")

def add_note_to_db(file_id, note):
    conn = sqlite3.connect('stl_files.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE stl_files SET note=? WHERE id=?', (note, file_id))
    conn.commit()
    conn.close()

# STL File Handling
def import_stl():
    file_paths = filedialog.askopenfilenames(filetypes=[("STL files", "*.stl")])
    if file_paths:
        for file_path in file_paths:
            file_name = os.path.basename(file_path)
            file_size = os.path.getsize(file_path)
            mesh = trimesh.load(file_path)
            vertex_count = len(mesh.vertices)
            volume = mesh.volume
            model_dimension = str(mesh.extents)  # Get the model dimensions
            modification_time = os.path.getmtime(file_path)
            modification_date = datetime.fromtimestamp(modification_time).strftime('%Y-%m-%d %H:%M:%S')
            note = ""
            add_to_db(file_name, file_path, file_size, vertex_count, volume, model_dimension, modification_date, note)
            stl_records.append((file_name, file_path, file_size, vertex_count, volume, model_dimension, modification_date, note))
        display_files()
        update_footer()

def display_files():
    # Clear existing items in the display
    listbox.delete(0, tk.END)
    rows = fetch_from_db()
    for row in rows:
        # Check if volume is None and handle it
        volume = row[5] if row[5] is not None else 0.0
        listbox.insert(tk.END, f"ID: {row[0]} | Name: {row[1]} | Size: {row[3]} bytes | Vertices: {row[4]} | Volume: {volume:.2f} | Dimensions: {row[6]} | Modified: {row[7]} | Note: {row[8]}")

# Update footer with database statistics
def update_footer():
    rows = fetch_from_db()
    total_files = len(rows)
    total_size = sum(row[3] for row in rows)
    footer_label.config(text=f"Total Files: {total_files} | Total Size: {total_size} bytes")

# Function to add a note to the selected STL record
def add_note():
    selected = listbox.curselection()
    if selected:
        file_id = fetch_from_db()[selected[0]][0]
        note = simpledialog.askstring("Add Note", "Enter a note for this file:")
        if note:
            add_note_to_db(file_id, note)
            display_files()

# Create title bar with database controls
title_bar = tk.Frame(root, bg='#1f1f1f', relief='raised', bd=2)
title_bar.pack(fill=tk.X)

add_button = tk.Button(title_bar, text="Add STL", command=import_stl, bg='#3e3e3e', fg='white')
add_button.pack(side=tk.LEFT)

delete_button = tk.Button(title_bar, text="Delete STL", command=lambda: delete_selected(), bg='#3e3e3e', fg='white')
delete_button.pack(side=tk.LEFT)

export_button = tk.Button(title_bar, text="Export to CSV", command=export_to_csv, bg='#3e3e3e', fg='white')
export_button.pack(side=tk.LEFT)

note_button = tk.Button(title_bar, text="Add Note", command=add_note, bg='#3e3e3e', fg='white')
note_button.pack(side=tk.LEFT)

# Function to delete the selected STL(s) from the database
def delete_selected():
    selected = listbox.curselection()
    if selected:
        file_ids = [fetch_from_db()[index][0] for index in selected]
        delete_from_db(file_ids)
        display_files()
        update_footer()

# Listbox to display STL file details
listbox = tk.Listbox(root, bg='#2e2e2e', fg='white', selectbackground='#3e3e3e', selectmode=tk.MULTIPLE)
listbox.pack(fill=tk.BOTH, expand=True)
display_files()  # Initial display of files

# Thick footer for database statistics
footer = tk.Frame(root, bg='#1f1f1f', height=30)
footer.pack(fill=tk.X, side=tk.BOTTOM)
footer_label = tk.Label(footer, text="", bg='#1f1f1f', fg='white')
footer_label.pack()
update_footer()

# Start the main event loop
root.mainloop()
