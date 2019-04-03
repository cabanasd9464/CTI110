# Rock paper scissors versus a computer opponent
# April 2, 2019
# CTI-110 P5HW2 - Rock, Paper, Scissors Game
# Drake Cabanas
#

# Generate random numbers and assign computer number
# Assign numbers to variables
# Input user choice
# Compare user choice and computer choice
# Determine winner
# Display winner or rematch



# This program is a game of rock paper scissors versus a computer.
import random

# Constants
rock = 1
paper = 2
scissors = 3

# Generate the random number to be used by the computer
def generate_random_number():
    computer_number = random.randint (1,3)
    return computer_number

# Calculate computer choice based on random number
def get_computer_choice (computer_number):
    # Assign numbers to game choices
    if computer_number == 1:
        computer_choice = 'rock'
    elif computer_number == 2:
        computer_choice = 'paper'
    elif computer_number == 3:
        computer_choice = 'scissors'
    return computer_choice

# Retrieve the user choice
def get_user_choice():
    user_choice = input( 'Please enter your choice: rock, paper, or scissors? ')
    return user_choice

# Determine winner based on rules
def decide_winner(computer_choice, user_choice):
    # Assign winning statements
    rock_wins = 'Rock crushes scissors.'
    paper_wins = 'Paper covers rock.'
    scissors_wins = 'Scissors cuts paper.'
    winner = 'You tied. Go again.'
    statement = ''

    # Paper beats rock
    if computer_choice == 'rock' and user_choice == 'paper':
        winner = 'You'
        statement = paper_wins
    elif computer_choice == 'paper' and user_choice == 'rock':
        winner = 'The computer'
        statement = paper_wins
    # Rock beats scissors
    if computer_choice == 'scissors' and user_choice == 'rock':
        winner = 'You'
        statement = rock_wins
    elif computer_choice == 'rock' and user_choice == 'scissors':
        winner = 'The computer'
        statement = rock_wins
    # Scissors beats paper
    if computer_choice == 'paper' and user_choice == 'scissors':
        winner = 'You'
        statement = scissors_wins
    elif computer_choice == 'scissors' and user_choice == 'paper':
        winner = 'The computer'
        statement = scissors_wins
        
    return winner, statement

# Resets if both players choose same option
def tie():
    # Grabs computer number
    computer_number = generate_random_number()
    # Converts computer number to rock/paper/scissors
    computer_choice = get_computer_choice(computer_number)
    # Grabs user choice
    user_choice = get_user_choice()
    # Displays to user what the computer chose
    print('The computer chose',computer_choice,)
    # Decides winner
    winner, statement = decide_winner( computer_choice, user_choice)
    # Displays winner when no tie
    if winner != 'You tied. Go again.':
        print( winner, 'won')
    return winner

def main():
    # Grabs computer number
    computer_number = generate_random_number()
    # Converts computer number to rock/paper/scissors
    computer_choice = get_computer_choice(computer_number)
    # Grabs user choice
    user_choice = get_user_choice()
    # Displays to user what the computer chose
    print('The computer chose', computer_choice,)
    # Decides winner. 
    winner, statement = decide_winner( computer_choice, user_choice)
    # Displays winner when no tie
    if winner != 'You tied. Go again.':
        print( winner, 'won.',statement,)
    # Displays tie, resets to tie function
    while winner == 'You tied. Go again.':
        print(winner)
        winner = tie()
        
main()


