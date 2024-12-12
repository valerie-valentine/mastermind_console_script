from helper_functions import random_number_api


class Game:
    def __init__(self, difficulty_level, game_status="In Progress", answer=None,
                 previous_guesses_list=None, lives=10):
        self.lives = lives
        self.answer = answer
        # difficulty level is set by the controller when creating a new game
        self.difficulty_level = difficulty_level
        # teranary operator to check if previous_guesses_list is None and set it to an empty list to avoid immutable default arguments error
        self.previous_guesses = previous_guesses_list if previous_guesses_list is not None else []
        self.game_status = game_status

    def generate_answer(self):
        # generates and sets the answer based on difficulty level
        self.answer = random_number_api(self.difficulty_level)

    def submit_user_guess(self, guess):
        # Handles checking guess for game_over (win/loss) and game updating model
        self.previous_guesses.append(guess)

        if guess.guess_value == self.answer:
            self.game_status = "Won"
        else:
            self.lives -= 1
            if self.lives == 0:
                self.game_status = "Loss"
