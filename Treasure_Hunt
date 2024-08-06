#Choice 1 - If "left", countinue. If "right", game over
#Choice 2 - If "wait", continue. If "swim", game over
#Choice 3 - If "yellow", you win! If "red" or "blue", game over. 

#ASCII webiste - ascii.co.uk/art

print('''
                    _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           ||.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'||||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-| |.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
               '-._'-.|| |' `_.-'
                    '-.||_/.-'
''') 

def try_again(): 
    Y_N = input("Try again? Y or N? ").lower()
    if Y_N == "y":
        game_on()
    
    elif Y_N == "n":
        print("Fair winds! May yer anchor be ever tight!")

    else:
        print("You did not enter a valid input. Goodbye.")

def game_on():
    choice1 = input('Avast! You\'ve come at a crossroad. Where do you want to go? Type "left" or "right".\n').lower()
    
    if choice1 == "left":
        choice2 = input('You\'ve now come to a lake where there\'s an island in the middle.'
                        '\nWhat are you going to do? Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower() 
    
        if choice2 == "wait":
            choice3 = input("You\'ve arrived at the island and have come across a weathered house with 3 different colored doors inside: red, yellow and blue."
            "\nWhich door are you choosing to open?\n").lower() 
    
            if choice3 == "yellow":
              print("Shiver me timbers! You have found the treasure! You WIN!")
    
            elif choice3 == "red":
                print("Blimey...you were burned up by a frenzied flame... Game over!")
                try_again()
            
    
            elif choice3 == "blue":
                print("Blimey...you were impaled by a booby trap. Game over!")
                try_again()
    
            else:
                print("You did not enter a valid input. Game over.")
                try_again()
    
        else: 
            print("Arr...you were eaten by blood-frenzied piranhas. Game over!")
            try_again()
    
    elif choice1 == "right": 
        print("You schallywag! You fell in to a hole."
              "\nGame over!")
        try_again()

    else: 
        print("You did not enter a valid input.")
        try_again()  

print("Ahoy matey! Welcome to the Treasure Hunt at Treasure Island!")
print("Your mission is to find the precious hidden treasure.")
game_on()
