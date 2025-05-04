# YouTube Subtitles to Instructions Converter
# Scrape YouTube how-to video subtitles and create text instructions.
# Copyright (C) 2024, Sourceduty - All Rights Reserved.

# pip install openai pytube youtube-transcript-api

import tkinter as tk
from tkinter import filedialog, scrolledtext, DISABLED, NORMAL
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import SRTFormatter
from pytube import YouTube
import openai
import os

# Set your OpenAI API key here
openai.api_key = 'OpenAI API Key here'

video_links = []
subtitle_texts = {}

def select_file():
    global video_links
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            video_links = [link.strip() for link in file.readlines() if link.strip()]
            progress_display.delete(1.0, tk.END)
            text_display.delete(1.0, tk.END)
            for link in video_links:
                text_display.insert(tk.END, link + "\n")
            update_progress("Video links loaded. Click 'Download Subtitles' to proceed.")
            btn_download.config(state=NORMAL)
            btn_create.config(state=DISABLED)

def download_subtitles():
    global subtitle_texts
    subtitle_texts = {}
    progress_display.delete(1.0, tk.END)
    for link in video_links:
        try:
            video_id = link.split("v=")[-1]
            yt = YouTube(link)
            update_progress(f"Processing: {yt.title}")

            if not os.path.exists('Subtitles'):
                os.makedirs('Subtitles')

            transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
            formatter = SRTFormatter()
            srt_formatted = formatter.format_transcript(transcript)
            
            subtitle_text = '\n'.join([entry['text'] for entry in transcript])
            subtitle_texts[yt.title] = subtitle_text

            subtitle_file_path = os.path.join('Subtitles', f"{yt.title}.srt")
            subtitle_text_path = os.path.join('Subtitles', f"{yt.title}.txt")
            
            with open(subtitle_file_path, 'w', encoding='utf-8') as file:
                file.write(srt_formatted)

            with open(subtitle_text_path, 'w', encoding='utf-8') as file:
                file.write(subtitle_text)

            update_progress(f"Saved subtitles for {yt.title}")
        except Exception as e:
            update_progress(f"Error processing {link}: {e}")
    update_progress("Subtitles downloaded and saved in 'Subtitles' folder. Click 'Create Instructions' to generate instructions.")
    btn_download.config(state=DISABLED)
    btn_create.config(state=NORMAL)

def create_instructions():
    progress_display.delete(1.0, tk.END)
    for title, subtitle_text in subtitle_texts.items():
        try:
            instructions = convert_to_instructions(subtitle_text)
            if not os.path.exists('Instructions'):
                os.makedirs('Instructions')
            instructions_file_path = os.path.join('Instructions', f"{title}_instructions.txt")
            with open(instructions_file_path, 'w', encoding='utf-8') as file:
                file.write(instructions)
            update_progress(f"Saved instructions for {title}")
        except Exception as e:
            update_progress(f"Error generating instructions for {title}: {e}")
    update_progress("Instructions generated and saved in 'Instructions' folder.")
    btn_create.config(state=DISABLED)

def convert_to_instructions(text):
    prompt = (
        "Convert the following text into a detailed step-by-step instruction list. "
        "Each step should be clear, concise, and provide enough detail for someone to follow easily. "
        "Include necessary context, tools, and any warnings if applicable.\n\n"
        f"Text:\n{text}\n\n"
        "Instructions:"
    )
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000  # Increased max_tokens for more detailed instructions
        )
        instructions = response.choices[0].message['content'].strip()
        return instructions
    except Exception as e:
        update_progress(f"Failed to generate instructions: {e}")
        return ""

def clear_texts():
    text_display.delete(1.0, tk.END)
    progress_display.delete(1.0, tk.END)
    btn_select.config(state=NORMAL)
    btn_download.config(state=DISABLED)
    btn_create.config(state=DISABLED)

def update_progress(message):
    progress_display.insert(tk.END, message + "\n")
    progress_display.see(tk.END)

# Initialize the main window
root = tk.Tk()
root.title("YouTube Subtitles to Instructions Converter")
root.geometry("1000x600")

# Create frames for layout
button_frame = tk.Frame(root)
button_frame.pack(fill=tk.X, padx=10, pady=10)

text_frame = tk.Frame(root)
text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10, side=tk.LEFT)

progress_frame = tk.Frame(root)
progress_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Add buttons
btn_select = tk.Button(button_frame, text="Select File", command=select_file)
btn_select.pack(side=tk.LEFT, padx=5)

btn_download = tk.Button(button_frame, text="Download Subtitles", command=download_subtitles, state=DISABLED)
btn_download.pack(side=tk.LEFT, padx=5)

btn_create = tk.Button(button_frame, text="Create Instructions", command=create_instructions, state=DISABLED)
btn_create.pack(side=tk.LEFT, padx=5)

btn_clear = tk.Button(button_frame, text="Clear", command=clear_texts)
btn_clear.pack(side=tk.LEFT, padx=5)

# Add text widget for displaying the text
text_display = scrolledtext.ScrolledText(text_frame, wrap=tk.WORD, height=30)
text_display.pack(fill=tk.BOTH, expand=True)

# Add text widget for displaying the progress
progress_display = scrolledtext.ScrolledText(progress_frame, wrap=tk.WORD, height=30, bg='black', fg='white')
progress_display.pack(fill=tk.BOTH, expand=True)

# Start the main event loop
root.mainloop()
