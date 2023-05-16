# Pizza Order Practice
print("Welcome to Python Pizza Deliveries!!!")

print("Small Pizza: $15\nMedium Pizza: $20\nLarge Pizza: $25\n\nPepperoni for Small Pizza: + $2")
print("Pepperoni for Medium or Large Pizza: + $3\n\nExtra cheese for any size pizza: + $1\n")
size = input("What size pizza do you want? S, M, or L ? ")
add_pepperoni = input("Do you want pepperoni? Y or N ? ")
extra_cheese = input("Do you want extra cheese? Y or N ? ")
bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")
