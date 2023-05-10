height = input("Enter your height in m:  ")
weight = input("Enter your weight in Kg: ")

converted_height = float(height)
converted_weight = float(weight)

bmi = int(converted_weight/converted_height**2)

print(bmi)
