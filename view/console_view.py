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

    # Maybe move this function to the view & then call in play game method of controller
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
        # lives will get passed in from the controller
        print(f"You have {lives} attempts remaining. \n")

    def get_valid_guess(self, level, previous_guesses):
        # control flow concept - move to controller? / knows a little bit about validation & what constitutes a valid guess
        # controller passes guess into game.is_valid_guess method - a validation method
        # Maybe okay in view because it is basic validation?

        # maybe move validation to game or guess model????
        while True:
            # User input - asks user to make a guess - view
            guess = input(
                f"Make a guess: \n"
            )
            if not guess.isnumeric():
                # User feedback - checks for numeric value - view
                print("Please enter a number with a numerical value. \n")
            elif len(guess) != level:
                # User feedback - checks for correct length - view
                print(f"Please enter a number with {level} digits. \n")
            elif guess in [guess.guess_value for guess in previous_guesses]:
                # make this a view function to give feedback & get a valid new guess
                print(f"You have already guessed {
                      guess}. Please try again. \n")
            else:
                return guess

    def display_guess_feedback(self, correct_number, correct_location):
        # correct_number & correct_location get passed in from the controller
        if correct_number == 0 and correct_location == 0:
            print("All incorrect \n")
        else:
            print(f"{correct_number} correct number and {
                  correct_location} correct location \n")

    def display_game_over_feedback(self, answer, game_status):
        # displays the feedback when a game is over -> won or loss
        # game status & answer will get passed in from the controller
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
