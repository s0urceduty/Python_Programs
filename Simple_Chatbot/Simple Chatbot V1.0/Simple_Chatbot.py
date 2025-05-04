# Simple Chatbot V1.0
#🤖 Text-based conversational chatbot.

# Copyright (c) 2023, Sourceduty
# This software is free and open-source; anyone can redistribute it and/or modify it.

import random

cmd_Greet = ["hello", "hi", "hey",
             "chatbot",
             "respond"]
rply_Greet = ["Hello",
              "Greetings!",
              "How can chatbot help you?"
              ]

cmd_Leave = ["Bye",
             "Chatbot sleep",
             "Goodbye",
             ]
rply_Leave = ["Goodbye"]

cmd_Ask = ["name",
           "identify"
           ]
rply_Ask = ["My name is Chatbot"]

cmd_Sad = ["bad",
           "sad",
           "not feeling well",
           "unhappy",
           "depressed",
           ]
rply_Sad = ["text",
            "text",
            "text",
            "text"]

cmd_Happy = ["happy",
             "good",
             "joyful",
             "calm",
             "great",
             "amazing",
             "awesome"]
rply_Happy = ["text",
              "text",
              "text"]

cmd_Bored = ["boring",
             "bored",
             "bore",
             "nothing to do"]
rply_Bored = ["Watch some stand up comedy video",
              "Install a new game.",
              "Install mix or pyshow.",
              "Code python.",
              "Take a nap.",
              "Check out...",
              "Check out..."]


def chatbot(text):
    for word in text.split():
        if word in cmd_Bored:
            response = random.choice(rply_Bored)
            print(response.lower())
            return response
        elif word in cmd_Leave:
            response = random.choice(rply_Leave)
            print(response.lower())
            return response
        elif word in cmd_Ask:
            response = random.choice(rply_Ask)
            print(response.lower())
            return response
        elif word in cmd_Sad:
            response = random.choice(rply_Sad)
            print(response.lower())
            return response
        elif word in cmd_Happy:
            response = random.choice(rply_Happy)
            print(response.lower())
            return response
        elif word in cmd_Greet:
            response = random.choice(rply_Greet)
            print(response.lower())
            return response
    print("Invalid entry.")
    return False


def main():
    print ("Simple Chatbot V1.0")
    print ("---------------------------------")
    while True:
        print("Text entry: ", end='')
        word = input().lower()
        chatbot(word)


if __name__ == "__main__":
    main()
