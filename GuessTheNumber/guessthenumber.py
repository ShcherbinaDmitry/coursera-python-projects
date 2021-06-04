# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math

range = 100 #When launching this program a new game starts in range [0:100), in order to start we need to define range
# helper function to start and restart the game
def new_game():
    ''' This function creates random number for player to guess and prints out starting message '''
    global number
    global number_of_guesses
    number = random.randrange(0, range)
    number_of_guesses = int(math.ceil(math.log(range,2)))
    print 'Starting a new game. Number of remaining guesses is', number_of_guesses
  

#Event handler
def range100():
    '''Event handler for a button that changes the range to [0,100) and starts a new game'''     
    global range
    range = 100
    new_game()

def range1000():
    '''Event handler for a button that changes the range to [0,1000) and starts a new game'''
    global range
    range = 1000
    new_game()
    
def input_guess(guess):
    '''Event handler for player guess which prints out players guess, remaining guesses and is a guess lower, higher of correct '''
    guess = int(guess)
    print
    global number_of_guesses
    print 'Your guess was', guess
    
    if number_of_guesses >0:
        if guess == number:
            print 'Correct!'
            new_game()
            
        elif guess > number:
            number_of_guesses -= 1
            print 'Number of remaining guesses is', number_of_guesses
            print 'Lower'
            
        elif guess < number:
            number_of_guesses -= 1 
            print 'Number of remaining guesses is', number_of_guesses
            print 'Higher'
                       
    else:
        print 'You are out of guesses. Starting a new round'
        new_game()
   

    
# create frame
frame = simplegui.create_frame('Guess the Number', 200, 200) #creating a frame

# register event handlers for control elements and start frame
frame.add_button('Start new game, range [0:100)',range100, 100) #adding a button to change range to 0-100
frame.add_button('Start new game, range [0:1000)',range1000, 100) #adding a button to change range to 0-1000
frame.add_input('Enter your guess', input_guess, 100) #adding an input field for players guess

new_game() #starting a new game at first launch of the program

