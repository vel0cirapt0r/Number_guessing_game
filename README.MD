Number Guessing Game

This is a simple Python-based Number Guessing Game where you try to guess a randomly selected secret number within a user-defined range. You have a limited number of attempts based on the size of the range, making it challenging and fun!

How It Works

1. Set the Range: You begin by specifying a starting and ending number for the range of possible numbers.


2. Guess the Secret Number: The program will select a random number within your range, and you’ll try to guess it.


3. Hints: After each guess, the program will tell you if your guess was too high or too low, helping you zero in on the secret number.


4. Limited Attempts: The number of guesses is limited, calculated based on the size of the range. This adds a layer of challenge and requires strategic guesses.


5. Win or Lose: If you guess the number within the allotted attempts, you win! Otherwise, the game reveals the correct number, and you can try again.



Example

Here’s how a typical game session might look:

1. The game welcomes you and asks for a starting and ending number for the range.


2. If the range is valid, the game announces the number of guesses you have.


3. You start guessing, with the game giving hints after each guess.


4. If you guess correctly, it congratulates you! If not, it provides the answer after you’ve used all attempts.



Code Overview

Random Number Generation: A random integer is selected within your chosen range.

User Input: The program requests input for both the range and each guess.

Hints: After each incorrect guess, the game tells you if the guess was too high or too low.

Winning and Losing Conditions: The game congratulates you if you guess correctly; otherwise, it reveals the number after your chances run out.


How to Run

1. Make sure you have Python installed.


2. Save the code to a file (e.g., guessing_game.py).


3. Run the game by typing python guessing_game.py in your terminal or command prompt.



Enjoy the challenge, and happy guessing!
