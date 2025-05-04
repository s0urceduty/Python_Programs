# Simple Calculator

# Copyright (c) 2023, Sourceduty
# https://about.me/sourceduty

# This software is free and open-source; anyone can redistribute it and/or modify it.


# Add two numbers
def add(x, y):
    return x + y

# Subtract two numbers
def subtract(x, y):
    return x - y

# Multipliy two numbers
def multiply(x, y):
    return x * y

# Divide two numbers
def divide(x, y):
    return x / y
    
# Power of
def power(x, y):
    return x ** y

# Menu 
print("SOURCEDUTY CALCULATOR")
print ("----------------------")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("6.Exit")
print ("----------------------")

while True:
    # User input choice
    choice = input("Enter function: ")

    # Check input choice
    if choice in ('1', '2', '3', '4',):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print ("----------------------")

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
            print ("----------------------")
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
            print ("----------------------")
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
            print ("----------------------")
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
            print ("----------------------")    
        
    else:
        print("Invalid input")
 
    # Menu exit option        
    if choice in ('6'):
        raise SystemExit    
            
        break                

input("Press enter to exit.")
