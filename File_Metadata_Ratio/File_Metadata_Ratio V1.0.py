import os
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import eyed3

def analyze_mp3_files(files):
    songs_data = []
    for file_path in files:
        if file_path.endswith('.mp3'):
            audiofile = eyed3.load(file_path)
            bit_rate = audiofile.info.bit_rate[1] if audiofile.info.bit_rate else 'Unknown'
            file_size = os.path.getsize(file_path)
            duration = audiofile.info.time_secs if audiofile.info.time_secs else 'Unknown'
            songs_data.append((os.path.basename(file_path), bit_rate, file_size, duration))
    return songs_data

def generate_report(songs_data):
    songs_data.sort(key=lambda x: (-x[1], x[2], -x[3]))
    optimal_song = songs_data[0]
    report = 'Song Optimization Report:\n\n'
    report += '\n'.join([f'{filename}: Bit Rate = {bit_rate} kbps, File Size = {file_size} bytes, Duration = {duration} seconds' for filename, bit_rate, file_size, duration in songs_data])
    report += f'\n\nOptimal Song: {optimal_song[0]}\n'
    return report

def import_files():
    file_paths = filedialog.askopenfilenames(title="Select MP3 Files", filetypes=[("MP3 files", "*.mp3")])
    if file_paths:
        songs_data = analyze_mp3_files(file_paths)
        report = generate_report(songs_data)
        report_text.delete(1.0, tk.END)
        report_text.insert(tk.END, report)

# Set up the GUI
root = tk.Tk()
root.title("MP3 File Optimizer")

# Create a button to import files
import_button = tk.Button(root, text="Import MP3 Files", command=import_files)
import_button.pack()

# Create a scrolled text area to display the report
report_text = scrolledtext.ScrolledText(root, width=100, height=30)
report_text.pack()

# Run the GUI event loop
root.mainloop()
