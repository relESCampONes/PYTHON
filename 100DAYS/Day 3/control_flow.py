print("Welcome to the rollercoaster!!!")
height = float(input("What is your height? "))
age = int(input("How old are you?"))
bill = 0

if height >= 1.20:
    print("You can ride the rollercoaster!!!")
    if age <12:
        bill = 5
        print(f"Child tickets are ${bill}.")
    elif age <=18:
        bill = 7
        print(f"Youth tickets are ${bill}.")
    elif age >= 45 and age <=55:
        bill = 0
        print(f"Midlife tickets are ${bill}")
    else:
        bill = 12
        print(f"Adult tickets are ${bill}.")

    wants_photo = input("A photo costs $3, do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill = bill + 3

    print(f"Your final bill is ${bill}")
else:
    print("Wait a few years and come back!!!")
