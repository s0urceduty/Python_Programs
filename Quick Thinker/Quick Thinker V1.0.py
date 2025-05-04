# Quick Thinker Game
# Copyright (C) 2024, Sourceduty - All Rights Reserved.

import random
import time

# List of words
words = ["apple", "banana", "orange", "grape", "pineapple", "watermelon", "strawberry", "blueberry", "kiwi", "peach"]

def generate_challenge():
    # Select a random word from the list
    word = random.choice(words)
    # Select a random initial letter from the chosen word
    initial_letter = random.choice(word)
    return word, initial_letter

def play_game():
    score = 0
    print("Welcome to Quick Thinker! Type 'quit' at any time to end the game.")
    print("You will be presented with a random word with a random initial letter.")
    print("You have 5 seconds to guess the entire word.")
    print("Let's start!")
    while True:
        word, initial_letter = generate_challenge()
        print("The word starts with the letter:", initial_letter)
        start_time = time.time()
        user_input = input("Your guess: ").lower()
        end_time = time.time()

        if user_input == "quit":
            break
        
        if (end_time - start_time) > 5:
            print("Time's up! You took too long.")
            continue
        
        if user_input == word:
            score += 1
            print("Correct!")
        else:
            print("Incorrect! The correct word was:", word)

    print("Game Over! Your final score is:", score)

if __name__ == "__main__":
    play_game()
