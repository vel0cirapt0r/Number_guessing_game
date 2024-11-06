import math  # For calculating the optimal number of chances
import random  # For generating the secret number

# Introduction to the game
print("Welcome to my Number Guessing Game!\nYou'll have to guess the secret number within a range of your choice.")
print("Let's get started!")

# Prompt the user to set the guessing range
while True:
    try:
        # Get the lower bound of the range from the user
        lower_bound = int(input("Please enter the starting number for the range: "))

        # Get the upper bound of the range from the user
        upper_bound = int(input("Please enter the ending number for the range: "))

        # Check if the provided range is valid
        if lower_bound >= upper_bound:
            print("Oops! The starting number should be less than the ending. Please try again.")
        else:
            print(f"Great! I'm thinking of a number between {lower_bound} and {upper_bound}.")
            print("Let's see if you can guess it!")
            break  # Exit loop if a valid range is provided
    except ValueError:
        # Handle cases where input is not an integer
        print("Please enter valid integers for the range.")

# Calculate the maximum number of chances using binary search logic
chances = math.ceil(math.log2(upper_bound - lower_bound + 1)) - 1
print(f"You have {chances} chances to guess the secret number.")

# Generate the secret number within the specified range
guess = random.randint(lower_bound, upper_bound)

# Initialize guess counter to track the number of attempts
guess_counter = 0

# Main game loop, running until the player either guesses the number or exhausts their chances
while guess_counter < chances:
    guess_counter += 1  # Increment attempt count
    client_guess = int(input("Take a guess: "))  # Prompt user for their guess

    # Check if the user's guess is correct
    if client_guess == guess:
        print(f"Congratulations! The number is {guess} and you guessed it in {guess_counter} attempt(s).")
        break  # Exit loop on correct guess

    # Check if the user has used up all attempts without guessing correctly
    elif guess_counter >= chances and client_guess != guess:
        print(f'Oops, sorry! The number was {guess}. Better luck next time!')

    # Provide hints if the guess was incorrect and attempts are still available
    elif client_guess < guess:
        print('Your guess is too low.')
    elif client_guess > guess:
        print('Your guess is too high.')
