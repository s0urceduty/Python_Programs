Drag and Drop to Folder with Random Naming

Description:

This Python application provides a graphical user interface (GUI) for users to drag and drop files into. Once files are dropped, the application copies these files to a new directory, renaming each file with a unique random alphanumeric string. This utility is useful for managing file organization and ensuring file names are anonymized or standardized without manual effort.

Requirements:

- Python 3.x
- Tkinter
- tkinterdnd2
- secrets
- string

Setup and Installation:

1. Ensure Python 3.x is installed on your system.
2. Install the required Python packages using pip:
   pip install tkinterdnd2
3. Download or clone this repository to your local machine.

Usage Instructions:

1. Run the script using Python:
   python file_organizer.py
2. A window titled "Drag and Drop Files Here" will open. Drag files from your system into this window.
3. The files will be copied to a newly created folder named 'Renamed_Files' in the script's directory. Each file will have a new name consisting of a random 10-character alphanumeric string, preserving the original file extension.
4. Check the 'Renamed_Files' directory to access the copied and renamed files.

Notes:

- The script generates a 10-character random alphanumeric name for each file to ensure uniqueness. Adjust the length of the random string in the script if longer names are required.
- This script does not delete or move the original files; it only creates copies in the specified folder.