#Love calculator
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is your name? \n")

bring = (name1 + name2).lower()

def verification(name):
    letter_t = name.count("t")
    letter_r = name.count("r")
    letter_u = name.count("u")
    letter_e = name.count("e")
    letter_l = name.count("l")
    letter_o = name.count("o")
    letter_v = name.count("v")

    first_digit = int(letter_t + letter_r + letter_u + letter_e)
    second_digit = int(letter_l + letter_o + letter_v + letter_e)

    return str(first_digit)+str(second_digit)


total = int(verification(bring))

if total < 10 or total > 90:
    print(f"Your score is {total}%, you go together like coke and mentos.")
elif total >= 40 and total <=50:
    print(f"Your score is {total}%, you are alright together.")
else:
    print(f"Your score is {total}%")
