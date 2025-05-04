# Music_BPM_Mp3_10

# ♫ Estimate the BPM of ten MP3 files.

# Copyright (C) 2023, Sourceduty - All Rights Reserved.
# THE CONTENTS OF THIS PROJECT ARE PROPRIETARY.

import librosa
import numpy as np
import os

def get_bpm_from_mp3(file_path):
    # Load the MP3 file using librosa
    y, sr = librosa.load(file_path, sr=None)
    
    # Estimate the tempo (BPM)
    onset_env = librosa.onset.onset_strength(y=y, sr=sr)
    bpm, _ = librosa.beat.beat_track(onset_envelope=onset_env, sr=sr)
    
    return bpm

# Get the script's directory
script_directory = os.path.dirname(os.path.abspath(__file__))

# Automatically detect up to 10 MP3 files in the directory
mp3_files = [f for f in os.listdir(script_directory) if f.endswith('.mp3')][:10]
if not mp3_files:
    raise ValueError("No MP3 files found in the script's directory.")

with open(os.path.join(script_directory, 'BPM.txt'), 'w') as f:
    for mp3_file in mp3_files:
        file_path = os.path.join(script_directory, mp3_file)
        bpm = get_bpm_from_mp3(file_path)
        song_title = os.path.basename(file_path).replace('.mp3', '')
        f.write(f"Song Title: {song_title}\nBPM: {bpm:.2f}\n\n")
        print(f"BPM for '{song_title}': {bpm:.2f}")

print("BPMs saved to BPM.txt.")
