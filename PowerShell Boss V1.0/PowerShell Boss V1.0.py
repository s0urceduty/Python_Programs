# Powershell Boss V1.0
# GUI for Powershell and it's features.

import tkinter as tk
from tkinter import scrolledtext
import subprocess
import threading

# Global variable to keep track of the PowerShell process
powershell_process = None

# Function to execute PowerShell command and display output in the log area
def run_command(command):
    if powershell_process is None:
        try:
            log_text.config(state='normal')
            log_text.insert(tk.END, f"Running command: {command}\n")
            log_text.see(tk.END)
            log_text.config(state='disabled')
            
            result = subprocess.run(['powershell', '-Command', command], capture_output=True, text=True, shell=True)
            
            log_text.config(state='normal')
            log_text.insert(tk.END, result.stdout.strip() + "\n")
            if result.stderr:
                log_text.insert(tk.END, f"Error: {result.stderr.strip()}\n")
            log_text.see(tk.END)
            log_text.config(state='disabled')
        except Exception as e:
            log_text.config(state='normal')
            log_text.insert(tk.END, f"Error: {str(e)}\n")
            log_text.see(tk.END)
            log_text.config(state='disabled')

# Function to display a comprehensive help menu
def display_help_menu():
    help_text = """
PowerShell Help Menu:

A
- Get-Acl: Get permission settings for a file or registry key.
- Set-Acl: Set permissions.
- Get-Alias: Return alias names for Cmdlets.
- Set-Alias: Create or change an alias.
- Get-AppxPackage: List the app packages installed in a user profile.
- Remove-AppxPackage: Remove an app package from a user account.

B
- Backup-GPO: Backup group policy objects (GPOs).
- Enable-BitLocker: Enable encryption for a BitLocker volume.
- Get-BitLockerVolume: Get information about volumes BitLocker can protect.
- Disable-BitLocker: Disable encryption for a BitLocker volume.

C
- Get-ChildItem: Get child items (contents of a folder or registry key).
- Clear-Host: Clear the screen.
- Copy-Item: Copy an item from a namespace location.

D
- Get-Date: Get current date and time.
- Get-Disk: Get information about disks visible to the OS.
- Clear-Disk: Remove all partition information and uninitialize a disk.

E
- Get-EventLog: Get event log data.
- Get-WinEvent: Get event log data (Vista+).
- Export-Csv: Export objects to a CSV file.

F
- Format-Table: Format output as a table.
- Format-List: Format output as a list of properties, each on a new line.
- ForEach-Object: Loop through each item in the pipeline.

G
- Get-Process: Get information about processes running on the system.
- Get-Service: Get a list of services installed on the system.
- Get-Command: Retrieve basic information about a command.

H
- Get-Help: Display help about commands and cmdlets.
- Get-History: Get a listing of the session history.
- Get-Host: Get host information (e.g., PowerShell version).

I
- Invoke-Command: Run commands on local or remote computers.
- Import-Module: Add a module to the current session.
- Invoke-RestMethod: Send an HTTP/HTTPS request to a RESTful web service.

J
- Get-Job: Retrieve PowerShell background jobs that are running.
- Start-Job: Start a background job.
- Stop-Job: Stop a PowerShell background job.

K
- Stop-Process: Stop a running process.
- Kill: Alias for Stop-Process.

L
- Get-LocalUser: Retrieve information about local user accounts.
- Set-Location: Set the current working directory.
- Get-Location: Display the current directory.

M
- Get-Module: Retrieve a list of modules imported in the current session.
- Move-Item: Move an item from one location to another.
- Measure-Object: Measure properties of objects passed through the pipeline.

N
- Get-NetAdapter: Retrieve basic network adapter properties.
- Test-NetConnection: Display diagnostic information for a connection.
- New-Item: Create a new item (file, directory, etc.).

O
- Out-File: Send output to a file.
- Out-Host: Send output to the host.
- Out-Null: Discard the output (redirect to null).

P
- Get-Partition: Get information about disk partitions.
- Get-Package: Retrieve a list of software packages installed.
- Push-Location: Push a location to the stack.

R
- Restart-Computer: Restart the operating system on a computer.
- Remove-Item: Delete an item.
- Read-Host: Read input from the host console.

S
- Set-Service: Change service properties.
- Start-Service: Start a stopped service.
- Stop-Service: Stop a running service.

T
- Test-Connection: Send a ping request.
- Get-TimeZone: Get the current system time zone.
- Start-Transaction: Start a new transaction.

U
- Get-Unique: Get unique items in a collection.
- Update-Help: Update PowerShell help files.
- Unblock-File: Unblock files downloaded from the internet.

V
- Get-Volume: Retrieve information about storage volumes.
- Get-VpnConnection: Retrieve VPN connection profile information.
- Set-Variable: Set a value for a variable.

W
- Get-WindowsFeature: Retrieve roles and features.
- Set-WinSystemLocale: Set the system locale for the computer.
- Write-Output: Write an object to the pipeline.

Use "Get-Help <command>" for detailed information on any command.
    """
    log_text.config(state='normal')
    log_text.delete(1.0, tk.END)
    log_text.insert(tk.END, help_text.strip())
    log_text.see(tk.END)
    log_text.config(state='disabled')

# Function to clear the text area
def clear_text_area():
    log_text.config(state='normal')
    log_text.delete(1.0, tk.END)
    log_text.config(state='disabled')

# Function to start the PowerShell terminal
def start_terminal():
    global powershell_process
    if powershell_process is None:
        log_text.config(state='normal')
        log_text.delete(1.0, tk.END)
        log_text.insert(tk.END, "PowerShell terminal started. Enter commands below.\n")
        log_text.config(state='disabled')
        
        powershell_process = subprocess.Popen(
            ['powershell', '-NoExit', '-Command', '-'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            shell=True
        )
        threading.Thread(target=read_output, daemon=True).start()

# Function to read output from the PowerShell process and display it in the text area
def read_output():
    global powershell_process
    while powershell_process:
        output = powershell_process.stdout.readline()
        if output:
            log_text.config(state='normal')
            log_text.insert(tk.END, output)
            log_text.see(tk.END)
            log_text.config(state='disabled')

# Function to send input to the PowerShell terminal
def send_command(event):
    global powershell_process
    if powershell_process:
        command = entry.get()
        if command.strip() != "":
            powershell_process.stdin.write(command + "\n")
            powershell_process.stdin.flush()
            entry.delete(0, tk.END)

# List of top 10 PowerShell commands
powershell_commands = [
    'Get-Process', 'Get-Service', 'Get-EventLog -LogName System',
    'Get-Command', 'Get-ChildItem', 'Get-PSDrive -PSProvider FileSystem',
    'Get-NetIPConfiguration', 'Get-WmiObject Win32_OperatingSystem',
    'Test-Connection', 'Get-Disk'
]

# Create the main window
window = tk.Tk()
window.title("PowerShell Boss V1.0")

# Apply dark mode theme
window.configure(bg='#2e2e2e')

# Frame for buttons (on the left side)
button_frame = tk.Frame(window, bg='#2e2e2e')
button_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.Y)

# Dynamically create buttons for each PowerShell command
for command in powershell_commands:
    button = tk.Button(button_frame, text=command, command=lambda c=command: run_command(c), bg='#3c3f41', fg='#ffffff', bd=0, relief='flat')
    button.pack(fill=tk.X, pady=5)

# Add a Help button that displays the help menu (styled in red)
help_button = tk.Button(button_frame, text="Help", command=display_help_menu, bg='#ff4040', fg='#ffffff', bd=0, relief='flat')
help_button.pack(fill=tk.X, pady=5)

# Add a Clear button to clear the text area (styled in blue)
clear_button = tk.Button(button_frame, text="Clear", command=clear_text_area, bg='#4040ff', fg='#ffffff', bd=0, relief='flat')
clear_button.pack(fill=tk.X, pady=5)

# Add a Start Terminal button (styled in red)
terminal_button = tk.Button(button_frame, text="Start Terminal", command=start_terminal, bg='#ff4040', fg='#ffffff', bd=0, relief='flat')
terminal_button.pack(fill=tk.X, pady=5)

# Log area for output and terminal (single text area)
log_text = scrolledtext.ScrolledText(window, width=80, height=20, wrap=tk.WORD, bg='#1e1e1e', fg='#00ff00', insertbackground='white', font=("Courier", 10))
log_text.pack(fill=tk.BOTH, padx=10, pady=10, expand=True)
log_text.tag_configure("left", lmargin1=0, lmargin2=0)
log_text.config(state='disabled')

# Entry box for typing commands in the terminal
entry = tk.Entry(window, bg='#1e1e1e', fg='#00ff00', insertbackground='white', font=("Courier", 10))
entry.pack(fill=tk.X, padx=10, pady=5)
entry.bind('<Return>', send_command)

# Start the GUI event loop
window.mainloop()
