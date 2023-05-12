print("Welcome to the rollercoaster!!!")
height = float(input("What is your height? "))
age = int(input("How old are you?"))

if height >= 1.20:
    print("You can ride the rollercoaster!!!")
    if age <12:
        print("Please pay $5.")
    elif age <=18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Wait a few years and come back!!!")
