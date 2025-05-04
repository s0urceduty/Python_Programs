# Decision_Data_Accumulator v2.0
# Sorting alphabetical user input with Python

# Copyright (c) 2023, Sourceduty
# https://about.me/sourceduty

# This software is free and open-source; anyone can redistribute it and/or modify it.


import re
import os
import json
import csv
from collections import defaultdict

# Initialize decision memory as a defaultdict with colors and decision counters
decision_memory = defaultdict(int)
total_decisions = 0

# Define the data file paths
data_file_json = "decision_data.json"
data_file_csv = "decision_data.csv"

# Load decision data from the JSON file if it exists
if os.path.exists(data_file_json):
    with open(data_file_json, "r") as json_file:
        decision_memory = json.load(json_file)

# Function to save decision data to a JSON file
def save_decision_data():
    with open(data_file_json, "w") as json_file:
        json.dump(dict(decision_memory), json_file)

# Function to export decision data to a CSV file
def export_decision_data_to_csv():
    with open(data_file_csv, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Color", "Decisions"])
        for color, count in decision_memory.items():
            csv_writer.writerow([color, count])

# Function to display a histogram of color decisions
def display_histogram():
    print("Decision Histogram:")
    for color, count in decision_memory.items():
        print(f"{color}: {'*' * count}")

# User input
print("Decision Data Accumulator V2.0")
print("------------------------------")

while True:
    user_input = input("Enter a color word (or 'exit' to quit, 'custom' to add a custom decision): ").strip()

    if user_input.lower() == 'exit':
        # Save decision data and exit
        save_decision_data()
        break
    elif user_input.lower() == 'custom':
        custom_color = input("Enter a custom color: ")
        if custom_color:
            # Increment the custom color's count
            decision_memory[custom_color] += 1
            total_decisions += 1
            print(f"Custom color '{custom_color}' added.")
        else:
            print("Invalid custom color.")
    else:
        if not user_input.isalpha():
            print("Please enter only alphabetical characters.")
            print("--------------------")
            print("Not Alphabetical.")
            print("--------------------")
        else:
            total_decisions += 1
            print("Data accepted.")
            print("--------------------")
            print("1. View Decision")
            print("2. View Decision Memory")
            print("3. Clear Decision Memory")
            print("4. View Decision Statistics")
            print("5. Export Decision Data to CSV")
            print("6. Display Decision Histogram")
            print("-------------------")
            choice = input("Enter function: ")

            yellow_decision = user_input.lower() == "yellow"

            if user_input == "":
                print("No input.")
                print("--------------------")

            if choice in ('1', '2', '3', '4', '5', '6'):
                print("----------------------")

                if choice == '1':
                    if yellow_decision:
                        print("Decision: Yellow")
                    else:
                        print("Decision: Not Yellow")
                    print("----------------------")
                elif choice == '2':
                    # View decision memory
                    print("Decision Memory:")
                    for color, count in decision_memory.items():
                        print(f"Color: {color}, Decisions: {count}")
                    print(f"Total Decisions: {total_decisions}")
                    print("----------------------")
                elif choice == '3':
                    # Clear decision memory
                    decision_memory.clear()
                    total_decisions = 0
                    print("Decision memory cleared")
                    print("----------------------")
                elif choice == '4':
                    # View decision statistics
                    display_histogram()
                    display_statistics()
                    print("----------------------")
                elif choice == '5':
                    # Export decision data to a CSV file
                    export_decision_data_to_csv()
                    print("Decision data exported to CSV.")
                    print("----------------------")
                elif choice == '6':
                    # Display a histogram of color decisions
                    display_histogram()
                    print("----------------------")
                else:
                    print("Invalid input")
            else:
                print("Invalid input")

# Display statistics before exiting
display_statistics()
input("Press enter to exit.")
