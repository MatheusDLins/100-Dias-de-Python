print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))

if height > 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you have to grow taller before you can ride.")

print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

name = (name1 + name2).lower()
t = name.count("t")
r = name.count("r")
u = name.count("u")
e = name.count("e")

l = name.count("l")
o = name.count("o")
v = name.count("v")

total1 = str(t + r + u + e)
total2 = str(l + o + v + e)

total = int(total1 + total2)

if(total < 10 or total > 90):
    print(f"Your score is {total}, you go together like coke and mentos.")
elif(total >= 40 and total <= 50):
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")