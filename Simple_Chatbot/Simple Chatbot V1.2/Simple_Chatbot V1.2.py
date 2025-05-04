# Simple Chatbot V1.2
#🤖 Text-based conversational chatbot.

# Copyright (c) 2023, Sourceduty
# This software is free and open-source; anyone can redistribute it and/or modify it.

import random

cmd_Greet = ["hello", "hi", "hey", "chatbot", "respond"]
rply_Greet = ["Hello", "Greetings!", "How can chatbot help you?"]

cmd_Leave = ["bye", "chatbot sleep", "goodbye"]
rply_Leave = ["Goodbye", "Take care!", "See you later!"]

cmd_Ask = ["name", "identify"]
rply_Ask = ["My name is Chatbot", "I'm Chatbot, your virtual assistant."]

cmd_Sad = ["bad", "sad", "not feeling well", "unhappy", "depressed"]
rply_Sad = ["I'm here to chat and cheer you up!", "Let's talk about something to make you feel better.", "I'm sorry to hear that. How can I help?"]

cmd_Happy = ["happy", "good", "joyful", "calm", "great", "amazing", "awesome"]
rply_Happy = ["I'm glad to hear that!", "What's making you feel so happy?", "That's fantastic!"]

cmd_Bored = ["boring", "bored", "bore", "nothing to do"]
rply_Bored = [
    "Watch some stand-up comedy videos.",
    "Install a new game.",
    "Try learning a new skill or hobby.",
    "Take a nap to recharge.",
    "How about reading a book?",
    "Explore a new hobby or craft project.",
    "Call or chat with a friend for some fun conversation."
]

cmd_Food = ["hungry", "food", "eat", "dinner"]
rply_Food = [
    "What type of cuisine are you in the mood for?",
    "Cook something delicious at home or order your favorite takeout.",
    "I can suggest some recipes if you'd like!",
    "Eating a healthy meal can lift your spirits. What's your favorite dish?"
]

cmd_Weather = ["weather", "forecast", "temperature"]
rply_Weather = ["I can provide you with the current weather for your location. Please share your city or zip code."]

def chatbot(text):
    for word in text.split():
        if word in cmd_Bored:
            response = random.choice(rply_Bored)
            print(response)
            return response
        elif word in cmd_Leave:
            response = random.choice(rply_Leave)
            print(response)
            return response
        elif word in cmd_Ask:
            response = random.choice(rply_Ask)
            print(response)
            return response
        elif word in cmd_Sad:
            response = random.choice(rply_Sad)
            print(response)
            return response
        elif word in cmd_Happy:
            response = random.choice(rply_Happy)
            print(response)
            return response
        elif word in cmd_Greet:
            response = random.choice(rply_Greet)
            print(response)
            return response
        elif word in cmd_Food:
            response = random.choice(rply_Food)
            print(response)
            return response
        elif word in cmd_Weather:
            response = random.choice(rply_Weather)
            print(response)
            return response
    print("Invalid entry.")
    return False

def number_guess_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("Let's play a number guessing game. I'm thinking of a number between 1 and 100.")

    while True:
        guess = input("Take a guess: ")
        try:
            guess = int(guess)
            attempts += 1

            if guess < number_to_guess:
                print("Higher! Try again.")
            elif guess > number_to_guess:
                print("Lower! Try again.")
            else:
                print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

def main():
    print("Simple Chatbot V1.2")
    print("---------------------------------")
    
    while True:
        print("1. Chat with the chatbot")
        print("2. Play a number guessing game")
        print("3. Quit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            print("You are now chatting with the chatbot.")
            print("Type 'exit' to return to the main menu.")
            while True:
                word = input().lower()
                if word == 'exit':
                    break
                chatbot(word)
        elif choice == '2':
            number_guess_game()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
