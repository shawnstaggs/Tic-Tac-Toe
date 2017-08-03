# Create Tic Tac Toe for the python bootcamp
from __future__ import print_function
from IPython.display import clear_output
def display_board(board):
    
    pass

def player_input():
    pass

def place_marker(board, marker, position):
    pass

def win_check(board, mark):
    pass

import random
def choose_first():
    print("Player %s goes first.", random.choice([1,2]))

def space_check(board, position):

    pass

def full_board_check(board):

    pass

def player_choice(board):

    pass

def replay():
    again = input("Would you like to play again?(Y/N)")
    if again.isalpha():
        if again[0] == 'y':
            return True
        else:
            return False
    else:
        replay()

print('Welcome to Tic Tax Toe!')

while True:
    choose_first()

#    set up the game

#    while game on 
#        player 1 turn

#        player 2 turn


    if not replay():
        break
