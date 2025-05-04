# Snake Pencil V1.2
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
# Auto Mode Toggle and Pattern Selection

import math  # For movement patterns
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import BooleanProperty, ListProperty, StringProperty
from kivy.logger import Logger
from collections import deque
from kivy.uix.popup import Popup
import time
import random  # For random movement

# Setting window size (optional: make responsive)
Window.size = (1000, 800)  # Increased size for better layout

# Color options (RGB tuples)
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
    automatic_mode = BooleanProperty(False)  # Track automatic mode
    selected_pattern = StringProperty('circle')  # Default movement pattern

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Initial position at the center of the window
        self.snake_pos = [Window.width // 2, Window.height // 2]
        # Using deque for efficient path management as a flat list
        self.snake_path = deque([self.snake_pos[0], self.snake_pos[1]], maxlen=5000)
        self.auto_path = deque(maxlen=5000)  # For automatic patterns
        self.mirror_path = deque(maxlen=5000)  # For mirrored drawing

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
            # Color for manual drawing
            self.color_instruction = Color(*self.current_color)
            self.snake_line = Line(points=list(self.snake_path), width=2)
            # Calculate contrasting color
            contrasting_color = self.get_contrasting_color(self.current_color)
            self.mirror_color_instruction = Color(*contrasting_color)
            self.mirror_line = Line(points=list(self.mirror_path), width=2)
            # Color for automatic drawing (different color for distinction)
            self.auto_color_instruction = Color(1, 1, 1)  # White color
            self.auto_line = Line(points=[], width=2)

        # Schedule the update method at 60 FPS
        Clock.schedule_interval(self.update, 1 / 60)

        # Bind keyboard events
        Window.bind(on_key_down=self._on_key_down)
        Window.bind(on_key_up=self._on_key_up)

        # Initialize pattern variables for movement patterns
        self.pattern_angle = 0  # Separate angle for automatic patterns
        self.pattern_radius = 100  # Radius for circular and spiral movement
        self.pattern_radius_increment = 0.1  # For spiral
        self.center_x = self.snake_pos[0]
        self.center_y = self.snake_pos[1]

    # Template Generation Methods (unchanged)
    def generate_heart(self):
        """Generate a simple heart shape as a list of relative (dx, dy) tuples."""
        return [
            (0, 0), (10, 20), (20, 0), (30, 20), (40, 0), (50, 20), (60, 0),
            (50, -20), (40, 0), (30, -20), (20, 0), (10, -20), (0, 0)
        ]

    def generate_cube(self):
        """Generate a simple cube shape as a list of relative (dx, dy) tuples."""
        return [
            (0, 0), (0, 50), (50, 50), (50, 0), (0, 0),
            (25, 25), (25, 75), (75, 75), (75, 25), (25, 25)
        ]

    def generate_smiley(self):
        """Generate a simple smiley face as a list of relative (dx, dy) tuples."""
        points = []
        # Outer circle
        for angle in range(0, 360, 30):
            radians = angle * math.pi / 180
            x = 50 * math.cos(radians)
            y = 50 * math.sin(radians)
            points.append((x, y))
        return points

    def generate_star(self):
        """Generate a simple 5-pointed star as a list of relative (dx, dy) tuples."""
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
        """Generate a simple equilateral triangle as a list of relative (dx, dy) tuples."""
        return [
            (0, 0), (50, 86.6), (100, 0), (0, 0)
        ]

    def generate_square(self):
        """Generate a simple square as a list of relative (dx, dy) tuples."""
        return [
            (0, 0), (0, 50), (50, 50), (50, 0), (0, 0)
        ]

    def generate_pentagon(self):
        """Generate a simple pentagon as a list of relative (dx, dy) tuples."""
        points = []
        for angle in range(0, 360, 72):
            radians = angle * math.pi / 180
            x = 50 * math.cos(radians)
            y = 50 * math.sin(radians)
            points.append((x, y))
        points.append(points[0])  # Close the pentagon
        return points

    def generate_hexagon(self):
        """Generate a simple hexagon as a list of relative (dx, dy) tuples."""
        points = []
        for angle in range(0, 360, 60):
            radians = angle * math.pi / 180
            x = 50 * math.cos(radians)
            y = 50 * math.sin(radians)
            points.append((x, y))
        points.append(points[0])  # Close the hexagon
        return points

    def generate_octagon(self):
        """Generate a simple octagon as a list of relative (dx, dy) tuples."""
        points = []
        for angle in range(0, 360, 45):
            radians = angle * math.pi / 180
            x = 50 * math.cos(radians)
            y = 50 * math.sin(radians)
            points.append((x, y))
        points.append(points[0])  # Close the octagon
        return points

    # Automatic Movement Pattern Methods (unchanged)
    def get_next_position_circle(self, dt):
        """Calculate the next relative position in a circular path."""
        self.pattern_angle += math.radians(1)  # Increment angle
        rel_x = self.pattern_radius * math.cos(self.pattern_angle)
        rel_y = self.pattern_radius * math.sin(self.pattern_angle)
        return rel_x, rel_y

    def get_next_position_figure_eight(self, dt):
        """Calculate the next relative position in a figure-eight path."""
        self.pattern_angle += math.radians(1)  # Increment angle
        rel_x = self.pattern_radius * math.sin(self.pattern_angle)
        rel_y = self.pattern_radius * math.sin(self.pattern_angle) * math.cos(self.pattern_angle)
        return rel_x, rel_y

    def get_next_position_spiral(self, dt):
        """Calculate the next relative position in a spiral path."""
        self.pattern_angle += math.radians(1)  # Increment angle
        self.pattern_radius += self.pattern_radius_increment  # Gradually increase radius
        rel_x = self.pattern_radius * math.cos(self.pattern_angle)
        rel_y = self.pattern_radius * math.sin(self.pattern_angle)
        return rel_x, rel_y

    def get_next_position_random(self, dt):
        """Calculate the next relative position in a random path."""
        move_x = random.choice([-self.snake_speed, 0, self.snake_speed])
        move_y = random.choice([-self.snake_speed, 0, self.snake_speed])
        return move_x, move_y

    # Keyboard Event Handlers (unchanged)
    def _on_key_down(self, window, key, scancode, codepoint, modifier):
        """Handle key press events."""
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
        """Handle key release events."""
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
            120: 'x'    # 'x'
        }

        key_char = key_mapping.get(key)
        if key_char and key_char in self.key_pressed:
            del self.key_pressed[key_char]

        # If shift key is released, turn off fast mode
        if key in (304, 303):  # Kivy keycodes for left and right Shift
            self.shift_held = False
            self.fast_mode = False

    # Pause and Resume Functionality (unchanged)
    def toggle_pause(self):
        """Toggle between paused and active states."""
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

    # Main Update Loop (Ensuring this method is correctly defined)
    def update(self, dt):
        """Update the snake's position and drawing based on the current mode."""
        if self.paused:
            return

        if self.automatic_mode:
            # Handle automatic movement based on selected pattern
            if self.selected_pattern == 'circle':
                rel_x, rel_y = self.get_next_position_circle(dt)
            elif self.selected_pattern == 'figure_eight':
                rel_x, rel_y = self.get_next_position_figure_eight(dt)
            elif self.selected_pattern == 'spiral':
                rel_x, rel_y = self.get_next_position_spiral(dt)
            elif self.selected_pattern == 'random':
                rel_x, rel_y = self.get_next_position_random(dt)
            else:
                # Default to circular movement
                rel_x, rel_y = self.get_next_position_circle(dt)

            # Compute absolute positions based on snake_pos
            new_x = self.snake_pos[0] + rel_x
            new_y = self.snake_pos[1] + rel_y

            # Append to automatic path
            self.auto_path.extend([new_x, new_y])
            self.auto_line.points = list(self.auto_path)
        else:
            # Handle manual movement
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

    # Movement Handling (unchanged)
    def move_snake(self, move_x, move_y):
        """Move the snake by (move_x, move_y) and update the drawing."""
        snake_size = 10  # Define snake size or retrieve dynamically

        # Calculate new position
        new_x = self.snake_pos[0] + move_x
        new_y = self.snake_pos[1] + move_y

        # Clamp within window boundaries considering snake size
        new_x = max(snake_size, min(new_x, Window.width - snake_size))
        new_y = max(snake_size, min(new_y, Window.height - snake_size))

        # Update the snake's position
        self.snake_pos = [new_x, new_y]
        self.snake_path.extend([new_x, new_y])

        # Update the Line's points
        self.snake_line.points = list(self.snake_path)

        # Update the mirrored path
        mirrored_x = Window.width - new_x
        mirrored_y = new_y  # Vertical mirroring; change to (Window.height - new_y) for horizontal
        self.mirror_path.extend([mirrored_x, mirrored_y])
        self.mirror_line.points = list(self.mirror_path)

    # Color Management (unchanged)
    def change_color(self, color_index):
        """Change the snake's drawing color based on the selected index."""
        if color_index in COLOR_OPTIONS:
            self.current_color = COLOR_OPTIONS[color_index]
            self.color_instruction.rgb = self.current_color
            # Update contrasting color
            contrasting_color = self.get_contrasting_color(self.current_color)
            self.mirror_color_instruction.rgb = contrasting_color
            Logger.info(f"Color changed to index {color_index}")
        else:
            Logger.warning("Invalid color index.")

    def get_contrasting_color(self, color):
        """Calculate a contrasting color by inverting the original color."""
        return tuple(1 - c for c in color)

    def open_color_menu(self):
        """Open a popup menu for color selection."""
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        for index, color in COLOR_OPTIONS.items():
            btn = Button(text=f"Color {index}", size_hint=(1, None), height=50)
            btn.background_color = color + (1,)
            btn.bind(on_release=lambda btn, idx=index: self.change_color(idx))
            layout.add_widget(btn)
        popup = Popup(title='Select Color',
                      content=layout,
                      size_hint=(0.3, 0.5))
        popup.open()

    # Saving Drawings (unchanged)
    def save_drawing(self):
        """Save the current drawing as a PNG image capturing the full screen."""
        image_path = f"snake_drawing_{int(time.time())}.png"
        try:
            # Capture the entire window by exporting the root widget
            App.get_running_app().root.export_to_png(image_path)
            Logger.info(f"Drawing saved as {image_path}")

            # Show a popup to inform the user
            popup = Popup(title='Save Drawing',
                          content=Label(text=f'Drawing saved as {image_path}'),
                          size_hint=(0.4, 0.3))
            popup.open()
        except Exception as e:
            Logger.error(f"Failed to save drawing: {str(e)}")

            # Show a popup to inform the user of the error
            popup = Popup(title='Save Error',
                          content=Label(text='Failed to save drawing.'),
                          size_hint=(0.4, 0.3))
            popup.open()

    # Returning to Main Menu (unchanged)
    def return_to_main_menu(self):
        """Return to the main menu screen."""
        app = App.get_running_app()
        if app.root:
            app.root.current = 'main_menu'
            Logger.info("Returned to Main Menu")
            # Optionally, reset the drawing pad state here

    # Adding Templates to Drawing (unchanged)
    def add_template(self, key_char):
        """Add a predefined template to the drawing based on the pressed key."""
        # Get the template corresponding to the pressed key
        shape = self.templates.get(key_char, [])

        if not shape:
            Logger.warning(f"No template found for key '{key_char}'.")
            return

        # Calculate absolute positions based on current snake position
        base_x, base_y = self.snake_pos
        new_points = []

        # If the first point is (0,0), skip it to avoid duplicating the current position
        start_index = 1 if shape and shape[0] == (0, 0) else 0

        for point in shape[start_index:]:
            dx, dy = point  # Relative movement
            new_x = base_x + dx
            new_y = base_y + dy
            # Clamp within window boundaries
            new_x = max(10, min(new_x, Window.width - 10))
            new_y = max(10, min(new_y, Window.height - 10))
            new_points += [new_x, new_y]

        # Append the new points to the snake path as floats
        self.snake_path.extend(new_points)

        # Update the Line's points
        self.snake_line.points = list(self.snake_path)

        # Update mirrored path
        for i in range(start_index, len(shape)):
            dx, dy = shape[i]
            mirrored_x = Window.width - (base_x + dx)
            mirrored_y = base_y + dy
            self.mirror_path.extend([mirrored_x, mirrored_y])

        self.mirror_line.points = list(self.mirror_path)

        # Update snake_pos to the last point of the template
        if new_points:
            self.snake_pos = [new_points[-2], new_points[-1]]

        Logger.info(f"Added template from key '{key_char}' to the drawing.")

    # Clearing the Drawing Area (unchanged)
    def clear_drawing(self):
        """Clear the current drawing and reset the snake's position."""
        # Clear the snake path
        self.snake_path.clear()
        # Clear the mirrored path
        self.mirror_path.clear()
        # Reset the snake's position to the center
        self.snake_pos = [Window.width // 2, Window.height // 2]
        # Append the starting position as floats
        self.snake_path.extend([self.snake_pos[0], self.snake_pos[1]])
        self.mirror_path.extend([Window.width - self.snake_pos[0], self.snake_pos[1]])
        # Reset the Line's points
        self.snake_line.points = [self.snake_pos[0], self.snake_pos[1]]
        self.mirror_line.points = [Window.width - self.snake_pos[0], self.snake_pos[1]]
        Logger.info("Drawing area cleared.")

class MainMenu(Screen):
    """Main Menu Screen with Start, Quit, and Color Selection options."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=100, spacing=30)

        # Application Title
        title = Label(text="Snake Pencil", font_size='60sp', size_hint=(1, 0.3))
        layout.add_widget(title)

        # Version Label
        version_label = Label(text=f"Version: {App.get_running_app().version}", font_size='20sp', size_hint=(1, 0.1))
        layout.add_widget(version_label)

        # Start Button
        start_button = Button(text="Start", size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        start_button.bind(on_release=self.start_game)
        layout.add_widget(start_button)

        # Quit Button
        quit_button = Button(text="Quit", size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        quit_button.bind(on_release=self.quit_app)
        layout.add_widget(quit_button)

        # Color Selection Button
        color_button = Button(text="Select Color", size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        color_button.bind(on_release=self.open_color_menu_main)
        layout.add_widget(color_button)

        self.add_widget(layout)

    def start_game(self, instance):
        """Switch to the drawing pad screen."""
        self.manager.current = 'drawing_pad'
        Logger.info("Game Started")

    def quit_app(self, instance):
        """Quit the application."""
        App.get_running_app().stop()
        Logger.info("App Quit")

    def open_color_menu_main(self, instance):
        """Open the color selection menu from the main menu."""
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        for index, color in COLOR_OPTIONS.items():
            btn = Button(text=f"Color {index}", size_hint=(1, None), height=50)
            btn.background_color = color + (1,)
            btn.bind(on_release=lambda btn, idx=index: self.select_color_main(idx))
            layout.add_widget(btn)
        popup = Popup(title='Select Color',
                      content=layout,
                      size_hint=(0.3, 0.5))
        popup.open()

    def select_color_main(self, color_index):
        """Set the selected color in the main menu."""
        app = App.get_running_app()
        if hasattr(app, 'selected_color'):
            app.selected_color = COLOR_OPTIONS[color_index]
            Logger.info(f"Main Menu: Color changed to index {color_index}")
        else:
            Logger.warning("App does not have 'selected_color' property.")

class DrawingPadScreen(Screen):
    """Screen that contains the DrawingPad widget and UI controls."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.drawing_pad = DrawingPad()
        self.add_widget(self.drawing_pad)

class SnakeApp(App):
    """Main application class."""
    version = '1.1'  # Updated version number
    selected_color = ListProperty([0, 1, 0])  # Default Green

    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainMenu(name='main_menu'))
        sm.add_widget(DrawingPadScreen(name='drawing_pad'))
        sm.current = 'main_menu'
        return sm

if __name__ == '__main__':
    SnakeApp().run()
