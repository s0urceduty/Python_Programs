# Snake Pencil V1.0
# The classic Snake game with creative drawing capabilities. 
# Copyright (C) 2024, Sourceduty - All Rights Reserved.

# Controls:
# SPACE: Pause or resume the game.
# WASD: Move the snake up, down, left, or right.
# Q/E with W/S: Move the snake diagonally.
# Shift: Hold to move the snake faster.
# C: Open the color menu to change the snake’s drawing color.
# P: Save the current drawing as an image file.
# M: Return to the main menu from the pause menu.
# 1-9: Add predefined template drawings.
# X: Clear the current drawing.

import math 
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import BooleanProperty, ListProperty, StringProperty
from kivy.logger import Logger
from collections import deque
from kivy.uix.popup import Popup
import time

# Setting window size (optional: make responsive)
Window.size = (800, 600)

# Color options
COLOR_OPTIONS = {
    1: (1, 0, 0),      # Red
    2: (0, 1, 0),      # Green
    3: (0, 0, 1),      # Blue
    4: (1, 1, 0),      # Yellow
    5: (0.5, 0, 0.5),  # Purple
    6: (1, 1, 1),      # White
    7: (1, 0.5, 0),    # Orange
    8: (0, 1, 1),      # Cyan
    9: (1, 0, 1)       # Magenta
}

class DrawingPad(Widget):
    fast_mode = BooleanProperty(False)
    paused = BooleanProperty(False)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Initial position at the center
        self.snake_pos = [Window.width // 2, Window.height // 2]
        # Using deque for efficient path management
        self.snake_path = deque([tuple(self.snake_pos)], maxlen=5000)
        
        # Get the initial color from the App's selected_color property
        app = App.get_running_app()
        self.current_color = app.selected_color if hasattr(app, 'selected_color') else COLOR_OPTIONS[2]  # Default Green
        self.snake_speed = 5
        self.fast_speed = 10
        self.key_pressed = {}
        self.shift_held = False  # Track the state of the shift key

        # Define templates for keys 1-9
        self.templates = {
            '1': self.generate_heart(),
            '2': self.generate_cube(),
            '3': self.generate_smiley(),
            '4': self.generate_star(),
            '5': self.generate_triangle(),
            '6': self.generate_square(),
            '7': self.generate_pentagon(),
            '8': self.generate_hexagon(),
            '9': self.generate_octagon()
        }

        with self.canvas:
            self.color_instruction = Color(*self.current_color)
            self.line = Line(points=self.snake_path, width=2)

        # Schedule the update method at 60 FPS
        Clock.schedule_interval(self.update, 1 / 60)

        # Bind keyboard events
        Window.bind(on_key_down=self._on_key_down)
        Window.bind(on_key_up=self._on_key_up)

    def generate_heart(self):
        # Simple heart shape as a list of relative (dx, dy) tuples
        return [
            (0, 0), (10, 20), (20, 0), (30, 20), (40, 0), (50, 20), (60, 0),
            (50, -20), (40, 0), (30, -20), (20, 0), (10, -20), (0, 0)
        ]

    def generate_cube(self):
        # Simple cube shape as a list of relative (dx, dy) tuples
        return [
            (0, 0), (0, 50), (50, 50), (50, 0), (0, 0),
            (25, 25), (25, 75), (75, 75), (75, 25), (25, 25)
        ]

    def generate_smiley(self):
        # Simple smiley face as a list of relative (dx, dy) tuples
        points = []
        # Outer circle
        for angle in range(0, 360, 30):
            radians = angle * math.pi / 180
            x = 50 * math.cos(radians)
            y = 50 * math.sin(radians)
            points.append((x, y))
        # Eyes and smile can be additional lines or omitted for simplicity
        return points

    def generate_star(self):
        # Simple 5-pointed star as a list of relative (dx, dy) tuples
        points = []
        for angle in range(0, 360, 72):
            radians = angle * math.pi / 180
            x = 50 * math.cos(radians)
            y = 50 * math.sin(radians)
            points.append((x, y))
            radians = (angle + 36) * math.pi / 180
            x = 25 * math.cos(radians)
            y = 25 * math.sin(radians)
            points.append((x, y))
        return points

    def generate_triangle(self):
        # Simple equilateral triangle as a list of relative (dx, dy) tuples
        return [
            (0, 0), (50, 86.6), (100, 0), (0, 0)
        ]

    def generate_square(self):
        # Simple square as a list of relative (dx, dy) tuples
        return [
            (0, 0), (0, 50), (50, 50), (50, 0), (0, 0)
        ]

    def generate_pentagon(self):
        # Simple pentagon as a list of relative (dx, dy) tuples
        points = []
        for angle in range(0, 360, 72):
            radians = angle * math.pi / 180
            x = 50 * math.cos(radians)
            y = 50 * math.sin(radians)
            points.append((x, y))
        points.append(points[0])  # Close the pentagon
        return points

    def generate_hexagon(self):
        # Simple hexagon as a list of relative (dx, dy) tuples
        points = []
        for angle in range(0, 360, 60):
            radians = angle * math.pi / 180
            x = 50 * math.cos(radians)
            y = 50 * math.sin(radians)
            points.append((x, y))
        points.append(points[0])  # Close the hexagon
        return points

    def generate_octagon(self):
        # Simple octagon as a list of relative (dx, dy) tuples
        points = []
        for angle in range(0, 360, 45):
            radians = angle * math.pi / 180
            x = 50 * math.cos(radians)
            y = 50 * math.sin(radians)
            points.append((x, y))
        points.append(points[0])  # Close the octagon
        return points

    def _on_key_down(self, window, key, scancode, codepoint, modifier):
        if codepoint:
            key_char = codepoint.lower()
            self.key_pressed[key_char] = True  # Track key press

        # Check if shift key is in modifiers
        if 'shift' in modifier:
            self.shift_held = True
            self.fast_mode = True

        # Handle specific key actions
        if codepoint:
            key_char = codepoint.lower()
            if key_char == ' ':
                self.toggle_pause()
            elif key_char == 'c':
                self.open_color_menu()
            elif key_char == 'p':
                self.save_drawing()
            elif key_char == 'm':
                self.return_to_main_menu()
            elif key_char in self.templates:
                self.add_template(key_char)
            elif key_char == 'x':
                self.clear_drawing()

    def _on_key_up(self, window, key, scancode):
        # Define a mapping from key codes to characters
        key_mapping = {
            119: 'w',  # 'w'
            97: 'a',   # 'a'
            115: 's',  # 's'
            100: 'd',  # 'd'
            113: 'q',  # 'q'
            101: 'e',  # 'e'
            32: ' ',   # space
            99: 'c',   # 'c'
            112: 'p',  # 'p'
            109: 'm',  # 'm'
            116: 't',  # 't'
            120: 'x'    # 'x'
        }

        key_char = key_mapping.get(key)
        if key_char and key_char in self.key_pressed:
            del self.key_pressed[key_char]

        # If shift key is released, turn off fast mode
        if key in (304, 303):  # Kivy keycodes for left and right Shift
            self.shift_held = False
            self.fast_mode = False

    def toggle_pause(self):
        self.paused = not self.paused
        if self.paused:
            Clock.unschedule(self.update)
            Logger.info("Game Paused")
            # Display a pause overlay
            popup = Popup(title='Paused',
                          content=Label(text='Game Paused'),
                          size_hint=(0.5, 0.3))
            popup.open()
        else:
            Clock.schedule_interval(self.update, 1 / 60)
            Logger.info("Game Resumed")
            # Optionally, close the pause overlay if implemented

    def update(self, dt):
        if self.paused:
            return

        move_x, move_y = 0, 0
        speed = self.fast_speed if self.fast_mode else self.snake_speed

        try:
            # Diagonal movements using 'q' and 'e'
            if self.key_pressed.get('w') and self.key_pressed.get('q'):
                move_x, move_y = -speed, speed  # Up-Left
            elif self.key_pressed.get('w') and self.key_pressed.get('e'):
                move_x, move_y = speed, speed   # Up-Right
            elif self.key_pressed.get('s') and self.key_pressed.get('q'):
                move_x, move_y = -speed, -speed # Down-Left
            elif self.key_pressed.get('s') and self.key_pressed.get('e'):
                move_x, move_y = speed, -speed  # Down-Right
            # Cardinal directions
            elif self.key_pressed.get('w'):
                move_y = speed    # Move Up
            elif self.key_pressed.get('s'):
                move_y = -speed   # Move Down
            elif self.key_pressed.get('a'):
                move_x = -speed   # Move Left
            elif self.key_pressed.get('d'):
                move_x = speed    # Move Right

            # Move the snake only if there's input
            if move_x != 0 or move_y != 0:
                self.move_snake(move_x, move_y)
        except Exception as e:
            Logger.error(f"Error during update: {str(e)}")

    def move_snake(self, move_x, move_y):
        snake_size = 10  # Define snake size or retrieve dynamically

        # Calculate new position
        new_x = self.snake_pos[0] + move_x
        new_y = self.snake_pos[1] + move_y

        # Clamp within window boundaries considering snake size
        new_x = max(snake_size, min(new_x, Window.width - snake_size))
        new_y = max(snake_size, min(new_y, Window.height - snake_size))

        # Update the snake's position
        self.snake_pos = [new_x, new_y]
        self.snake_path.append(tuple(self.snake_pos))

        # Update the Line's points
        self.line.points += [new_x, new_y]

    def change_color(self, color_index):
        if color_index in COLOR_OPTIONS:
            self.current_color = COLOR_OPTIONS[color_index]
            self.color_instruction.rgb = self.current_color
            Logger.info(f"Color changed to index {color_index}")
        else:
            Logger.warning("Invalid color index.")

    def open_color_menu(self):
        # Separate color menu
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        for index, color in COLOR_OPTIONS.items():
            btn = Button(text=f"Color {index}", size_hint=(1, None), height=50)
            btn.background_color = color + (1,)
            btn.bind(on_release=lambda btn, idx=index: self.change_color(idx))
            layout.add_widget(btn)
        popup = Popup(title='Select Color', content=layout, size_hint=(0.5, 0.5))
        popup.open()

    def save_drawing(self):
        image_path = f"snake_drawing_{int(time.time())}.png"
        try:
            self.export_to_png(image_path)
            Logger.info(f"Drawing saved as {image_path}")
            
            # Show a popup to inform the user
            popup = Popup(title='Save Drawing',
                          content=Label(text=f'Drawing saved as {image_path}'),
                          size_hint=(0.5, 0.3))
            popup.open()
        except Exception as e:
            Logger.error(f"Failed to save drawing: {str(e)}")
            
            # Show a popup to inform the user of the error
            popup = Popup(title='Save Error',
                          content=Label(text='Failed to save drawing.'),
                          size_hint=(0.5, 0.3))
            popup.open()

    def return_to_main_menu(self):
        app = App.get_running_app()
        if app.root:
            app.root.current = 'main_menu'
            Logger.info("Returned to Main Menu")
            # Optionally, reset the drawing pad state here

    def add_template(self, key_char):
        # Get the template corresponding to the pressed key
        shape = self.templates.get(key_char, [])
        
        if not shape:
            Logger.warning(f"No template found for key '{key_char}'.")
            return

        # Calculate absolute positions based on current snake position
        base_x, base_y = self.snake_pos
        new_points = []

        for point in shape:
            dx, dy = point  # Now point is a tuple (dx, dy)
            new_x = base_x + dx
            new_y = base_y + dy
            # Clamp the new points within window boundaries
            new_x = max(10, min(new_x, Window.width - 10))
            new_y = max(10, min(new_y, Window.height - 10))
            new_points += [new_x, new_y]

        # Append the new points to the snake path
        self.line.points += new_points

        Logger.info(f"Added template from key '{key_char}' to the drawing.")

    def clear_drawing(self):
        # Clear the snake path
        self.snake_path.clear()
        # Reset the snake's position to the center
        self.snake_pos = [Window.width // 2, Window.height // 2]
        self.snake_path.append(tuple(self.snake_pos))
        # Reset the Line's points
        self.line.points = list(self.snake_pos)
        Logger.info("Drawing area cleared.")

class MainMenu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)

        title = Label(text="Snake Pencil", font_size='40sp')
        layout.add_widget(title)

        start_button = Button(text="Start", size_hint=(0.5, 0.2), pos_hint={'center_x': 0.5})
        start_button.bind(on_release=self.start_game)
        layout.add_widget(start_button)

        quit_button = Button(text="Quit", size_hint=(0.5, 0.2), pos_hint={'center_x': 0.5})
        quit_button.bind(on_release=self.quit_app)
        layout.add_widget(quit_button)

        # Add Color Selection Button
        color_button = Button(text="Select Color", size_hint=(0.5, 0.2), pos_hint={'center_x': 0.5})
        color_button.bind(on_release=self.open_color_menu_main)
        layout.add_widget(color_button)

        self.add_widget(layout)

    def start_game(self, instance):
        self.manager.current = 'drawing_pad'
        Logger.info("Game Started")

    def quit_app(self, instance):
        App.get_running_app().stop()
        Logger.info("App Quit")

    def open_color_menu_main(self, instance):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        for index, color in COLOR_OPTIONS.items():
            btn = Button(text=f"Color {index}", size_hint=(1, None), height=50)
            btn.background_color = color + (1,)
            btn.bind(on_release=lambda btn, idx=index: self.select_color_main(idx))
            layout.add_widget(btn)
        popup = Popup(title='Select Color',
                      content=layout,
                      size_hint=(0.5, 0.5))
        popup.open()

    def select_color_main(self, color_index):
        app = App.get_running_app()
        if hasattr(app, 'selected_color'):
            app.selected_color = COLOR_OPTIONS[color_index]
            Logger.info(f"Main Menu: Color changed to index {color_index}")
        else:
            Logger.warning("App does not have 'selected_color' property.")

class DrawingPadScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.drawing_pad = DrawingPad()
        self.add_widget(self.drawing_pad)

class SnakeApp(App):
    selected_color = ListProperty([0, 1, 0])  # Default Green

    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainMenu(name='main_menu'))
        sm.add_widget(DrawingPadScreen(name='drawing_pad'))
        sm.current = 'main_menu'
        return sm

if __name__ == '__main__':
    SnakeApp().run()
