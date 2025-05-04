import tkinter as tk
from tkinter import messagebox
import psutil
import matplotlib.pyplot as plt

def get_drive_info():
    drives = psutil.disk_partitions()
    drive_info = []
    for drive in drives:
        # Filtering only for drives with drive letters
        if 'cdrom' in drive.opts or drive.fstype == '':
            continue  # Skip cdrom drives and drives without a filesystem
        usage = psutil.disk_usage(drive.mountpoint)
        drive_info.append({
            'Drive': drive.device,
            'Mountpoint': drive.mountpoint,
            'File system type': drive.fstype,
            'Total space': usage.total,
            'Used space': usage.used,
            'Free space': usage.free,
            'Percentage used': usage.percent
        })
    return drive_info

def display_drive_info():
    drive_info = get_drive_info()
    info_str = ""
    for drive in drive_info:
        for key, value in drive.items():
            info_str += f"{key}: {value}\n"
        info_str += "\n"
    messagebox.showinfo("Drive Info", info_str)

def display_drive_chart():
    drive_info = get_drive_info()
    for drive in drive_info:
        labels = 'Used Space', 'Free Space'
        sizes = [drive['Used space'], drive['Free space']]
        colors = ['#ff9999','#66b3ff']
        explode = (0.1, 0)  # explode the 1st slice (Used Space)

        plt.figure(figsize=(6, 6))
        plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
                shadow=True, startangle=140)
        plt.title(f"Drive {drive['Drive']} Usage")
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.show()

# GUI Setup
root = tk.Tk()
root.title("Drive Storage Space Visualizer")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

label = tk.Label(frame, text="Drive Storage Space Visualizer", font=("Arial", 16))
label.pack(pady=10)

button_info = tk.Button(frame, text="Show Drive Info", command=display_drive_info, width=20)
button_info.pack(pady=10)

button_chart = tk.Button(frame, text="Show Drive Chart", command=display_drive_chart, width=20)
button_chart.pack(pady=10)

exit_button = tk.Button(frame, text="Exit", command=root.quit, width=20)
exit_button.pack(pady=10)

root.mainloop()
