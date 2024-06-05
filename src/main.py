# Basic print statement
print("Hello world!")

# Print multiple outputs with different lines use \n
print("hello world\nhello world")

# Input
input("What is your name?")

# Hello + input
print("Hello " + input("What is your name?") + "!")

# Variable coding
name = input("What is your name?")
length = len(name)
print(length)

# f-String
score = 2
height = 1.5
print(f"your score is {score} and your height is {height}")

# if statements
if height > 2:
    print("You are long")
    if score == 3:
        print("x")
    elif score == 4:
        print("b")
else:
    print("You are short")

# Randomness in python
import random

# Lists in python
# Very important in python
banana = "yellow"
kiwi = "brown"
fruits = [banana, kiwi]