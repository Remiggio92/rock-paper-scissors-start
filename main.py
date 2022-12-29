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

#Write your code below this line 👇
import random
gestures = [rock, paper, scissors]
choice = len(gestures)
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if player_choice >= 3 or player_choice <0:
  print("You provided a wrong number. You lost!")
else:
  print(gestures[player_choice])
  computer_choice = random.randint(0, choice - 1)
  print(f"Computer chose:\n {gestures[computer_choice]}")

  if player_choice == 0 and computer_choice == 2:
    print("You won!")
  elif player_choice == 0 and computer_choice == 1:
    print("You lost!")
  elif player_choice == 1 and computer_choice == 0:
    print("You won!")
  elif player_choice == 1 and computer_choice == 2:
    print("You lost!")
  elif player_choice == 2 and computer_choice == 0:
    print("You lost!")
  elif player_choice == 2 and computer_choice == 1:
    print("You won!")
  else:
    print("It's a draw!")