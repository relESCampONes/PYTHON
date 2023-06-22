import random

print("Welcome to the Jokenpô Game!!!")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    ROCK
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
    PAPER
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    SCISSORS
'''

choices = [rock,paper,scissors]
print(rock,paper,scissors)
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if choice in (0,1,2):
    print("\n-------JOKENPÔ-------")
    drawn = random.randint(0, 2)
    print(choices[choice],"\nX")
    print(choices[drawn])
    if choice == drawn:
        print("You Tied!!!")
    elif choice == 0 and drawn == 1:
        print("You Lose!!!")
    elif choice == 0 and drawn == 2:
        print("You Win!!!")
    elif choice == 1 and drawn == 0:
        print("You Win!!!")
    elif choice == 1 and drawn == 2:
        print("You Lose!!!")
    elif choice == 2 and drawn == 0:
        print("You Lose!!!")
    elif choice == 2 and drawn == 1:
        print("You Win!!!")
else:
    print("Choose between 0 and 2, try again!!!")