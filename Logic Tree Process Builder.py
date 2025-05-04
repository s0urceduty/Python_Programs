# Logic Tree Process Builder

# Copyright (C) 2024, Sourceduty
# All Rights Reserved.

# A terminal-based Python program for building and saving logic tree process models.
# Supports Super, High, Medium, and Low Process Architecture Levels.
# Features include hierarchical step management, descriptions, priorities, custom arrows, and validation.

import os

class ProcessStep:
    def __init__(self, name, step_type="[Standard]", description="", priority="", parent=None):
        self.name = name
        self.step_type = step_type
        self.description = description
        self.priority = priority
        self.children = []
        self.parent = parent
        self.arrow = "→"

    def add_child(self, child_step):
        self.children.append(child_step)

    def remove_child(self, child_step):
        self.children.remove(child_step)

    def display(self, level=0):
        indent = "    " * level
        print(f"{indent}{self.arrow} {self.name} {self.step_type}", end="")
        if self.description:
            print(f" - {self.description}", end="")
        if self.priority:
            print(f" (Priority: {self.priority})", end="")
        print()
        for child in self.children:
            child.display(level + 1)

def main():
    print_help_menu()
    while True:
        print("\nMain Menu:\n")
        print("1. Build Logic Tree Process Model")
        print("2. View Help")
        print("3. Exit\n")
        main_choice = input(">>> ").strip()

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
    print("\n================================= Logic Tree Process Builder =================================\n")
    print("This program allows you to build detailed and customized logic tree process models step-by-step.\n")
    print("===============================================================================================\n")
    print("\nKey Features:\n")
    print("1. Four architecture levels: Super, High, Medium, and Low.")
    print("2. Hierarchical step types, descriptions, priorities, and arrows.")
    print("3. Options to add, edit, delete, and navigate steps within the tree.")
    print("4. Save models to a text file in a structured format.\n")
    print("===============================================================================================\n")
    print("\nHow to Use:\n")
    print("1. Select 'Build Logic Tree Process Model' to start.")
    print("2. Choose the architecture level.")
    print("3. Navigate through the tree to add, edit, or delete steps.")
    print("4. View the current model at any time.")
    print("5. Save the completed model.\n")
    print("===============================================================================================\n")

def select_architecture_level():
    print("\nSelect the Process Architecture Level:")
    levels = ["Super Level", "High Level", "Medium Level", "Low Level"]
    for i, level in enumerate(levels, start=1):
        print(f"{i}. {level}")
    try:
        level_choice = int(input("Enter your choice (1-4): ").strip())
        if 1 <= level_choice <= 4:
            root = ProcessStep(name=levels[level_choice - 1])
            build_process_model(root)
        else:
            print("Invalid choice. Returning to main menu.")
    except ValueError:
        print("Invalid input. Returning to main menu.")

def build_process_model(root):
    current_step = root
    while True:
        print(f"\nCurrent Location: {get_step_path(current_step)}\n")
        print("Process Step Menu:")
        print("1. Add a new child step")
        print("2. Edit this step")
        print("3. Delete this step")
        print("4. Navigate to a child step")
        print("5. Navigate to parent step")
        print("6. View current model")
        print("7. Customize arrows for children")
        print("8. Finish and save model")
        step_choice = input("Enter your choice (1-8): ").strip()

        if step_choice == '1':
            add_step(current_step)
        elif step_choice == '2':
            edit_step(current_step)
        elif step_choice == '3':
            if current_step.parent:
                delete_step(current_step)
                current_step = current_step.parent
            else:
                print("Cannot delete the root step.")
        elif step_choice == '4':
            if current_step.children:
                current_step = navigate_to_child(current_step)
            else:
                print("No child steps to navigate to.")
        elif step_choice == '5':
            if current_step.parent:
                current_step = current_step.parent
            else:
                print("Already at the root step.")
        elif step_choice == '6':
            display_model(root)
        elif step_choice == '7':
            customize_arrows(current_step)
        elif step_choice == '8':
            if root:
                display_model(root)
                save_option = input("Would you like to save this model to a file? (yes/no): ").strip().lower()
                if save_option in ['yes', 'y']:
                    save_model(root)
            else:
                print("No steps to save. Returning to main menu.")
            break
        else:
            print("Invalid choice. Please try again.")

def add_step(current_step):
    step_name = input("Enter the name of the new process step: ").strip()
    step_type = select_step_type()
    description = input("Enter a description for this step (optional): ").strip()
    priority = input("Enter the priority for this step (High, Medium, Low, or leave blank): ").strip()

    new_step = ProcessStep(
        name=step_name,
        step_type=step_type,
        description=description,
        priority=priority,
        parent=current_step
    )
    current_step.add_child(new_step)
    print(f"Step '{step_name}' added successfully under '{current_step.name}'.")

def select_step_type():
    print("\nSelect step type:")
    step_types = {
        "1": "[Standard]",
        "2": "[Decision]",
        "3": "[Parallel]",
        "4": "[End]"
    }
    for key, value in step_types.items():
        print(f"{key}. {value}")
    choice = input("Enter your choice (1-4): ").strip()
    return step_types.get(choice, "[Standard]")

def edit_step(step):
    print(f"\nEditing Step: {step.name}")
    new_name = input(f"Enter new name (leave blank to keep '{step.name}'): ").strip()
    if new_name:
        step.name = new_name
    new_type = select_step_type()
    step.step_type = new_type
    new_description = input(f"Enter new description (leave blank to keep current): ").strip()
    if new_description:
        step.description = new_description
    new_priority = input(f"Enter new priority (High, Medium, Low, or leave blank to keep current): ").strip()
    if new_priority:
        step.priority = new_priority
    print("Step updated successfully.")

def delete_step(step):
    parent = step.parent
    if parent:
        parent.remove_child(step)
        print(f"Step '{step.name}' deleted successfully from '{parent.name}'.")
    else:
        print("Cannot delete the root step.")

def navigate_to_child(current_step):
    print("\nChild Steps:")
    for idx, child in enumerate(current_step.children, start=1):
        print(f"{idx}. {child.name} {child.step_type}")
    try:
        choice = int(input("Enter the number of the child step to navigate to: ").strip())
        if 1 <= choice <= len(current_step.children):
            return current_step.children[choice - 1]
        else:
            print("Invalid choice. Staying at current step.")
            return current_step
    except ValueError:
        print("Invalid input. Staying at current step.")
        return current_step

def display_model(root):
    print("\nCurrent Logic Tree Process Model:")
    root.display()

def get_step_path(step):
    path = []
    while step:
        path.insert(0, step.name)
        step = step.parent
    return " > ".join(path)

def customize_arrows(current_step):
    if not current_step.children:
        print("No child steps to customize arrows for.")
        return
    print("\nArrow Options:")
    arrows = {
        "1": "→",
        "2": "←",
        "3": "↔",
        "4": "⇄"
    }
    for key, value in arrows.items():
        print(f"{key}. {value}")
    choice = input("Select the arrow type (1-4): ").strip()
    arrow = arrows.get(choice, "→")
    for child in current_step.children:
        child.arrow = arrow
    print(f"Arrows for all child steps under '{current_step.name}' updated to '{arrow}'.")

def save_model(root):
    filename = input("Enter the filename to save the model (e.g., model.txt): ").strip()
    try:
        with open(filename, "w") as file:
            file.write(f"{root.name} Process Model\n")
            save_step(file, root)
        print(f"Model successfully saved to {filename}.")
    except Exception as e:
        print(f"Error saving file: {e}")

def save_step(file, step, level=0):
    indent = "    " * level
    file.write(f"{indent}{step.arrow} {step.name} {step.step_type}")
    if step.description:
        file.write(f" - {step.description}")
    if step.priority:
        file.write(f" (Priority: {step.priority})")
    file.write("\n")
    for child in step.children:
        save_step(file, child, level + 1)

if __name__ == "__main__":
    main()
