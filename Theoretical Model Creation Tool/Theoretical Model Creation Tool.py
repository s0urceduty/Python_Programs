# Theoretical Model Creation Tool

# Copyright (C) 2024, Sourceduty - All Rights Reserved.

# A terminal-based Python program for building and saving theoretical science models.
# Includes expanded concepts, attributes, dynamic states, relationships, and validation.

import os

def main():
    print_help_menu()
    while True:
        print("\nMain Menu:")
        print("1. Build Theoretical Model")
        print("2. View Help")
        print("3. Exit")
        main_choice = input("Enter your choice (1-3): ").strip()

        if main_choice == '1':
            select_architecture_level()
        elif main_choice == '2':
            print_help_menu()
        elif main_choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def print_help_menu():
    print("\nTheoretical Model Creation Tool")
    print("This program allows you to build detailed and customizable theoretical science models.")
    print("\nKey Features:")
    print("1. Four architecture levels: Super, High, Medium, and Low.")
    print("2. Customizable step types, descriptions, priorities, and theoretical parameters.")
    print("3. Define theoretical concepts with attributes and dynamic states.")
    print("4. Model the evolution of scientific processes with dynamic states.")
    print("5. Validate models for theoretical consistency and scientific validity.")
    print("6. Specify units, constants, error margins, and more.")
    print("\nHow to Use:")
    print("1. Select 'Build Theoretical Science Model' to start.")
    print("2. Follow prompts to add, customize, and manage concepts and steps.")
    print("3. Save the completed model.")
    print("4. Use 'View Help' for guidance.")

def select_architecture_level():
    print("\nSelect the Process Architecture Level:")
    levels = ["Super Level", "High Level", "Medium Level", "Low Level"]
    for i, level in enumerate(levels, start=1):
        print(f"{i}. {level}")
    try:
        level_choice = int(input("Enter your choice (1-4): ").strip())
        if 1 <= level_choice <= 4:
            build_science_model(levels[level_choice - 1])
        else:
            print("Invalid choice. Returning to main menu.")
    except ValueError:
        print("Invalid input. Returning to main menu.")

def build_science_model(level):
    print(f"\nBuilding a {level} Theoretical Science Model")
    science_model = []

    while True:
        print("\nModel Step Menu:")
        print("1. Add a new concept")
        print("2. Edit an existing concept")
        print("3. Add a new dynamic state")
        print("4. Define relationships between concepts")
        print("5. View current model")
        print("6. Validate the model")
        print("7. Finish and save model")
        step_choice = input("Enter your choice (1-7): ").strip()

        if step_choice == '1':
            add_concept(science_model)
        elif step_choice == '2':
            edit_concept(science_model)
        elif step_choice == '3':
            add_dynamic_state(science_model)
        elif step_choice == '4':
            define_relationships(science_model)
        elif step_choice == '5':
            display_model(science_model)
        elif step_choice == '6':
            validate_model(science_model)
        elif step_choice == '7':
            if science_model:
                display_model(science_model)
                save_option = input("Would you like to save this model to a file? (yes/no): ").strip().lower()
                if save_option == 'yes':
                    save_model(level, science_model)
            else:
                print("No steps to save. Returning to main menu.")
            break
        else:
            print("Invalid choice. Please try again.")

def add_concept(science_model):
    concept_name = input("Enter the name of the theoretical concept (e.g., 'Temperature', 'Force', 'Energy'): ").strip()
    print("Suggested Input: A key scientific idea like 'Gravitational Force', 'Acceleration', or 'Energy'.")
    
    concept_type = input("Enter the type of concept (e.g., 'Law', 'Force', 'Variable', 'System'): ").strip()
    print("Suggested Input: Choose a concept type like 'Law' (e.g., Newton's Law), 'Force' (e.g., Gravitational Force), or 'System'.")
    
    description = input("Enter a description for this concept (e.g., 'The force that attracts a body toward the center of the earth'): ").strip()
    print("Suggested Input: A concise explanation of the concept, e.g., 'The force that attracts objects to the Earth's surface.'")
    
    units = input("Enter units of measurement for this concept (e.g., 'kg', 'm/s²', 'Joules'): ").strip()
    print("Suggested Input: Include units for the concept, such as 'kg' for mass, 'm/s²' for acceleration, or 'Joules' for energy.")
    
    constants = input("Enter constants associated with this concept (e.g., 'G = 6.674×10⁻¹¹ N·m²/kg²'): ").strip()
    print("Suggested Input: If the concept has constants, enter them here (e.g., 'G = 6.674×10⁻¹¹ N·m²/kg²' for gravitational constant).")
    
    attributes = input("Enter additional attributes for this concept (e.g., 'mass = 5 kg, velocity = 10 m/s'): ").strip()
    print("Suggested Input: Provide any relevant attributes like 'mass = 5 kg', 'velocity = 10 m/s'.")

    concept = {
        "name": concept_name,
        "type": concept_type,
        "description": description,
        "units": units,
        "constants": constants,
        "attributes": attributes
    }
    
    science_model.append(concept)

def edit_concept(science_model):
    if not science_model:
        print("No concepts to edit. Add concepts first.")
        return
    display_model(science_model)
    try:
        index = int(input("Enter the position of the concept to edit (1-based index): ").strip()) - 1
        if 0 <= index < len(science_model):
            print(f"Editing concept: {science_model[index]['name']}")
            new_name = input("Enter the new name of the concept: ").strip()
            new_description = input("Enter the new description: ").strip()
            new_units = input("Enter the new units of measurement: ").strip()
            new_constants = input("Enter the new constants: ").strip()
            new_attributes = input("Enter the new attributes: ").strip()
            
            science_model[index]["name"] = new_name
            science_model[index]["description"] = new_description
            science_model[index]["units"] = new_units
            science_model[index]["constants"] = new_constants
            science_model[index]["attributes"] = new_attributes
            print("Concept edited successfully.")
        else:
            print("Invalid position. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def add_dynamic_state(science_model):
    if not science_model:
        print("No concepts to apply dynamic states. Add concepts first.")
        return
    display_model(science_model)
    concept_index = int(input("Enter the position of the concept to add a dynamic state (1-based index): ")) - 1
    if 0 <= concept_index < len(science_model):
        state_name = input("Enter the name of the dynamic state (e.g., 'Temperature', 'Pressure', 'Time'): ").strip()
        print("Suggested Input: Choose a state such as 'Temperature', 'Pressure', or 'Time' based on your concept.")
        state_value = input(f"Enter the value for {state_name} (e.g., '300 K', '1 atm', 't = 0'): ").strip()
        print("Suggested Input: Provide the current value, such as '300 K' for temperature or '1 atm' for pressure.")
        time_dependency = input("Is this state time-dependent? (yes/no): ").strip().lower()
        print("Suggested Input: If this value changes over time, enter 'yes'. Otherwise, enter 'no'.")
        
        dynamic_state = {
            "state_name": state_name,
            "value": state_value,
            "time_dependent": time_dependency == 'yes'
        }

        if "dynamic_states" not in science_model[concept_index]:
            science_model[concept_index]["dynamic_states"] = []

        science_model[concept_index]["dynamic_states"].append(dynamic_state)
        print(f"Dynamic state '{state_name}' added to concept '{science_model[concept_index]['name']}'.")
    else:
        print("Invalid concept. Please try again.")

def define_relationships(science_model):
    if len(science_model) < 2:
        print("Not enough concepts to define relationships. Add more concepts first.")
        return
    display_model(science_model)
    from_concept = int(input("Enter the position of the concept to define relationship from (1-based index): ")) - 1
    to_concept = int(input("Enter the position of the concept to define relationship to (1-based index): ")) - 1
    if 0 <= from_concept < len(science_model) and 0 <= to_concept < len(science_model):
        relationship = input("Enter the relationship description (e.g., 'affects', 'depends on', 'interacts with'): ").strip()
        print("Suggested Input: Relationships can be described as 'affects', 'depends on', 'interacts with', etc.")
        science_model[from_concept]["relationships"] = science_model.get("relationships", [])
        science_model[from_concept]["relationships"].append({
            "to": science_model[to_concept]["name"],
            "relationship": relationship
        })
        print(f"Relationship between '{science_model[from_concept]['name']}' and '{science_model[to_concept]['name']}' defined.")
    else:
        print("Invalid concepts. Please try again.")

def display_model(science_model):
    if not science_model:
        print("No concepts in the model yet.")
        return
    print("\nCurrent Science Model:")
    for concept in science_model:
        print(f"\nConcept: {concept['name']}")
        print(f"Type: {concept['type']}")
        print(f"Description: {concept['description']}")
        print(f"Units: {concept['units']}")
        print(f"Constants: {concept['constants']}")
        print(f"Attributes: {concept['attributes']}")
        if 'dynamic_states' in concept:
            print("Dynamic States:")
            for state in concept['dynamic_states']:
                print(f"- {state['state_name']} = {state['value']} (Time-dependent: {state['time_dependent']})")
        if 'relationships' in concept:
            print("Relationships:")
            for rel in concept['relationships']:
                print(f"- {concept['name']} {rel['relationship']} {rel['to']}")
                
def validate_model(science_model):
    if not science_model:
        print("No concepts to validate.")
        return
    print("\nValidating model...")
    for concept in science_model:
        print(f"Validating concept: {concept['name']}")
        if not concept["attributes"]:
            print(f"Warning: Concept '{concept['name']}' has no attributes defined.")
        if 'dynamic_states' in concept:
            for state in concept['dynamic_states']:
                if state['time_dependent'] and not state['value']:
                    print(f"Warning: Dynamic state '{state['state_name']}' is time-dependent but has no value.")
    print("Validation complete.")

def save_model(level, science_model):
    filename = input("Enter the filename to save the model (e.g., model.txt): ").strip()
    try:
        with open(filename, "w") as file:
            file.write(f"{level} Science Model\n")
            for concept in science_model:
                file.write(f"Concept: {concept['name']}\n")
                file.write(f"Type: {concept['type']}\n")
                file.write(f"Description: {concept['description']}\n")
                file.write(f"Units: {concept['units']}\n")
                file.write(f"Constants: {concept['constants']}\n")
                file.write(f"Attributes: {concept['attributes']}\n")
                if 'dynamic_states' in concept:
                    for state in concept['dynamic_states']:
                        file.write(f"Dynamic State: {state['state_name']} = {state['value']} (Time-dependent: {state['time_dependent']})\n")
                if 'relationships' in concept:
                    for rel in concept['relationships']:
                        file.write(f"Relationship: {concept['name']} {rel['relationship']} {rel['to']}\n")
            print(f"Model successfully saved to {filename}.")
    except Exception as e:
        print(f"Error saving file: {e}")

if __name__ == "__main__":
    main()
