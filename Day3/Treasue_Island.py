print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|________
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

turn = (input("You have reached a cross road. where do you want to go? Left or Right\n")).lower()
if turn != "left":
    print("Fell into a hole.\nGame Over!")
else:
    wait = (input("You have reached a lake and there is an Island at the middle. Type \"wait\" " "to wait for a boat or "
                  "\"Swim\" " "to swim across\n")).lower()
    if wait != "wait":
        print("Attacked by an angry trout.\n Game Over!")
    else:
        doors = (input("You have arrived at the Island unharmed.There is a house with three doors.One red, one yellow, "
                       "one blue.Which color do you choose?\n")).lower()
        if doors == "red":
            print("You have entered a room full of fire.\n Game Over!")
        elif doors == "blue":
            print("You have entered a room full of beasts.\n Game Over")
        elif doors == "yellow":
            print("Congratulations, found the treasure. You Win!")
        else:
            print("You chose a door that doesn\'t exist. Game Over!")
