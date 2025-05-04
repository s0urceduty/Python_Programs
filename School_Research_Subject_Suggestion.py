import random

# Predefined list of research subjects
research_subjects = [
    "History",
    "Biology",
    "Physics",
    "Chemistry",
    "Computer Science",
    "Literature",
    "Mathematics",
    "Geography",
    "Economics",
    "Psychology",
]

# Function to suggest a research subject
def suggest_research_subject():
    return random.choice(research_subjects)

# Main function to provide suggestions
def main():
    print("Welcome to School Research Subject Suggestions!")
    while True:
        input("Press Enter to get a research subject suggestion...")
        suggested_subject = suggest_research_subject()
        print(f"Research Subject: {suggested_subject}")
        another = input("Do you want another suggestion? (yes/no): ").strip().lower()
        if another != "yes":
            break

if __name__ == "__main__":
    main()
