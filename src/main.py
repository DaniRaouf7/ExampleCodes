# Disclaimer this ain't main script, these are just annotations for python


# Basic print statement
print("Hello world!")

# Print multiple outputs with different lines use \n
print("hello world\nhello world")

# Input
input("What is your name?")

# Hello + input
print("Hello " + input("What is your name?") + "!")

# Variable coding
name = input("What is your name?\n")
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

# Loops
fruits_new = ["Apple", "Peach", "Pear"]
for fruit in fruits_new:
    print(fruit)
    print(fruit + " Pie")


# FizzBuzz Bro
for number in range(1, 101,):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else: 
    print(number)
    
# While loop
hurdles = 6
while hurdles > 0:
    jump()
    hurdles -= 1
    
    
def greet(Name):
    print('Hallo' + Name)
    print('You are cool')
    print('Bye')

greet(" Dani!")

def greet_with_name(name):
    print(f'Hello {name}!!')
    print(f'You are so cool {name}!')
    
greet_with_name("Dani")

# Parameter is name and argument is Dani
def greet_with(name, location):
    print(f'Hello {name}!')
    print(f'How is it like in {location}?')
    
greet_with(name = "Dani",location = "Pijnacker")

# To run your main script & Activate venv

"""
venv\Scripts\Activate   
"""

if __name__ == "__main__":
    main()

# And you need

python -m src._main


# Dictionaries
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "Iterates some code untill some certain condition, doing it over and over again"
}

    

''' Disclaimer, we can use thonny for debugging and to see what a code actually does!'''