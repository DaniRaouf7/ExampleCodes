a = 10
b = 12
c = 15

print("Welcome to the tip calculator!")
Total_bill = float(input("What was the total bill? $ \n"))
Tip = int(input(f"How many tip would you like to give? {a}, {b} or {c}? \n"))
People = int(input("How many people to split the bill? \n"))



Calculate = (Total_bill * (1+(Tip/100)))/People

Final_Result = round(Calculate, 2)

print(f"Each person should pay: \n ${Final_Result}")

