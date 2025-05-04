# Music_BPM_Mp3

# ♫ Estimate the BPM of an MP3.

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
file_path = os.path.join(script_directory, 'example.mp3')

bpm = get_bpm_from_mp3(file_path)

# Extract song title from the file name
song_title = os.path.basename(file_path).replace('.mp3', '')

# Save the song title and BPM to BPM.txt
with open(os.path.join(script_directory, 'BPM.txt'), 'w') as f:
    f.write(f"Song Title: {song_title}\nBPM: {bpm:.2f}")

print(f"BPM for '{song_title}': {bpm:.2f}")
print("BPM saved to BPM.txt.")
