#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



print("Welcome to the Pypassword Generator!\nBefore Generating your password, please make sure your password has a TOTAL MINIMUM OF 12 characters!!!!")

letters_total = int(input("How many letters would you like in your password?\n"))

symbols_total = int(input("How many symbols would you like?\n"))

numbers_total = int(input("How many numbers would you like?\n"))

if letters_total + symbols_total + numbers_total < 12:
    print("The total number of characters should be at least 12.")
else:
    password_list = []

    for char in range(letters_total):
        password_list.append(random.choice(letters))

    for char in range(symbols_total):
        password_list.append(random.choice(symbols))

    for char in range(numbers_total):
        password_list.append(random.choice(numbers))
        
    random.shuffle(password_list)
    
    random_generated_password = ''.join(password_list)


print(f"Here is you password: {random_generated_password}")

