# Calculate leap year
year = int(input("Which year do you wnat to check? \n"))

four = year % 4

if four > 0 :
    print(f"So the year {year} is not a leap year!!!")
else:
    hundred = year % 100
    if hundred > 0 :
        print(f"So the year {year} is a leap year!!!")
    else:
        four_hundred = year % 400
        if four_hundred > 0 :
            print(f"So the year {year} is not a leap year!!!")
        else:
            print(f"So the year {year} is a leap year!!!")
