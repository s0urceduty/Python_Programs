# 30 Day Challenge Terminal
# Copyright (C) 2024, Sourceduty - All Rights Reserved.

import datetime
import time
import random

def load_tasks():
    return [
        "Write a blog post about the latest trends in your industry.",
        "Create a short video tutorial on a topic you are knowledgeable about.",
        "Design an infographic that explains a complex process related to your niche.",
        "Record a podcast episode discussing a current hot topic with a guest.",
        "Take a high-quality photo related to your content theme and post it with a detailed caption.",
        "Write a detailed product review for a product or service in your industry.",
        "Create a piece of digital art that could be used as a cover for your social media profiles.",
        "Develop and share a short story that ties into the theme of your content.",
        "Compose and publish a listicle (e.g., 'Top 10 Tips for...').",
        "Record and edit a day-in-the-life video or vlog.",
        "Host a live Q&A session on social media about a relevant topic.",
        "Create a how-to guide for a tool or technique you use frequently.",
        "Design and post a carousel on Instagram about a key topic.",
        "Develop a content calendar for the next month.",
        "Write and send out a newsletter update to your subscribers.",
        "Create a series of themed Instagram stories for engagement.",
        "Produce a comparison video or article between two popular products or services.",
        "Interview an expert in your field and publish the interview.",
        "Develop and share a case study related to your niche.",
        "Record a tutorial on how to use a specific software tool relevant to your audience.",
        "Write an opinion piece on a controversial topic within your niche.",
        "Create and share a motivational post tailored to your audience.",
        "Design a new logo or graphic for a segment of your content.",
        "Conduct and share a survey with your audience, then publish the results.",
        "Create a DIY project that your audience can follow along with.",
        "Develop a mini-course or educational series and begin releasing it.",
        "Organize and host a webinar on a subject of expertise.",
        "Write a detailed analysis of a recent event or development in your field.",
        "Create a portfolio piece that showcases your best work.",
        "Plan and execute a collaborative piece with another content creator."
    ]

def print_help_menu():
    print("30 Day Challenge Terminal: Content Creation\n")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
    print("Challenge youself with 30 days of digital content creation using this program.")
    print("1. Starting the Program: Run the program and it will automatically prompt you for today's task.")
    print("2. Completing a Task: When prompted, complete the task assigned for the day.")
    print("3. Adding Notes: After completing the task, you will be asked to enter any notes about the task.")
    print("4. Confirming Task Completion: Press enter once you have completed the task and added your notes.")
    print("5. Viewing Statistics: At any time, type 'stats' and press enter to view your progress.")
    print("6. Exiting: The program must be left open to operate correctly. Close it only when you are done with all 30 days.")
    print("7. Help: Type 'help' and press enter to view this menu again.\n")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
    print("Keep this program running daily to ensure you are prompted each day.\n")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

def main():
    log_file_name = "challenge_log.txt"
    open(log_file_name, "w").close()

    tasks = load_tasks()
    day = 1
    print_help_menu()

    while day <= 30:
        command = input("Enter 'next' to get today's task, 'stats' to view statistics, or 'help' for help menu: ").lower()
        if command == 'next':
            task = random.choice(tasks)
            prompt_for_task(day, task, log_file_name)
            day += 1
            if day > 30:
                print("Challenge completed! You can view the statistics with 'stats' or exit the program.")
        elif command == 'stats':
            show_statistics(log_file_name)
        elif command == 'help':
            print_help_menu()
        else:
            print("Invalid command. Please enter 'next', 'stats', or 'help'.")

def prompt_for_task(day, task, log_file_name):
    print(f"Day {day}: Today's task is: {task}")
    note = input("Enter your note about the task upon completion: ")
    input("Press enter when you have completed the task... ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_task_completion(day, task, note, timestamp, log_file_name)

def log_task_completion(day, task, note, timestamp, log_file_name):
    with open(log_file_name, "a") as file:
        file.write(f"Day {day}, Task: {task}, Note: {note}, Completed at: {timestamp}\n")

def show_statistics(log_file_name):
    try:
        with open(log_file_name, "r") as file:
            logs = file.readlines()
            completed_days = len(logs)
            print(f"Total days with completed tasks: {completed_days}/30")
    except FileNotFoundError:
        print("Log file does not exist. No statistics available.")

if __name__ == "__main__":
    main()