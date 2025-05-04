# Travel Notepad V1.0
# Copyright (C) 2024, Sourceduty

import tkinter as tk
from tkinter import font, colorchooser, simpledialog, messagebox
from tkinter import filedialog
import requests
from datetime import datetime
import pytz

# Constants
LANGUAGES = {
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Chinese": "zh-cn",
    "Japanese": "ja",
    "Russian": "ru",
    "Italian": "it"
}

TEMPLATES = {
    "Travel": {
        "Places of Interest": "Places of Interest\nLocation: \n\nDescription:\n\nNotes:\n- \n- \n",
        "Journal": "Travel Journal\nDate: \n\nLocation: \n\nEvents:\n- \n- \n\nThoughts:\n- \n- \n",
        "Schedule": "Travel Schedule\nDate: \n\nActivities:\n1. \n2. \n3. \n\nNotes:\n- \n- \n",
        "Contacts": "Important Contacts\nName: \nPhone: \nEmail: \n\nAddress: \n\nNotes:\n- \n- \n",
        "mpg Calculation": "MPG Calculation\nDistance Traveled: \nFuel Used: \n\nMPG:\n",
        "Luggage Weight": "Luggage Weight Calculation\nItem: \nWeight: \n\nTotal Weight:\n",
    },
    "Custom Templates": {}
}

COUNTRIES_GUIDE = {
    "USA": "US",
    "Canada": "CA",
    "Germany": "DE",
    "France": "FR",
    "Japan": "JP",
    # Add more countries as needed
}

LANDMARKS_GUIDE = {
    "USA": "Statue of Liberty, Grand Canyon, Yellowstone",
    "Canada": "CN Tower, Niagara Falls, Banff National Park",
    "Germany": "Brandenburg Gate, Neuschwanstein Castle, Berlin Wall",
    "France": "Eiffel Tower, Louvre Museum, Notre-Dame Cathedral",
    "Japan": "Mount Fuji, Tokyo Tower, Kyoto Temples",
    # Add more landmarks as needed
}

TRAIN_STATIONS_GUIDE = {
    "USA": "New York Penn Station, Chicago Union Station, Los Angeles Union Station",
    "Canada": "Toronto Union Station, Vancouver Pacific Central Station, Montreal Central Station",
    "Germany": "Berlin Hauptbahnhof, Munich Hauptbahnhof, Frankfurt Hauptbahnhof",
    "France": "Gare du Nord, Gare de Lyon, Gare Montparnasse",
    "Japan": "Tokyo Station, Kyoto Station, Osaka Station",
    # Add more stations as needed
}

LUGGAGE_GUIDE = {
    "Domestic": "Carry-on: Max 22 x 14 x 9 inches (56 x 36 x 23 cm), Checked Bag: Max 62 linear inches (158 cm)",
    "International": "Carry-on: Max 21.5 x 15.5 x 9 inches (55 x 40 x 23 cm), Checked Bag: Max 50 lbs (23 kg)",
    # Add more details as needed
}

CURRENCY_API_URL = "https://api.exchangerate-api.com/v4/latest/USD"

class TravelNotepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Travel Notepad")
        self.root.geometry("800x600")

        # Text widget
        self.text_area = tk.Text(self.root, wrap='word')
        self.text_area.pack(expand='yes', fill='both')

        # Menu Bar
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # File Menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_app)

        # Control Menu
        self.control_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Control", menu=self.control_menu)

        # Control Submenus
        self.format_menu = tk.Menu(self.control_menu, tearoff=0)
        self.control_menu.add_cascade(label="Format", menu=self.format_menu)
        self.format_menu.add_command(label="Change Font", command=self.change_font)
        self.format_menu.add_command(label="Change Color", command=self.change_color)
        self.format_menu.add_command(label="Color Modes", command=self.select_color_mode)

        self.translate_menu = tk.Menu(self.control_menu, tearoff=0)
        self.control_menu.add_cascade(label="Translate", menu=self.translate_menu)
        for lang in LANGUAGES.keys():
            self.translate_menu.add_command(label=f"To {lang}", command=lambda l=lang: self.translate_text(l))

        self.tools_menu = tk.Menu(self.control_menu, tearoff=0)
        self.control_menu.add_cascade(label="Tools", menu=self.tools_menu)
        self.tools_menu.add_command(label="MPG Calculator", command=self.mpg_calculator)
        self.tools_menu.add_command(label="Luggage Weight Calculator", command=self.luggage_weight_calculator)
        self.tools_menu.add_command(label="Timezone Calculator", command=self.timezone_calculator)
        self.tools_menu.add_command(label="Currency Converter", command=self.currency_converter)

        self.templates_menu = tk.Menu(self.control_menu, tearoff=0)
        self.control_menu.add_cascade(label="Templates", menu=self.templates_menu)
        for category in TEMPLATES.keys():
            category_menu = tk.Menu(self.templates_menu, tearoff=0)
            for template in TEMPLATES[category]:
                category_menu.add_command(label=template, command=lambda t=template: self.load_template(category, t))
            self.templates_menu.add_cascade(label=category, menu=category_menu)

        self.country_guide_menu = tk.Menu(self.control_menu, tearoff=0)
        self.control_menu.add_cascade(label="Country Guide", menu=self.country_guide_menu)
        self.country_guide_menu.add_command(label="Countries and Abbreviations", command=self.show_countries)
        self.country_guide_menu.add_command(label="Landmarks", command=self.show_landmarks)
        self.country_guide_menu.add_command(label="Train Stations", command=self.show_train_stations)
        self.country_guide_menu.add_command(label="Luggage Guide", command=self.show_luggage_guide)

        # Status Bar
        self.status_bar = tk.Label(self.root, text="Ready", anchor='w')
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        # Insert default description
        self.insert_default_description()

    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.status_bar.config(text="New File")

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r') as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.INSERT, file.read())
            self.status_bar.config(text=f"Opened {file_path}")

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"),
                                                            ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.text_area.get(1.0, tk.END))
            self.status_bar.config(text=f"Saved {file_path}")

    def exit_app(self):
        self.root.quit()

    def change_font(self):
        font_choice = simpledialog.askstring("Font", "Enter font name:")
        size_choice = simpledialog.askinteger("Size", "Enter font size:")
        if font_choice and size_choice:
            new_font = font.Font(family=font_choice, size=size_choice)
            self.text_area.config(font=new_font)

    def change_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.text_area.config(fg=color)

    def select_color_mode(self):
        color_mode = simpledialog.askstring("Color Mode", "Enter color mode (white, black, blue, green):")
        if color_mode == "white":
            self.set_white_black()
        elif color_mode == "black":
            self.set_black_white()
        elif color_mode == "blue":
            self.set_blue_white()
        elif color_mode == "green":
            self.set_green_white()
        else:
            messagebox.showerror("Color Mode Error", "Invalid color mode selected.")

    def translate_text(self, language):
        lang_code = LANGUAGES[language]
        text = self.text_area.get(1.0, tk.END)
        if text.strip():
            translated_text = f"Translated text in {language} ({lang_code})"  # Placeholder for actual translation logic
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, translated_text)
            self.status_bar.config(text=f"Text translated to {language}")
        else:
            messagebox.showerror("Translation Error", "No text to translate.")

    def mpg_calculator(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("MPG Calculator")

        tk.Label(dialog, text="Distance Traveled (miles):").pack()
        distance_entry = tk.Entry(dialog)
        distance_entry.pack()

        tk.Label(dialog, text="Fuel Used (gallons):").pack()
        fuel_entry = tk.Entry(dialog)
        fuel_entry.pack()

        def calculate_mpg():
            try:
                distance = float(distance_entry.get())
                fuel = float(fuel_entry.get())
                mpg = distance / fuel
                result_label.config(text=f"MPG: {mpg:.2f}")
            except ValueError:
                result_label.config(text="Invalid input. Please enter numeric values.")

        tk.Button(dialog, text="Calculate MPG", command=calculate_mpg).pack()
        result_label = tk.Label(dialog, text="")
        result_label.pack()

    def luggage_weight_calculator(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Luggage Weight Calculator")

        tk.Label(dialog, text="Item:").pack()
        item_entry = tk.Entry(dialog)
        item_entry.pack()

        tk.Label(dialog, text="Weight (kg):").pack()
        weight_entry = tk.Entry(dialog)
        weight_entry.pack()

        def calculate_weight():
            try:
                weight = float(weight_entry.get())
                result_label.config(text=f"Weight: {weight:.2f} kg")
            except ValueError:
                result_label.config(text="Invalid input. Please enter a numeric value.")

        tk.Button(dialog, text="Calculate Weight", command=calculate_weight).pack()
        result_label = tk.Label(dialog, text="")
        result_label.pack()

    def timezone_calculator(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Timezone Calculator")

        tk.Label(dialog, text="Enter your timezone (e.g., 'Europe/London')").pack()
        tz_entry = tk.Entry(dialog)
        tz_entry.pack()

        def display_time():
            timezone = tz_entry.get()
            try:
                tz = pytz.timezone(timezone)
                local_time = datetime.now(tz)
                result_label.config(text=f"Local Time: {local_time.strftime('%Y-%m-%d %H:%M:%S')}")
            except pytz.UnknownTimeZoneError:
                result_label.config(text="Unknown timezone. Please enter a valid timezone.")

        tk.Button(dialog, text="Get Time", command=display_time).pack()
        result_label = tk.Label(dialog, text="")
        result_label.pack()

    def currency_converter(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Currency Converter")

        tk.Label(dialog, text="Amount in USD:").pack()
        amount_entry = tk.Entry(dialog)
        amount_entry.pack()

        tk.Label(dialog, text="To Currency Code (e.g., 'EUR')").pack()
        currency_entry = tk.Entry(dialog)
        currency_entry.pack()

        def convert_currency():
            amount = amount_entry.get()
            currency_code = currency_entry.get()
            try:
                amount = float(amount)
                response = requests.get(CURRENCY_API_URL)
                data = response.json()
                rates = data.get('rates', {})
                if currency_code in rates:
                    converted_amount = amount * rates[currency_code]
                    result_label.config(text=f"Converted Amount: {converted_amount:.2f} {currency_code}")
                else:
                    result_label.config(text="Invalid currency code.")
            except ValueError:
                result_label.config(text="Invalid amount. Please enter a numeric value.")
            except requests.RequestException:
                result_label.config(text="Error fetching currency rates.")

        tk.Button(dialog, text="Convert", command=convert_currency).pack()
        result_label = tk.Label(dialog, text="")
        result_label.pack()

    def show_countries(self):
        country_list = "\n".join([f"{country}: {abbr}" for country, abbr in COUNTRIES_GUIDE.items()])
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, f"Countries and Abbreviations:\n{country_list}")

    def show_landmarks(self):
        landmarks_list = "\n".join([f"{country}: {landmarks}" for country, landmarks in LANDMARKS_GUIDE.items()])
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, f"Landmarks:\n{landmarks_list}")

    def show_train_stations(self):
        stations_list = "\n".join([f"{country}: {stations}" for country, stations in TRAIN_STATIONS_GUIDE.items()])
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, f"Train Stations:\n{stations_list}")

    def show_luggage_guide(self):
        luggage_guide = "\n".join([f"{type}: {details}" for type, details in LUGGAGE_GUIDE.items()])
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, f"Luggage Weight and Size Guide:\n{luggage_guide}")

    def set_white_black(self):
        self.text_area.config(bg="white", fg="black")

    def set_black_white(self):
        self.text_area.config(bg="black", fg="white")

    def set_blue_white(self):
        self.text_area.config(bg="blue", fg="white")

    def set_green_white(self):
        self.text_area.config(bg="green", fg="white")

    def load_template(self, category, template_name):
        template = TEMPLATES[category][template_name]
        self.text_area.insert(tk.INSERT, template)
        self.status_bar.config(text=f"Loaded {template_name} template")

    def insert_default_description(self):
        default_description = (
            "Travel Notepad V1.0\n"
            "\nWelcome to the Travel Notepad by Sourceduty! This application is designed to help you manage and document all aspects of your travels. From tracking your travel schedule and important contacts to calculating MPG and luggage weight, this notepad is equipped with features to enhance your travel experience.\n"
            "\nFeatures:\n"
            "\nTemplates:\n"
            "  - Places of Interest: Document notable locations with descriptions and notes.\n"
            "  - Travel Journal: Record daily events and thoughts.\n"
            "  - Travel Schedule: Organize your travel activities and notes.\n"
            "  - Important Contacts: Keep track of essential contact details.\n"
            "  - MPG Calculation: Calculate the fuel efficiency of your vehicle.\n"
            "  - Luggage Weight Calculation: Monitor the weight of your luggage.\n"
            "\nTools:\n"
            "  - Translate: Translate text into various languages.\n"
            "  - MPG Calculator: Calculate miles per gallon for fuel efficiency.\n"
            "  - Luggage Weight Calculator: Track and calculate the weight of your luggage.\n"
            "  - Timezone Calculator: Determine local time in different timezones.\n"
            "  - Currency Converter: Convert amounts between currencies.\n"
            "\nCountry Guide:\n"
            "  - Countries and Abbreviations: View a list of countries and their abbreviations.\n"
            "  - Landmarks: Explore notable landmarks in each country.\n"
            "  - Train Stations: Find major train station locations in different countries.\n"
            "  - Luggage Guide: Access guidelines for luggage weight and size.\n"
            "\nColor Modes:\n"
            "  - Choose from various color modes to suit your preferences and environment.\n"
        )
        self.text_area.insert(tk.END, default_description)

if __name__ == "__main__":
    root = tk.Tk()
    app = TravelNotepad(root)
    root.mainloop()
