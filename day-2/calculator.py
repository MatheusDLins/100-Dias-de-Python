print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15?"))
peoples = int(input("How many people to split the bill?"))

total = round((bill * (tip / 100 + 1)) / peoples, 2)

print(f"Each person should pay: ${total}")