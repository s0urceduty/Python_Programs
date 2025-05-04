# Machine_Learning_Template
# 🤖 Multiple choice machine learning model developer tool.

# Create and customize machine learning model templates.

# Copyright (c) 2023, Sourceduty
# This software is free and open-source; anyone can redistribute it and/or modify it.

def save_user_choices_to_file(user_choices):
    with open("user_choices.txt", "w") as file:
        for category, choice in user_choices.items():
            file.write(f"Category: {category}\n{choice}\n")

def multiple_choice_form():
    choices = {
        "Intelligence Type": ["Artificial Narrow Intelligence", "Artificial General Intelligence", "Artificial Super Intelligence"],
        "Machine Learning Model": ["Supervised Learning", "Unsupervised Learning", "Reinforcement Learning"],
        "Machine Learning Type": [
            "Auditory Learning", "Episodic Learning", "Motor Learning",
            "Observational Learning", "Perceptual Learning", "Relational Learning",
            "Spatial Learning", "Stimulus-Response Learning"
        ],
        "Reasoning Type": [
            "Deductive", "Inductive", "Analogical", "Abductive",
            "Cause-and-effect", "Critical", "Decompositional"
        ],
        "Problem Solving Model": ["Regression", "Classification", "Clustering"]
    }

    user_choices = {}
    
    for choice, options in choices.items():
        print(f"Choice {len(user_choices) + 1}\nCategory: {choice}\n")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")

        while True:
            try:
                user_input = int(input("\nSelect an option by entering the corresponding number: "))
                if 1 <= user_input <= len(options):
                    user_choices[choice] = options[user_input - 1]
                    break
                else:
                    print("Invalid input. Please enter a valid option number.")
            except ValueError:
                print("Invalid input. Please enter a valid option number.")

    print("\nUser Choices:")
    for category, choice in user_choices.items():
        print(f"Category: {category}\n{choice}")

    # Save user choices to a .txt file
    save_user_choices_to_file(user_choices)

if __name__ == "__main__":
    multiple_choice_form()
