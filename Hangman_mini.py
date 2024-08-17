import random  

stages = ['''
____________
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \  
     |
 ____|___
''', '''
 ____________
      |/      |
      |      (_)
      |      \|/
      |       |
      |      / 
      |      
  ____|___
''', '''
____________
     |/      |
     |      (_)
     |      \|/
     |       |
     |
     |
 ____|___
''', '''
____________
     |/      |
     |      (_)
     |      \|/
     |       
     |    
     |
 ____|___
''', '''
____________
     |/      |
     |      (_)
     |      \|
     |       
     |      
     |
 ____|___
''', '''
____________
     |/      |
     |      (_)
     |       |
     |       
     |      
     |
 ____|___
''', '''
____________
     |/      |
     |      (_)
     |      
     |      
     |      
     |
 ____|___
''', '''
____________
     |/      |
     |      
     |      
     |       
     |      
     |
 ____|___
'''] 
          
print(''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/     
''') 

wordlist = ["abominate", "abolish", "act", "goat", "groin", "haul", "heaven", "lord", "near", "far", "enlightened", "game", "fabulous", "extravagent"]

lives = 7

chosen_word = random.choice(wordlist)


placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
  placeholder += "_"
print(placeholder)


game_over = False
correct_letters = []

while not game_over:
  print(f"**********************************{lives}/7 LEFT**********************************")
  guess = input("Guess a letter: ").lower()

  # Ref. O12 
  if guess in correct_letters:
    print(f"You\'ve already guessed {guess}. It is in the word.")
  
  display = ""

  for letter in chosen_word:
    if letter == guess:
      display += letter
      correct_letters.append(guess)
    
    # Ref. O7
    elif letter in correct_letters:
      display += letter
    else:
      display += "_"
  
  print(display)

  # Ref. O9
  if guess not in chosen_word:
    lives -= 1
    print(f"You guessed {guess}, that is not in the word. You lose a life.") 

    if lives == 0:
      game_over = True
      print(f"**********************************IT WAS {chosen_word}! YOU LOSE**********************************")
  
  
  if "_" not in display:
    game_over = True   
    print("**********************************YOU WIN!!!**********************************")

  print(stages[lives])

# Objectives:
# 00: Print hangman logo at start of the game (can also use import function)
# O1: Randomly choose a word from the wordlist and assign it to a varaible called chosen_word. Then print it.
# O2: Ask the user to guess a letter and assign their answer to a variable called guess. Make lowercase. 
# O3: Check if the letter the user guessed is one of the letters in the chosen_word. Printr "Right" if it is, "Wrong" if it's not. 
# O4: Create a "placeholder" with the same number of blanks as the chosen_word
# O5: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string
# O6: Use a while loop to let the user guess again 
# O7: Change the for loop so that you keep the previous correct letters in display 
# 08: Create a variable called "lives" to keep track of the number of lives left and set it equal to 6. 
# 09: If guess is not a letter in the chosen_word, reduce "lives" by 1. If lives goes down to 0, then game should stop and it should print "you lose". 
# O10: Print the ASCII art from "stage" (list) that corresponds to the current number of lives the user has remaining
# 011: Print hangman logo at start of the game.
# O12: User feedback - telling them you've already guessed a letter and/or that they've guessed incorrectly. 
# O13: USer feedback - Update code to tell the user how many lives are left (out of 7). 
# Optional: Update the wordlist from a module or file to increase word count/list using import module functionality. "Stages" can also be imported.
