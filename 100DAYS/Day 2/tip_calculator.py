print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people_to_split = int(input("How many people to split the bill? "))

total = bill * (1 + tip/100)
split = round(total/people_to_split, 2)

print(f"Each person should pay: ${split}")
