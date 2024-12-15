from art import game_logo, win_logo, lost_logo


class View:

    def display_instructions(self):
        print(game_logo)
        print("Welcome to Mastermind! \n")
        print("Play against the computer and break the code to win. \n")
        print("A random number from the digits 0-9 will be generated based on your chosen level. \n")
        print("You will have 10 attempts to guess the number. \n")
        print("Hints will be provided to help you along the way. \n")
        print("Good luck! \n")

    def get_user_difficulty_level(self):
        levels = {
            "easy": 4,
            "medium": 6,
            "hard": 8
        }

        while True:
            level = input(
                f"Please select a level to play (easy: {levels["easy"]} digits, medium: {levels["medium"]} digits, hard: {levels["hard"]} digits): ").lower()
            if level not in levels:
                print("Error: Please enter a valid level (easy, medium, hard).")
            else:
                return levels[level]

    def display_lives_remaining(self, lives):
        print(f"You have {lives} attempts remaining. \n")

    def get_valid_guess(self, level, previous_guesses):
        while True:
            guess = input(
                f"Make a guess: \n"
            )
            if not guess.isnumeric():
                print("Please enter a number with a numerical value. \n")
            elif len(guess) != level:
                print(f"Please enter a number with {level} digits. \n")
            elif guess in [guess.guess_value for guess in previous_guesses]:
                print(f"You have already guessed {
                      guess}. Please try again. \n")
            else:
                return guess

    def display_guess_feedback(self, correct_number, correct_location):
        if correct_number == 0 and correct_location == 0:
            print("All incorrect \n")
        else:
            print(f"{correct_number} correct number and {
                  correct_location} correct location \n")

    def display_game_over_feedback(self, answer, game_status):
        if game_status == "Won":
            print(win_logo)
            print(f"Congrats, you guessed the correct answer! \n")
        else:
            print(lost_logo)
            print(f"Game over! The correct answer was: {answer} \n")

    def get_restart_game_input(self):
        while True:
            user_input = input(
                "Would you like to play again? (Enter 'yes' or 'no'): ").lower()
            if user_input != "yes" and user_input != "no":
                print("Please enter a valid response. \n")
            elif user_input == "no":
                print("Thanks for playing!")
                return user_input
            else:
                return user_input

    def display_random_number_api_error_feedback(self):
        print("Failed to generate an answer from API. Please try again in a few.")
