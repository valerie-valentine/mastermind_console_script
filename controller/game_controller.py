from model.game import Game
from model.guess import Guess
from view.console_view import View


class Controller:
    def __init__(self, game=None):
        self.view = View()
        self.game = game

    def start_game(self):
        self.view.display_instructions()
        level = self.view.get_user_difficulty_level()
        self.game = Game(level)
        self.game.generate_answer()

        # Checks if valid answer is created otherwise cannot play game. If so, exit application.
        if not self.game.answer:
            self.view.display_random_number_api_error_feedback()
            return

        self.play_game()

    def play_game(self):
        while self.game.game_status == "In Progress":
            self.view.display_lives_remaining(self.game.lives)
            user_guess_input = self.view.get_valid_guess(
                self.game.difficulty_level, self.game.previous_guesses)
            current_guess = Guess(
                user_guess_input)
            current_guess.judge_guess(self.game.answer)
            self.view.display_guess_feedback(
                current_guess.correct_number, current_guess.correct_location)
            self.game.submit_user_guess(current_guess)

        self.check_game_over()

    def check_game_over(self):
        self.view.display_game_over_feedback(
            self.game.answer, self.game.game_status)
        self.play_another_game()

    def play_another_game(self):
        play_again = self.view.get_restart_game_input()

        if play_again == "yes":
            self.start_game()
