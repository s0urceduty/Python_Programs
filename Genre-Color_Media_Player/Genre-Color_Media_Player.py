# Genre-Color_Media_Player
# Copyright (C) 2024, Sourceduty - All Rights Reserved.

import os
import tkinter as tk
from tkinter import filedialog, Scrollbar
import pygame
from mutagen import File as MutagenFile
from mutagen.id3 import ID3
from mutagen.mp3 import MP3
import random
from PIL import Image, ImageTk

GENRE_COLORS = {
    'rock': "#8B0000",
    'pop': "#FF69B4",
    'jazz': "#9370DB",
    'classical': "#FFFFE0",
    'electronic': "#00CED1",
    'hip-hop': "#FF6347",
    'country': "#FFA07A",
    'blues': "#4682B4",
    'metal': "#8B0000",
    'reggae': "#32CD32",
    'folk': "#DEB887",
    'soul': "#FFD700",
    'punk': "#FF0000",
    'rnb': "#9400D3",
    'alternative': "#7B68EE",
    'indie': "#00BFFF",
    'funk': "#8A2BE2",
    'gospel': "#FF1493",
    'disco': "#FFFF00",
    'new-age': "#98FB98",
    'ambient': "#8B4513",
    'default': "#C8C8C8"
}

class VLCClone(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Genre-Color_Media_Player")
        self.geometry("800x600")
        self.configure(bg=GENRE_COLORS['default'])

        pygame.mixer.init()

        self.logo_image = Image.open("logo.png")
        self.logo_image = self.logo_image.resize((50, 50))
        self.logo_tk = ImageTk.PhotoImage(self.logo_image)

        header_frame = tk.Frame(self, bg=GENRE_COLORS['default'])
        header_frame.pack(pady=10)

        logo_label = tk.Label(header_frame, image=self.logo_tk, bg=GENRE_COLORS['default'])
        logo_label.grid(row=0, column=0, padx=10)

        title_label = tk.Label(header_frame, text="Genre-Color_Media_Player", font=("Helvetica", 16, "bold"), bg=GENRE_COLORS['default'])
        title_label.grid(row=0, column=1, padx=10)

        list_frame = tk.Frame(self)
        list_frame.pack(pady=20, fill=tk.BOTH, expand=True)

        scrollbar = Scrollbar(list_frame, orient=tk.VERTICAL)
        self.song_list = tk.Listbox(list_frame, selectmode=tk.SINGLE, yscrollcommand=scrollbar.set, bg="black", fg="white", height=10, font=("Courier", 10))
        self.song_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        scrollbar.config(command=self.song_list.yview)

        self.song_list.bind('<Double-1>', self.song_selected)

        self.info_label = tk.Label(self, text="Select a song to play", bg=GENRE_COLORS['default'], font=("Helvetica", 12))
        self.info_label.pack(pady=10)

        controls_frame = tk.Frame(self, bg='grey')
        controls_frame.pack(pady=20)

        self.open_file_button = tk.Button(controls_frame, text="Open Music File", command=self.open_file, width=15)
        self.open_file_button.grid(row=0, column=0, padx=10)

        self.open_folder_button = tk.Button(controls_frame, text="Open Music Folder", command=self.open_folder, width=15)
        self.open_folder_button.grid(row=0, column=1, padx=10)

        self.play_button = tk.Button(controls_frame, text="Play", command=self.play_music, width=10)
        self.play_button.grid(row=0, column=2, padx=10)

        self.pause_button = tk.Button(controls_frame, text="Pause", command=self.pause_music, width=10)
        self.pause_button.grid(row=0, column=3, padx=10)

        self.stop_button = tk.Button(controls_frame, text="Stop", command=self.stop_music, width=10)
        self.stop_button.grid(row=0, column=4, padx=10)

        self.volume_label = tk.Label(controls_frame, text="Volume", bg='grey', font=("Helvetica", 10))
        self.volume_label.grid(row=0, column=5, padx=10)

        self.volume_slider = tk.Scale(controls_frame, from_=0, to=100, orient=tk.HORIZONTAL, command=self.change_volume)
        self.volume_slider.set(100)
        self.volume_slider.grid(row=0, column=6, padx=10)

        self.current_file_path = None
        self.song_paths = {}

        self.song_list.insert(tk.END, f"{'Title':<30} {'Genre':<15} {'Band':<20} {'Duration'}")

    def open_file(self):
        file_path = filedialog.askopenfilename(title="Open Music File", filetypes=[("Audio Files", "*.mp3 *.wav")])

        if file_path:
            self.add_song_to_list(file_path)

    def open_folder(self):
        folder_path = filedialog.askdirectory(title="Open Music Folder")

        if folder_path:
            for root, dirs, files in os.walk(folder_path):
                for file_name in files:
                    if file_name.endswith((".mp3", ".wav")):
                        file_path = os.path.join(root, file_name)
                        self.add_song_to_list(file_path)

    def add_song_to_list(self, file_path):
        song_info = self.extract_song_info(file_path)
        song_title = song_info['title'][:30]
        song_genre = song_info['genre'][:15]
        song_band = song_info['band'][:20]
        song_duration = song_info['duration']
        
        formatted_song = f"{song_title:<30} {song_genre:<15} {song_band:<20} {song_duration}"
        song_index = self.song_list.size()
        self.song_list.insert(tk.END, formatted_song)
        
        self.song_paths[song_index] = file_path

    def extract_song_info(self, file_path):
        song_info = {
            'title': os.path.basename(file_path),
            'genre': 'Unknown',
            'band': 'Unknown',
            'duration': '00:00'
        }

        try:
            audio_file = MutagenFile(file_path, easy=True)
            if audio_file is not None:
                if 'genre' in audio_file:
                    song_info['genre'] = audio_file['genre'][0]

                if 'artist' in audio_file:
                    song_info['band'] = audio_file['artist'][0]

                if isinstance(audio_file, MP3):
                    song_info['duration'] = self.format_duration(audio_file.info.length)
        except Exception as e:
            print(f"Error extracting metadata: {e}")

        return song_info

    def format_duration(self, seconds):
        minutes = int(seconds // 60)
        seconds = int(seconds % 60)
        return f"{minutes:02}:{seconds:02}"

    def song_selected(self, event):
        selected_index = self.song_list.curselection()
        if selected_index:
            file_path = self.song_paths[selected_index[0]]
            self.current_file_path = file_path
            genre = self.identify_genre(self.current_file_path)
            self.change_color_based_on_genre(genre)
            self.update_info_label(file_path)
            self.play_music()

    def play_music(self):
        if self.current_file_path:
            pygame.mixer.music.stop()
            pygame.mixer.music.load(self.current_file_path)
            pygame.mixer.music.play()

    def pause_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()

    def stop_music(self):
        pygame.mixer.music.stop()

    def change_volume(self, value):
        pygame.mixer.music.set_volume(int(value) / 100)

    def identify_genre(self, file_path):
        try:
            audio_file = MutagenFile(file_path, easy=True)
            if audio_file is not None and 'genre' in audio_file:
                genre = audio_file['genre'][0].lower()
                if any(keyword in genre for keyword in GENRE_COLORS.keys()):
                    return genre
        except Exception as e:
            print(f"Error reading genre metadata: {e}")

        filename = os.path.basename(file_path).lower()
        for keyword in GENRE_COLORS.keys():
            if keyword in filename:
                return keyword

        return 'random'

    def change_color_based_on_genre(self, genre):
        if genre == 'random':
            color = "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        else:
            color = GENRE_COLORS.get(genre, GENRE_COLORS['default'])
        self.configure(bg=color)
        self.info_label.configure(bg=color)

    def update_info_label(self, file_path):
        song_title = os.path.basename(file_path)
        self.info_label.config(text=f"{song_title}", bg=GENRE_COLORS['default'])

if __name__ == "__main__":
    app = VLCClone()
    app.mainloop()
