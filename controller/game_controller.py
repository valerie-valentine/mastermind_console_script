from model.game import Game
from model.guess import Guess
from view.console_view import View


class Controller:
    def __init__(self, game=None):
        # Create view & game attributes and instantiates a View
        self.view = View()
        self.game = game

    # start game function -> initializes game & gets user input to set game level and generate answer
    def start_game(self):
        self.view.display_instructions()
        level = self.view.get_user_difficulty_level()
        self.game = Game(level)
        self.game.generate_answer()

        print(f"Debugging Test String: {self.game.answer} \n")

        # To check if we have a valid answer created otherwise cannot play game. Restart application.
        if not self.game.answer:
            self.view.display_random_number_api_error_feedback()
            return

        self.play_game()

    # Handles player turns & game control flow

    def play_game(self):
        # play_game -> controls flow of game (runs game loop), interacts with model/game/guess to check guesses and the view to display feedback
        while self.game.game_status == "In Progress":
            self.view.display_lives_remaining(self.game.lives)
            user_guess_input = self.view.get_valid_guess(
                self.game.difficulty_level, self.game.previous_guesses)
            # instantiate a guess and pass in valid guess data from view
            current_guess = Guess(
                user_guess_input)
            # move check_user_guess to guess & in constructor pass in answer to set correct_num & correct_loc of guess
            current_guess.judge_guess(self.game.answer)

            # provide feedback to user
            self.view.display_guess_feedback(
                current_guess.correct_number, current_guess.correct_location)

            # check guess is wrong and reduce lives or change game_status & return if (won/lost) - model
            self.game.submit_user_guess(current_guess)

        self.check_game_over()

    def check_game_over(self):
        # Handles gameover feedback
        self.view.display_game_over_feedback(
            self.game.answer, self.game.game_status)
        self.play_another_game()

    def play_another_game(self):
        play_again = self.view.get_restart_game_input()

        if play_again == "yes":
            # Reset game with self.start_game
            self.start_game()
