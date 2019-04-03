# Random number guessing game
# April 2, 2019
# CTI-110 P5HW1 - Random Number
# Drake Cabanas
#

# Generate random numbers and assign cumpter number
# Input user guess
# Check user guess
# Track users guesses
# Compare user guess with computer number
# Display succcess or failure
# Restart game



# This program is a random number guessing game that restarts upon a successful guess
import random

# Generate the random number to be used
def generate_random_number():
    number = random.randint (1,100)
    return number

# Retrieve the user guess
def get_user_number( user_guess = 'Take a guess: ' ):
    guess = int(input(user_guess))
    return guess

# Check the user guess to see if it is correct
def check_guess(guess, number):
    if guess < number:
        return('Too low, try again.')
    elif guess > number:
        return('Too high, try again.')
    else:
        return('Congratulations! You guessed the right number.')
        
def main():
    # Sets the new game
    user_win = False
    new_game = True
    print('Welcome to my guessing game.')
    
    while user_win or new_game:
        # Tracks the guesses taken
        guesses_taken = 0
        # Takes the random number
        number = generate_random_number()
        # Takes the user guess
        guess = get_user_number()
        # Updates the guesses taken with the first guess
        guesses_taken = guesses_taken + 1
        # Checks the guess
        response = check_guess (guess, number)
        
        # While the response is anything but a win, continues retrieving user guesses
        while response != 'Congratulations! You guessed the right number.':
            # Prints if the guess was too high or too low
            print(response)
            # Retreives updated guess
            guess = get_user_number( "Try again: ")
            # Updates the guesses taken with subsequent guesses
            guesses_taken = guesses_taken + 1
            # Checks the Guess
            response = check_guess (guess, number)

        # Displays congragulations and number of guesses used
        print(response)
        print('It took you', guesses_taken, 'tries.')
        user_win = True


main()
