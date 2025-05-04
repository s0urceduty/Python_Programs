# Text_File_Name_Suggestion
# 📄 File name suggestion for text files.

# Copyright (c) 2023, Sourceduty
# This software is free and open-source; anyone can redistribute it and/or modify it.

import os
import re

def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def suggest_file_name(text):
    # Remove non-alphanumeric characters and spaces from the text
    cleaned_text = re.sub(r'[^a-zA-Z0-9]', ' ', text)
    words = cleaned_text.split()
    # Take the first few words to create the file name suggestion
    suggestion = "_".join(words[:3])
    return suggestion

def main(directory_path):
    if not os.path.exists(directory_path):
        print(f"Directory '{directory_path}' does not exist.")
        return

    for root, _, files in os.walk(directory_path):
        for file_name in files:
            if file_name.endswith('.txt'):
                file_path = os.path.join(root, file_name)
                text = read_text_file(file_path)
                suggestion = suggest_file_name(text)
                print(f"File: {file_name}\nSuggested Name: {suggestion}\n")

if __name__ == "__main__":
    directory_path = "path/to/your/text/files/directory"
    main(directory_path)