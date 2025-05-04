# Snake Pencil V2.0
# Self-guided line drawing Python program.
# Copyright (C) 2025, Sourceduty - All Rights Reserved.

import random
import time
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.graphics.texture import Texture
from kivy.core.image import Image as CoreImage


class MovementHandler:
    """Handles smooth movement for both AI and manual mode."""

    def __init__(self):
        self.x, self.y = Window.width // 2, Window.height // 2
        self.vx, self.vy = 0, 0
        self.speed_modes = [2, 4, 6]  # Slow, Normal, Fast
        self.speed_index = 1  # Default to Normal
        self.speed = self.speed_modes[self.speed_index]
        self.acceleration = 0.2
        self.deceleration = 0.9
        self.manual_mode = False
        self.keys_pressed = {}
        self.ai_modes = ["Random", "No Overlaps", "Color Change on Overlaps"]
        self.ai_mode_index = 0
        self.time_modes = [30, 60, 120, 300, None]  # 30 sec, 1 min, 2 min, 5 min, Unlimited
        self.time_mode_index = 0
        self.runtime_limit = self.time_modes[self.time_mode_index]  # Default time limit

    def toggle_manual_mode(self, button):
        """Toggle between AI and manual mode."""
        self.manual_mode = not self.manual_mode
        button.text = "Mode: Manual" if self.manual_mode else "Mode: AI"

    def toggle_ai_mode(self, button):
        """Cycle through AI movement styles."""
        if not self.manual_mode:
            self.ai_mode_index = (self.ai_mode_index + 1) % len(self.ai_modes)
            button.text = f"AI: {self.ai_modes[self.ai_mode_index]}"

    def toggle_time_mode(self, button):
        """Cycle through time limits."""
        self.time_mode_index = (self.time_mode_index + 1) % len(self.time_modes)
        self.runtime_limit = self.time_modes[self.time_mode_index]
        time_text = "Unlimited" if self.runtime_limit is None else f"{self.runtime_limit // 60} min" if self.runtime_limit >= 60 else f"{self.runtime_limit} sec"
        button.text = f"Time: {time_text}"

    def toggle_speed_mode(self, button):
        """Cycle through different speed modes."""
        self.speed_index = (self.speed_index + 1) % len(self.speed_modes)
        self.speed = self.speed_modes[self.speed_index]
        speed_text = ["Slow", "Normal", "Fast"][self.speed_index]
        button.text = f"Speed: {speed_text}"


class DrawingPad(Widget):
    """Game area with AI and manual movement."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.movement = MovementHandler()
        self.snake_path = []

        with self.canvas:
            self.color_instruction = Color(1, 1, 1)
            self.snake_line = Line(points=[], width=2)

        self.paused = True
        Clock.schedule_interval(self.update, 1 / 60)

        # Re-added key event bindings
        Window.bind(on_key_down=self.on_key_down)
        Window.bind(on_key_up=self.on_key_up)

    def update(self, dt):
        """Updates movement based on mode and time limit."""
        if self.paused:
            return

        self.move_smooth()

        x, y = self.movement.x, self.movement.y
        self.snake_path.append((x, y))
        self.snake_line.points += [x, y]

        if self.movement.ai_modes[self.movement.ai_mode_index] == "Color Change on Overlaps":
            if (x, y) in self.snake_path[:-1]:
                self.color_instruction.rgb = (random.random(), random.random(), random.random())

    def move_smooth(self):
        """Handles smooth movement for both AI and manual."""
        if self.movement.manual_mode:
            if 'left' in self.movement.keys_pressed:
                self.movement.vx = max(-self.movement.speed, self.movement.vx - self.movement.acceleration)
            if 'right' in self.movement.keys_pressed:
                self.movement.vx = min(self.movement.speed, self.movement.vx + self.movement.acceleration)
            if 'up' in self.movement.keys_pressed:
                self.movement.vy = min(self.movement.speed, self.movement.vy + self.movement.acceleration)
            if 'down' in self.movement.keys_pressed:
                self.movement.vy = max(-self.movement.speed, self.movement.vy - self.movement.acceleration)
        else:
            self.movement.vx = random.uniform(-self.movement.speed, self.movement.speed)
            self.movement.vy = random.uniform(-self.movement.speed, self.movement.speed)

        self.movement.x += self.movement.vx
        self.movement.y += self.movement.vy

    def on_key_down(self, window, key, *args):
        """Handles key press events."""
        key_map = {275: 'right', 276: 'left', 273: 'up', 274: 'down'}
        if key in key_map:
            self.movement.keys_pressed[key_map[key]] = True

    def on_key_up(self, window, key, *args):
        """Handles key release events."""
        key_map = {275: 'right', 276: 'left', 273: 'up', 274: 'down'}
        if key in key_map and key_map[key] in self.movement.keys_pressed:
            del self.movement.keys_pressed[key_map[key]]

    def capture_image(self):
        """Captures and saves the drawing as an image."""
        texture = self.export_as_image()
        filename = f"snake_drawing_{int(time.time())}.png"
        texture.save(filename)
        print(f"Image saved as {filename}")

    def start_drawing(self):
        """Start drawing."""
        self.paused = False

    def pause_drawing(self):
        """Pauses the drawing."""
        self.paused = True

    def reset_drawing(self):
        """Resets the drawing."""
        self.snake_path.clear()
        self.snake_line.points = []
        self.movement.x, self.movement.y = Window.width // 2, Window.height // 2
        self.paused = True


class ControlPanel(BoxLayout):
    """Control panel for game management."""

    def __init__(self, drawing_pad, **kwargs):
        super().__init__(orientation="horizontal", size_hint=(1, 0.1), **kwargs)
        self.drawing_pad = drawing_pad

        self.mode_button = Button(text="Mode: AI", on_release=lambda x: self.drawing_pad.movement.toggle_manual_mode(self.mode_button))
        self.ai_mode_button = Button(text="AI: Random", on_release=lambda x: self.drawing_pad.movement.toggle_ai_mode(self.ai_mode_button))
        self.time_button = Button(text="Time: 30 sec", on_release=lambda x: self.drawing_pad.movement.toggle_time_mode(self.time_button))
        self.speed_button = Button(text="Speed: Normal", on_release=lambda x: self.drawing_pad.movement.toggle_speed_mode(self.speed_button))
        self.capture_button = Button(text="Capture", on_release=lambda x: self.drawing_pad.capture_image())
        self.start_button = Button(text="Start", on_release=lambda x: self.drawing_pad.start_drawing())
        self.pause_button = Button(text="Pause", on_release=lambda x: self.drawing_pad.pause_drawing())
        self.reset_button = Button(text="Reset", on_release=lambda x: self.drawing_pad.reset_drawing())
        self.quit_button = Button(text="Quit", on_release=lambda x: App.get_running_app().stop())

        self.add_widget(self.mode_button)
        self.add_widget(self.ai_mode_button)
        self.add_widget(self.time_button)
        self.add_widget(self.speed_button)
        self.add_widget(self.capture_button)
        self.add_widget(self.start_button)
        self.add_widget(self.pause_button)
        self.add_widget(self.reset_button)
        self.add_widget(self.quit_button)


class MainApp(App):
    """Main application class."""

    def build(self):
        Window.size = (1000, 800)
        root = BoxLayout(orientation="vertical")
        drawing_pad = DrawingPad()
        controls = ControlPanel(drawing_pad)
        root.add_widget(drawing_pad)
        root.add_widget(controls)
        return root


if __name__ == "__main__":
    MainApp().run()
