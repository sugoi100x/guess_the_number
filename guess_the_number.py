# "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
# This project uses CodeSkulptor own Modules


# Modulers used in this project
import simplegui
import random

# global variabless
secret_number = 0
num_range = 100
number_of_guesses = 7

# helper function to start and restart the game
def new_game():
    """
    This handler starts the game
    """
    
    global secret_number, number_of_guesses
    secret_number = random.randrange(0,num_range)
    
    # This condition sets number of guesses for each type of game
    if num_range == 100:
        number_of_guesses = 7
    else:
        number_of_guesses = 10
    
    # Prints informations about the new game
    print "New game. Range is [0," + str(num_range) + ")"
    print "Number of remaining guesses is " + str(number_of_guesses)
    print ""

# define event handlers for control panel
def range100():
    """
    This handler sets the range between [0, 100)
    for the game.
    """
    global num_range
    num_range = 100
    new_game()

def range1000():
    """
    This handler sets the range between [0, 1000)
    for the game.
    """
    global num_range
    num_range = 1000
    new_game()
    
def input_guess(guess):
    """
    This handler takes the player guess and
    output the results of the guess.
    """
    
    global number_of_guesses
    
    # Takes the player guess and prints.
    number = int(guess)
    print "Guess was", number

    # Prints the remaining guess
    number_of_guesses = number_of_guesses - 1
    print "Number of remaining guesses is " + str(number_of_guesses)
    
    # Prints information about of the player guesses
    if number_of_guesses == 0 and number != secret_number:
        print "You ran out of guesses. The number was " + str(secret_number)
        print ""
        new_game()
    else:
        if number == secret_number:
            print "Correct!"
            print ""
            new_game()
        elif number > secret_number:
            print "Lower!"
        else:
            print "Higher!"
        
    print ""
    
 

    
# create frame
frame = simplegui.create_frame("Guess the number",300,300)

# register event handlers for control elements and start frame
frame.add_button("Range is[0,100)", range100, 200)
frame.add_button("Range is[0,1000)", range1000, 200)
frame.add_input("Enter", input_guess, 100)


# call new_game 
new_game()