# CAPTCHA Game V1.0
# Copyright (C) 2024, Sourceduty - All Rights Reserved.

# The first and original CAPTCHA solving Python game. 

import tkinter as tk
from tkinter import simpledialog
import turtle
import random
import string
import time

class CaptchaGame:
    def __init__(self, root):
        self.root = root
        self.root.title("CAPTCHA Game V1.0")
        self.canvas = tk.Canvas(root, width=400, height=300)
        self.canvas.grid(row=0, column=0, columnspan=2, pady=5)

        self.turtle_screen = turtle.TurtleScreen(self.canvas)
        self.turtle_screen.bgcolor("#000000")
        self.t = turtle.RawTurtle(self.turtle_screen)
        self.t.hideturtle()
        self.t.speed(0)

        self.player_name = tk.StringVar()
        self.captcha_input = tk.StringVar()
        self.high_score = float('inf')
        self.games_completed = 0
        self.captcha = ""
        self.high_scores = []

        self.create_widgets()

    def create_widgets(self):
        self.captcha_entry = tk.Entry(self.root, textvariable=self.captcha_input, font=("Arial", 14))
        self.captcha_entry.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        self.submit_button = tk.Button(self.root, text="Submit", command=self.check_captcha, font=("Arial", 14), bg="red", fg="white")
        self.submit_button.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        self.message_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.message_label.grid(row=2, column=0, columnspan=2, pady=5)

        self.high_scores_display = tk.Text(self.root, font=("Arial", 14), bg="white", fg="black", height=10, width=40)
        self.high_scores_display.grid(row=3, column=0, columnspan=2, padx=10, pady=5)
        self.high_scores_display.insert(tk.END, "High Scores:\n")
        self.high_scores_display.config(state=tk.DISABLED)

        self.init_start_popup()

    def init_start_popup(self):
        self.popup = tk.Toplevel(self.root)
        self.popup.title("Start Game")
        self.popup.geometry("300x150")
        tk.Label(self.popup, text="Enter your name:", font=("Arial", 14)).pack(pady=10)
        tk.Entry(self.popup, textvariable=self.player_name, font=("Arial", 14)).pack(pady=10)
        tk.Button(self.popup, text="Start Game", command=self.start_game, font=("Arial", 14), bg="red", fg="white").pack(pady=10)
        
    def update_high_scores(self):
        self.high_scores_display.config(state=tk.NORMAL)
        self.high_scores_display.delete(1.0, tk.END)
        self.high_scores_display.insert(tk.END, "High Scores:\n")
        for score in self.high_scores:
            self.high_scores_display.insert(tk.END, f"{score}\n")
        self.high_scores_display.config(state=tk.DISABLED)

    def generate_captcha(self, length=6):
        characters = string.ascii_letters + string.digits
        captcha = ''.join(random.choice(characters) for _ in range(length))
        return captcha

    def draw_captcha(self, captcha):
        self.t.clear()
        self.t.penup()
        x_start = -100
        for char in captcha:
            font_size = random.randint(20, 40)
            color = random.choice(["#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#FF00FF", "#00FFFF"])
            self.t.goto(x_start, 0)
            self.t.pendown()
            self.t.color(color)
            self.t.write(char, font=("Arial", font_size, "bold"))
            x_start += 30
            self.t.penup()

        for _ in range(10):
            x1, y1 = random.randint(-200, 200), random.randint(-100, 100)
            x2, y2 = random.randint(-200, 200), random.randint(-100, 100)
            self.t.goto(x1, y1)
            self.t.pendown()
            self.t.color("#FF0000")
            self.t.goto(x2, y2)
            self.t.penup()

    def start_game(self):
        if not self.player_name.get():
            self.message_label.config(text="Please enter your name!")
            return

        self.games_completed = 0
        self.high_score = float('inf')
        self.message_label.config(text="")
        self.popup.destroy()
        self.next_captcha()

    def next_captcha(self):
        self.captcha_input.set("")
        self.captcha = self.generate_captcha()
        self.draw_captcha(self.captcha)
        self.start_time = time.time()

    def check_captcha(self):
        user_input = self.captcha_input.get()
        end_time = time.time()

        if end_time - self.start_time > 30:
            self.display_message("Time's up! You failed to enter the CAPTCHA in time.")
            self.end_game()
        elif user_input == self.captcha:
            self.games_completed += 1
            time_taken = end_time - self.start_time
            if time_taken < self.high_score:
                self.high_score = time_taken
            if self.games_completed < 3:
                self.display_message("CAPTCHA solved correctly! Moving to next round...", 1)
                self.next_captcha()
            else:
                self.display_message(f"Congratulations {self.player_name.get()}! You solved all CAPTCHAs. High Score: {self.high_score:.2f} seconds")
                self.high_scores.append(f"{self.player_name.get()}: {self.high_score:.2f} seconds")
                self.high_scores = sorted(self.high_scores, key=lambda x: float(x.split(': ')[1].split()[0]))
                self.update_high_scores()
                self.end_game()
        else:
            self.display_message("Incorrect CAPTCHA! Game Over.")
            self.end_game()

    def display_message(self, message, wait_time=2):
        self.message_label.config(text=message)
        self.root.update()
        time.sleep(wait_time)
        self.message_label.config(text="")

    def end_game(self):
        self.captcha = ""
        self.captcha_input.set("")
        self.t.clear()

if __name__ == "__main__":
    root = tk.Tk()
    app = CaptchaGame(root)
    root.mainloop()
