# Mastermind Game

Mastermind is a classic code-breaking game where you have to guess the correct combination of numbers within a limited number of attempts. This Python script allows you to play the game with different difficulty levels: easy, medium, and hard.

## How to Play

1. Run the `main.py` script in your Python environment.
2. The game will start, and you will be prompted to choose a difficulty level: easy, medium, or hard.
3. You will have 10 attempts to guess the correct number combination based on the chosen difficulty level:
   - Easy: 4 digits
   - Medium: 6 digits
   - Hard: 8 digits
4. After selecting the difficulty level, the game will provide you with instructions on how to play and the number of digits required for that level.
5. You will be prompted to make your guesses. Enter a 4, 6, or 8-digit number (depending on the difficulty level) as your guess. For example, if you're playing on the easy level, enter a 4-digit number like "1234."
6. The game will provide feedback after each guess. You will be told how many correct numbers are in your guess and how many of them are in the correct locations. For example, if you guessed "1234" and three of the numbers are correct but only one is in the correct position, you'll be told that you have "3 correct numbers and 1 correct location."
7. Continue making guesses until you either guess the correct combination or run out of attempts (10 attempts in total).
8. If you guess the correct combination, you win the game! If not, the game will reveal the correct combination.
9. The game ends, and you can choose to play again.

To quit the game, you can use `ctrl + c` at any time.

## Functions

Here's an explanation of the functions used in the `main.py` script:

- `main()`: The main function that controls the game flow. It initializes the game, handles user input, and checks if the game continues or is over.
- `start_instruction()`: Asks the player to choose a difficulty level and generates a random number for the answer. Returns the chosen level and answer.
- `game_instructions(level)`: Provides instructions to the player based on the chosen difficulty level.
- `random_number`: Makes the Api call to generate the random number.
- `get_valid_guess`: Validates the format and content of the player's guess.
- `check_user_guess: contains the logic to check user guess against answer and calculate the correct number of numbers guessed and numbers with location also guessed.
- `choose_level`: validates and retrieves user's input for level (code length).
- start_instructions: prints the instructions to user.

Enjoy playing Mastermind! Have fun playing the Mastermind game and try to crack the code within the limited number of attempts. Good luck!
