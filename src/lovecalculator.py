print("The Love Calculator is calculating your score...")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_names = name1 + name2
lower_names = combined_names.lower()

t = lower_names.count('t')
r = lower_names.count('r')
u = lower_names.count('u')
e = lower_names.count('e')

first_digit_score = t + r + u + e

l = lower_names.count('l')
o = lower_names.count('o')
v = lower_names.count('v')
e = lower_names.count('e')

second_digit_score = l + o + v + e

Final_love_score = int(str(first_digit_score) + str(second_digit_score))

if Final_love_score < 10 or Final_love_score > 90:
    print(f"Your score is {Final_love_score}, you go together like coke and mentos.")
elif Final_love_score > 40 and Final_love_score < 50:
    print(f"Your score is {Final_love_score}, you are alright together.")
else: 
    print(f"Your score is {Final_love_score}.")
    
