# Military Terminal Program V1.2
# Copyright (C) 2024, Sourceduty - All Rights Reserved.

import time
from calendar import isleap

# Function to display the startup screen
def display_startup_screen():
    print("+++++++++++++++++++++++++++++++++++++++++++++++ ARMY TERMINAL V1.2 +++++++++++++++++++++++++++++++++++++++++++++++\n")
    print("⠀                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣄⣠⣀⡀⣀⣠⣤⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⢠⣠⣼⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⢠⣤⣦⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀                ⠀⠀⠀⠀⠀            ⠀⠀⣼⣿⣟⣾⣿⣽⣿⣿⣅⠈⠉⠻⣿⣿⣿⣿⣿⡿⠇⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⢀⡶⠒⢉⡀⢠⣤⣶⣶⣿⣷⣆⣀⡀⠀⢲⣖⠒⠀⠀⠀⠀⠀")
    print("                            ⢀⣤⣾⣶⣦⣤⣤⣶⣿⣿⣿⣿⣿⣿⣽⡿⠻⣷⣀⠀⢻⣿⣿⣿⡿⠟⠀⠀⠀⠀⠀⠀⣤⣶⣶⣤⣀⣀⣬⣷⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣤⣦⣼⣀⠀")
    print("                            ⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠓⣿⣿⠟⠁⠘⣿⡟⠁⠀⠘⠛⠁⠀⠀⢠⣾⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠏⠙⠁")
    print("                            ⠀⠸⠟⠋⠀⠈⠙⣿⣿⣿⣿⣿⣿⣷⣦⡄⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⣼⣆⢘⣿⣯⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡉⠉⢱⡿⠀⠀⠀⠀⠀")
    print("⠀                            ⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡿⠦⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡗⠀⠈⠀⠀⠀⠀⠀⠀")
    print("⠀                            ⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣉⣿⡿⢿⢷⣾⣾⣿⣞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⣠⠟⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀                            ⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⠿⠿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣾⣿⣿⣷⣦⣶⣦⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠈⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣤⡖⠛⠶⠤⡀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠙⣿⣿⠿⢻⣿⣿⡿⠋⢩⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠧⣤⣦⣤⣄⡀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠘⣧⠀⠈⣹⡻⠇⢀⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣤⣀⡀⠀⠀⠀⠀⠀⠀⠈⢽⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⣴⣿⣷⢲⣦⣤⡀⢀⡀⠀⠀⠀⠀⠀⠀")
    print("⠀                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣷⢀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠂⠛⣆⣤⡜⣟⠋⠙⠂⠀⠀⠀⠀⠀")
    print("⠀                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⠉⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣾⣿⣿⣿⣿⣆⠀⠰⠄⠀⠉⠀⠀")
    print("⠀⠀                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⠿⠿⣿⣿⣿⠇⠀⠀⢀⠀⠀⠀")
    print("⠀⠀⠀⠀            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                ⠀⢀⣿⡿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⡇⠀⠀⢀⣼⠗⠀⠀")
    print("⠀⠀⠀⠀⠀⠀            ⠀⠀                ⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠃⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠁⠀⠀⠀")
    print("⠀                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠒⠀⠀⠀\n⠀")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++> INTERNATIONAL +++++++++++++++++++++++++++++++++++++++++++++++++\n")
    print("++ ID: 439211 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 1984-6-14 ++\n")
                
# Function to calculate days between two dates
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    dom = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    domleap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (isleap(year1) and isleap(year2)):
        e1 = sum(domleap) + sum(domleap[:month1 - 1]) + day1
        e2 = sum(domleap) + sum(domleap[:month2 - 1]) + day2
        return e2 - e1

    days = 0
    if isleap(year1):
        days += (sum(domleap[month1 - 1:]) - day1) + sum(dom[:month2 - 1]) + day2
    elif isleap(year2):
        days += (sum(dom[month1 - 1:]) - day1) + sum(domleap[:month2 - 1]) + day2
    else:
        days += (sum(dom[month1 - 1:]) - day1) + sum(dom[:month2 - 1]) + day2
    for year in range(year1 + 1, year2):
        if isleap(year):
            days += sum(domleap)
        else:
            days += sum(dom)
    return days

# Function to decode Morse code
def decodeMorse(morseCode):
    morse_code = {
        ".-" : "A", "-..." : "B", "-.-." : "C", "-.." : "D", "." : "E", "..-." : "F", "--." : "G", "...." : "H", 
        ".." : "I", ".---" : "J", "-.-" : "K", ".-.." : "L", "--" : "M", "-." : "N", "---" : "O", ".--." : "P", 
        "--.-" : "Q", ".-." : "R", "..." : "S", "-" : "T", "..-" : "U", "...-" : "V", ".--" : "W", "-..-" : "X", 
        "-.--" : "Y", "--.." : "Z", ".----" : "1", "..---" : "2", "...--" : "3", "....-" : "4", "....." : "5", 
        "-...." : "6", "--..." : "7", "---.." : "8", "----." : "9", "-----" : "0", "SPACE" : " "
    }
    morseCode = morseCode.strip()
    new = morseCode.replace("   ", " SPACE ")
    prep = new.split()
    res = ""
    li = list(morse_code.keys())
    for n in prep:
        if n in li:
            res = res + morse_code[n]
        else:
            pass
    return res.strip()

# Function to display NATO phonetic alphabet
def display_nato_phonetic_alphabet():
    alphabet = {
        'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo', 'F': 'Foxtrot', 
        'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliett', 'K': 'Kilo', 'L': 'Lima', 
        'M': 'Mike', 'N': 'November', 'O': 'Oscar', 'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 
        'S': 'Sierra', 'T': 'Tango', 'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray', 
        'Y': 'Yankee', 'Z': 'Zulu'
    }
    print("\nNATO Phonetic Alphabet:\n")
    for letter, code in alphabet.items():
        print(f"{letter} ~ {code}")

# Main menu with new subcommands
def display_main_menu():
    print("+----------------------------------+---------+------------------------+----------------+")
    print("|             Sectors              |  Code   |         Short          |     Number     |")
    print("+----------------------------------+---------+------------------------+----------------+")
    sectors = [
        ("Management", "G0001", "Tango-Five-One", "89.5-A"),
        ("Radar", "G0002", "Tango-Four-Two", "1.43-B"),
        ("Inventory", "G0003", "Tango-Eight-Two", "54.5-C"),
        ("Missions", "G0004", "Tango-Two-Six", "63.1-D"),
        ("Plans", "G0005", "Tango-Nine-Two", "5.54-E"),
        ("Reroute", "G0006", "Tango-Seven-One", "43.1-F"),
        ("Defense", "G0007", "Tango-Three-Zero", "22.4-G"),
    ]
    for sector in sectors:
        print(f"| {sector[0]:<32} | {sector[1]:<7} | {sector[2]:<22} | {sector[3]:<14} |")
    print("+----------------------------------+---------+------------------------+----------------+")

# Subcommands for operations
def operations_menu():
    print("\nOperations Menu:")
    print("[A] Operations - Mission Briefings, Strategy Planning")
    print("[B] Communications - Secure Messaging, Radio Frequencies")
    print("[C] Navigation - Map Overlays, Coordinates Entry")
    print("[D] Logistics - Supply Inventory, Transport Requests")
    print("[E] Intelligence - Recon Reports, Data Analysis")
    print("[F] Emergency - Distress Signals, Medical Assistance")
    print("[G] Decode Morse Code - Signaling, Communications")

# Function to simulate terminal interaction
def terminal_interface():
    display_startup_screen()
    display_main_menu()

    while True:
        print("\n[[[[[================================< COMMAND CENTER INTERFACE >================================]]]]]\n")
        print("DATE: 2023-11-25 [][][]")
        print("OPERATIONAL STATUS: ACTIVE [GREEN] [][][]\n")
        
        operation = input("Choose Operation: [A/B/C/D/E/F/G] or type 'HELP' for assistance\n>> ").upper()
        
        if operation == 'HELP':
            operations_menu()
        elif operation == 'A':
            print("Operation A selected: Operations - Mission Briefings, Strategy Planning")
        elif operation == 'B':
            print("Operation B selected: Communications - Secure Messaging, Radio Frequencies")
        elif operation == 'C':
            print("Operation C selected: Navigation - Map Overlays, Coordinates Entry")
        elif operation == 'D':
            print("Operation D selected: Logistics - Supply Inventory, Transport Requests")
        elif operation == 'E':
            print("Operation E selected: Intelligence - Recon Reports, Data Analysis")
        elif operation == 'F':
            print("Operation F selected: Emergency - Distress Signals, Medical Assistance")
        elif operation == 'G':
            morse_input = input("Enter Morse Code to decode (separate letters with space and words with '   '):\n>> ")
            print("Decoded Message: ", decodeMorse(morse_input))
        else:
            print("Invalid selection. Type 'HELP' for available operations.")
        
        # Pause before displaying the terminal interface again
        time.sleep(2)
        
        # Ask the user if they want to continue or exit
        continue_option = input("\nDo you wish to continue? [Y/N]: ").upper()
        if continue_option != 'Y':
            print("Exiting the terminal interface.")
            break

# Run the terminal interface
terminal_interface()