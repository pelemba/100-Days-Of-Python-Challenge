import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rock_paper_scissors = [rock, paper, scissors]
computer_choice = random.randint(0, 2)
player_choice = int(input("What do you choose. Type 0 for Rock, 1 for Paper, 2 for Scissors: "))

if player_choice >= 3 or player_choice < 0:
    print("Invalid choice!")
else:
    print(rock_paper_scissors[player_choice])
    print(f"Computer chose: {rock_paper_scissors[computer_choice]}")

    if player_choice == 0 and computer_choice == 2:
        print("You won!")
    elif player_choice == 2 and computer_choice == 0:
        print("You lost!")
    elif player_choice < computer_choice:
        print("You lost!")
    elif player_choice > computer_choice:
        print("You won!")
    else:
        print("It's a tie!")

