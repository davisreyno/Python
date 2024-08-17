# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""" 

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

print("Rock. Paper. Scissors. Shoot!")

#Computer input
def game_on():
  import random 
  global computer_choice
  computer_choice = random.randint(0, 2)

  if computer_choice == 0:
    print(rock)
    print("Computer chose Rock\n")

  elif computer_choice == 1:
    print(paper)
    print("Computer chose Paper\n")

  elif computer_choice == 2:
    print(scissors)
    print("Computer chose Scissors\n")


#User input
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))

if user_choice == 0:
  print(rock)
  print("You chose Rock")
  game_on()

elif user_choice == 1:
  print(paper)
  print("You chose Paper")
  game_on()

elif user_choice == 2:
  print(scissors)
  print("You chose Scissors")
  game_on()

#Invalid inputs
if user_choice >= 3 or user_choice < 0:
  print("You did not enter a valid input. Game over.")


#Game on

if user_choice == 2 and computer_choice == 0:
  print("You LOSE. Game over.")

elif not user_choice == 2 and computer_choice == 0:
  print("You WIN.")

elif user_choice < computer_choice: 
  print("You LOSE. Game over.")

elif user_choice > computer_choice:
  print("You WIN.") 

elif user_choice == computer_choice:
  print("It's a DRAW.")




