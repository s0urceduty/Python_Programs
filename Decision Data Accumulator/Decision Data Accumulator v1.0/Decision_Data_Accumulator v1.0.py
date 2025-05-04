
# Decision_Data_Accumulator v1.0
# Sorting alphabetical user input with Python

# Copyright (c) 2023, Sourceduty
# https://about.me/sourceduty

# This software is free and open-source; anyone can redistribute it and/or modify it.


import re

# User input
print ("Decision Data Accumulator V1.0")
print ("------------------------------")
s = user_input = str(input("Colour word entry: "))
print ("------------------------------")

while True:
    
# Alphabetical 
 if not s.isalpha():
   print ("Please enter only alphabetical characters.")
   print ("--------------------")
   print ("Not Alphabetical.")
   print ("--------------------")
   decision = False
   break
   input ("Press enter to exit.")

# Selection menu   
 if re.findall(r"[A-Za-z\-\']+", s):
   print ("Data accepted.")
   print ("--------------------")
   print ("1. View Decision")
   print ("2. View Decision Memory")
   print ("3. Clear Decision Memory")
   print ("-------------------")
   choice = input ("Enter function: ")
   decision = True

#--------------------------------------------------------
   
# Decision

#if decision == True:
   #if (s) == "Yellow":
    #yellow_decision = True
   #else:
    #yellow_decision = False

# Decision record

   #if yellow_decision == True:
    #decision_data = "Yellow"   
    #yellow_decision_data = True
    
#--------------------------------------------------------
    
# User input state  
   if user_input == "":
    print ("No input.")
    print ("--------------------")

    # Check input choice
   if choice in ('1', '2', '3',):
    print ("----------------------")

    if choice == '1':
        print ("Decision data here")
        print ("----------------------")
    elif choice == '2':
        print ("Decision memory here")
        print ("----------------------")
    elif choice == '3':
        print ("Decision memory cleared")
        print ("----------------------") 
        
    else:
        print ("Invalid input")     

 break

input ("Press enter to exit.")

