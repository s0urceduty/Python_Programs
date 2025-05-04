import tkinter as tk
import datetime
import psutil

def get_boot_time():
    boot_time_timestamp = psutil.boot_time()
    boot_time = datetime.datetime.fromtimestamp(boot_time_timestamp)
    return boot_time

def update_clock():
    current_time = datetime.datetime.now()
    uptime = current_time - boot_time
    uptime_str = str(uptime).split('.')[0]  # To display uptime without microseconds
    clock_label.config(text='Current uptime: ' + uptime_str)
    root.after(1000, update_clock)  # Refresh the label every 1000 ms

boot_time = get_boot_time()

root = tk.Tk()
root.title('System Uptime Monitor')

clock_label = tk.Label(root, text='', font=('Helvetica', 16))
clock_label.pack(pady=20)

update_clock()  # Initialize clock updating

root.mainloop()
