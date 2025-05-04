# Mouse_Pointer_Circle

# 🖱 Move the mouse cursor in a circle with CRTL + 1 keys.
# When CRTL + 1 is pressed the mouse cursor moves in a circle around its last position three times.

# pip install pyautogui keyboard

# Copyright (C) 2023, Sourceduty - All Rights Reserved.
# THE CONTENTS OF THIS PROJECT ARE PROPRIETARY.

import pyautogui
import keyboard
import math
import time

# Function to move the mouse cursor in a circular path around last known position
def move_in_circle_around_last_position(radius, speed, duration, circles):
    last_position = pyautogui.position()
    for _ in range(circles):
        start_time = time.time()
        while time.time() - start_time < duration:
            angle = (time.time() - start_time) * speed
            x = last_position[0] + radius * math.cos(angle)
            y = last_position[1] + radius * math.sin(angle)
            pyautogui.moveTo(x, y, duration=0.1)

# Function to check if Ctrl + 1 is pressed
def is_ctrl_1_pressed(e):
    return keyboard.is_pressed("ctrl+1")

if __name__ == "__main__":
    print("Press Ctrl + 1 to move the mouse cursor in a circle around its last known position three times.")
    
    while True:
        if is_ctrl_1_pressed(None):
            radius = 150  # You can adjust the radius as per your preference
            speed = 1.5  # Adjust the speed to control the cursor movement
            duration = 5  # Total duration for each circle
            circles = 3  # Number of circles to complete

            move_in_circle_around_last_position(radius, speed, duration, circles)
