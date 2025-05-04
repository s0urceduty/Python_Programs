# Nokia 3210 Cellphone OS Emulator
# The Nokia 3210, released in 1999, ran on Nokia's proprietary operating system.

import time

class Nokia3210:
    def __init__(self):
        self.contacts = {}
        self.messages = []
        self.alarms = []
        self.calendar = []
        self.current_profile = "General"
        self.wallpaper = "Default"
        self.phone_on = True

    def main_menu(self):
        while self.phone_on:
            print("\n=== Nokia 3210 Emulator ===")
            print("1. Phonebook")
            print("2. Messages")
            print("3. Calls")
            print("4. Settings")
            print("5. Games")
            print("6. Utilities")
            print("7. Reset to Factory Settings")
            print("8. Turn Off")
            choice = input("Select an option: ")

            if choice == "1":
                self.phonebook_menu()
            elif choice == "2":
                self.messages_menu()
            elif choice == "3":
                self.calls_menu()
            elif choice == "4":
                self.settings_menu()
            elif choice == "5":
                self.games_menu()
            elif choice == "6":
                self.utilities_menu()
            elif choice == "7":
                self.reset_factory_settings()
            elif choice == "8":
                self.turn_off()
            else:
                print("Invalid choice. Try again.")

    def phonebook_menu(self):
        while True:
            print("\n--- Phonebook ---")
            print("1. View Contacts")
            print("2. Add Contact")
            print("3. Back")
            choice = input("Select an option: ")
            if choice == "1":
                self.view_contacts()
            elif choice == "2":
                self.add_contact()
            elif choice == "3":
                break
            else:
                print("Invalid choice.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for name, number in self.contacts.items():
                print(f"{name}: {number}")

    def add_contact(self):
        name = input("Enter name: ")
        number = input("Enter number: ")
        self.contacts[name] = number
        print("Contact added.")

    def messages_menu(self):
        while True:
            print("\n--- Messages ---")
            print("1. View Messages")
            print("2. Send Message")
            print("3. Back")
            choice = input("Select an option: ")
            if choice == "1":
                self.view_messages()
            elif choice == "2":
                self.send_message()
            elif choice == "3":
                break
            else:
                print("Invalid choice.")

    def view_messages(self):
        if not self.messages:
            print("No messages.")
        else:
            for i, message in enumerate(self.messages, 1):
                print(f"{i}. {message}")

    def send_message(self):
        recipient = input("Enter recipient: ")
        text = input("Enter message: ")
        self.messages.append(f"To {recipient}: {text}")
        print("Message sent.")

    def calls_menu(self):
        print("\n--- Calls ---")
        print("1. Dial Number")
        print("2. Back")
        choice = input("Select an option: ")
        if choice == "1":
            number = input("Enter number to call: ")
            print(f"Calling {number}...")
        elif choice == "2":
            return
        else:
            print("Invalid choice.")

    def settings_menu(self):
        while True:
            print("\n--- Settings ---")
            print("1. Change Ringtone")
            print("2. Change Profile")
            print("3. Change Wallpaper")
            print("4. Back")
            choice = input("Select an option: ")
            if choice == "1":
                self.change_ringtone()
            elif choice == "2":
                self.change_profile()
            elif choice == "3":
                self.change_wallpaper()
            elif choice == "4":
                break
            else:
                print("Invalid choice.")

    def change_ringtone(self):
        print("Ringtone changed.")

    def change_profile(self):
        print("Available profiles: General, Silent, Outdoor")
        self.current_profile = input("Select a profile: ")
        print(f"Profile changed to {self.current_profile}.")

    def change_wallpaper(self):
        self.wallpaper = input("Enter new wallpaper name: ")
        print(f"Wallpaper changed to {self.wallpaper}.")

    def games_menu(self):
        print("\n--- Games ---")
        print("1. Play Snake")
        print("2. Back")
        choice = input("Select an option: ")
        if choice == "1":
            self.snake_game()
        elif choice == "2":
            return
        else:
            print("Invalid choice.")

    def snake_game(self):
        print("Starting Snake... Press 'q' to quit.")
        length = 1
        while True:
            move = input("Press Enter to move (q to quit): ")
            if move.lower() == 'q':
                break
            length += 1
            print(f"Snake length: {length}")
        print("Game Over.")

    def utilities_menu(self):
        while True:
            print("\n--- Utilities ---")
            print("1. Alarm")
            print("2. Calendar")
            print("3. Calculator")
            print("4. Back")
            choice = input("Select an option: ")
            if choice == "1":
                self.alarm_menu()
            elif choice == "2":
                self.calendar_menu()
            elif choice == "3":
                self.calculator()
            elif choice == "4":
                break
            else:
                print("Invalid choice.")

    def alarm_menu(self):
        time = input("Set alarm (HH:MM): ")
        self.alarms.append(time)
        print(f"Alarm set for {time}.")

    def calendar_menu(self):
        while True:
            print("\n--- Calendar ---")
            print("1. View Events")
            print("2. Add Event")
            print("3. Back")
            choice = input("Select an option: ")
            if choice == "1":
                self.view_events()
            elif choice == "2":
                self.add_event()
            elif choice == "3":
                break
            else:
                print("Invalid choice.")

    def view_events(self):
        if not self.calendar:
            print("No events scheduled.")
        else:
            for event in self.calendar:
                print(event)

    def add_event(self):
        event = input("Enter event details: ")
        self.calendar.append(event)
        print("Event added.")

    def calculator(self):
        print("Simple Calculator:")
        try:
            result = eval(input("Enter calculation (e.g., 2+2): "))
            print(f"Result: {result}")
        except:
            print("Invalid calculation.")

    def reset_factory_settings(self):
        confirm = input("Are you sure? This will erase all data (y/n): ")
        if confirm.lower() == 'y':
            self.contacts.clear()
            self.messages.clear()
            self.alarms.clear()
            self.calendar.clear()
            self.current_profile = "General"
            self.wallpaper = "Default"
            print("Factory settings restored.")

    def turn_off(self):
        print("Turning off...")
        self.phone_on = False

if __name__ == "__main__":
    emulator = Nokia3210()
    emulator.main_menu()
