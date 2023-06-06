print(''' *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /________________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
******************************************************************************* ''')

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
enter = input("You'are at a cross road. Where do you want to go? Type 'left' or 'right'\n").lower()

if enter in ("left","l"):
    swim = input("You've come to a lake. There is an island in the middle of the lake, do you want to swim or wait? Type 'swim' or 'wait'\n").lower()
    if swim in ("wait","w"):
        door = input("It was a great choice to wait, which door now? Type 'red','blue' or 'yellow'\n").lower()
        if door in ("red","r"):
            print("Burned by fire. GAME OVER.")
        elif door in ("blue","b"):
            print("Eaten by beasts. GAME OVER.")
        elif door in ("yellow","y"):
            print("You win! CONGRATULATIONS")
        else:
            print("You chose a door that doesn't exist. GAME OVER.")
    else:
        print("Attacked by trout. GAME OVER.")
else:
    print("Fall into a hole. GAME OVER.")
