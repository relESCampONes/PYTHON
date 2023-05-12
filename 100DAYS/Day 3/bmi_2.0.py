# Bmi Calculator 2.0

height = float(input("Enter your height in m: "))
weight = float(input("Ehter your weight in Kg: "))

bmi = round(weight/height**2, 2)
interpretation = ""

if bmi < 18.5 :
    interpretation = "underweight."
elif bmi < 25 :
    interpretation = "normal weight."
elif bmi < 30 :
    interpretation = "overweight."
elif bmi < 35 :
    interpretation = "obese."
else:
    interpretation = "clinically obese."

print(f"Your BMI is {bmi}, you are {interpretation}")
