#
# imports
#

import simplegui
import random
import math

#
# globals
#

secret_number = 0
number_of_guesses = 0
guess_ct = 0
range = 0
win = 0

#
# helper function to start and restart the game
#
def new_game():
    # initialize global variables used in your code here
    global secret_number
    global number_of_guesses
    global guess_ct
    global range
    
    number_of_guesses = math.ceil(math.log(range, 2))
    secret_number = random.randint(0, range)
    textbox_guess.set_text("")
    guess_ct = 0
        
    if range != 0:
        print
        print
        print "Guess a number between 0 and ", range - 1, "in at most ", number_of_guesses, " guesses:"
    print
    


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global range
    
    range = 100
    new_game()
    
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global range
    
    range = 1000
    new_game()
    
def input_range(range_str):
    # text box allowing user to select their own range, and start a new game
    global range
    
    range = int(range_str)
    textbox_range.set_text("")
    
    new_game()
    
def input_guess(guess_str):
    # main game logic goes here	
    global secret_number
    global number_of_guesses
    global guess_ct
    global win
    
    guess_num = int(guess_str)
    print "Guess", guess_ct + 1, " was: ", guess_num
    if guess_num < secret_number:
       guess_ct += 1 
       print "Higher!  You have ", number_of_guesses - guess_ct, " guesses left!"
        
    elif guess_num > secret_number:
       guess_ct += 1
       print "Lower! You have ", number_of_guesses - guess_ct, " guesses left!"
        
    else:
        print "You guessed it in ", guess_ct + 1, " out of ", number_of_guesses, " tries!"
        win = 1
    
    if (number_of_guesses - guess_ct) == 0 and not win:
        print "The number was: ", secret_number, ". You loose!"
    else:
        textbox_guess.set_text("")
        textbox_range.set_text("")

    
# create frame
frame = simplegui.create_frame("Guess The Number", 300,300)

# register event handlers for control elements and start frame
button_run = frame.add_button("New Game!", new_game)
button_game100 = frame.add_button("1-100", range100)
button_game1000 = frame.add_button("1-1000", range1000)
textbox_range = frame.add_input("Enter your own range:", input_range, 200)
textbox_guess = frame.add_input("What is your guess?", input_guess, 50)

# call new_game -- Instructions say that app must start with a game of 100, 
# hence the globals being set below
range = 100
number_of_guesses = 7
secret_number = random.randint(0,range)
guess_ct = 0
new_game()


# always remember to check your completed program against the grading rubric
